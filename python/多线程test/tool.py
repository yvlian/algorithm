from androguard.misc import AnalyzeAPK
from androguard.core.analysis.analysis import ExternalMethod
import matplotlib.pyplot as plt
import networkx as nx
import torch
import os
import random
import re
import sys
import json

def get_sensitive_api(path):
    with open(path, 'r') as f:
        sensitive_api = json.load(f)
        sensitive_api_dic = {}
        i = 0
        for k, apis in sensitive_api.items():
            for api in apis:
                # api = re.findall(':.*\(',api)[0].lstrip(':').rstrip('(').lower()
                api = api.lstrip('<').rstrip('>').lower().replace('()','')
                sensitive_api_dic[api] = i
                i += 1
    return sensitive_api_dic

def delete_xref0_nodes(CFG):
    nodes, external_methods = list(CFG.nodes)[:], []
    for orig_method in nodes:
        if not CFG.degree()[orig_method]:
            CFG.remove_node(orig_method)


def delete_init_and_external_method(CFG, dx, sensitive_api_dic):
    nodes = list(CFG.nodes)[:]

    for orig_method in nodes:
        if isinstance(orig_method, ExternalMethod):
            CFG.remove_node(orig_method)
            continue
        m_a = dx.get_method(orig_method.get_method())
        if m_a:
            ins_seq = get_instruction_seq_for_func(m_a, sensitive_api_dic)
            if ins_seq =='':
                for p in CFG.predecessors(orig_method):
                    for s in CFG.successors(orig_method):
                        CFG.add_edge(p,s)
                CFG.remove_node(orig_method)


def get_instruction_seq_for_func(m_a, sensitive_api_dic):
    basic_blocks = m_a.basic_blocks.get()

    # 该循环是获取CFG中的每一个节点(即APK中的自定义函数)得敏感API序列
    api_seq = []
    for i in basic_blocks:
        instructions = list(i.get_instructions())#instructions由一系列的dalvik指令组成
        for ins in instructions:#遍历每一个dalvik指令
            if 'invoke' in ins.get_name():#获取dalvik指令的操作码，若操作码中含有invoke字样，说明该指令调用了API
                operands = ins.get_operands()#从dalvike中提取参数
                if operands:
                    # api = re.findall('->.*\(',str(operands[-1][-1]))[0].lstrip('->').rstrip('\(').lower()
                    api = str(operands[-1][-1]).lower().lstrip('l').replace('/', '.').replace(';->', ':')
                    api = re.sub('\(.*\).*', '()', api).replace('()','')#这两步是为了获取到调用的API
                    if sensitive_api_dic=={} or api in sensitive_api_dic.keys():#使用敏感API表提出非敏感API,保留敏感API
                        api_seq.append(api)
    text =  '|'.join([x.replace(' ','') for x in api_seq]).replace(';','')
    return text


# def get_graph_and_nodes_ins_for_apk(apk_file, lock, f, sensitive_api_dic):
#     try:
#         # 由此步可获取APK文件的函数调用图CFG，其中包括邻接矩阵CFG.A、节点CFG.nodes、边CFG.edges等信息
#         print(apk_file)
#         a, d, dx = AnalyzeAPK(apk_file)
#         CFG = dx.get_call_graph()
#
#         # delete_xref0_nodes(CFG)
#         # 这里是为了删除一些孤立点和一些非自定义的函数（与任务相关，可不看）
#         #tips:用户自定义的函数，会androguard被标注为InternalMethod,非用户定义的函数被标注为ExternalMethod
#         delete_init_and_external_method(CFG, dx, sensitive_api_dic)
#         ins_seqs,nodes = {},list(CFG.nodes)[:]
#
#         #遍历CFG中每一个节点，并获取节点内的API序列
#         for orig_method in nodes:
#             m_a = dx.get_method(orig_method.get_method())
#             ins_seq = get_instruction_seq_for_func(m_a,sensitive_api_dic)
#             ins_seqs[orig_method] = ins_seq
#         methods,adj,node_feature = {},[],{}
#         for k in list(ins_seqs.keys()):
#             methods[k] = len(methods)
#         edges,L = CFG.edges,len(methods)
#         for s,t,_ in edges:
#             if s!=t:
#                 adj.append((methods[s],methods[t]))#adj为CFG的邻接矩阵
#         for k,v in methods.items():
#             node_feature[v] = ins_seqs[k]#node_feature为CFG中每个节点对应的敏感API序列
#         if lock is None:
#             print('不加锁：' + apk_file)
#             f.write(apk_file + '    ' + str(node_feature) + '\n')
#         else:
#             # print('加锁前：'+apk_file)
#             lock.acquire()
#             f.write(apk_file+'    '+str(node_feature)+'\n')
#             lock.release()
#             # print('加锁后：'+apk_file)
#         return adj,node_feature
#     except BaseException:
#         # if sys.platform == 'linux':
#         #     cmd = 'mv '+apk_file+' apk_data/error'
#         # else:
#         #     cmd = 'move '+apk_file+' apk_data/error'
#         #     cmd = cmd.replace('/','\\')
#         # os.system(cmd)
#         a = 1
#         print('APK文件异常')
#         return None,None


def get_graph_and_nodes_ins_for_apk(apk_file, sensitive_api_dic,thread_num):
    # 由此步可获取APK文件的函数调用图CFG，其中包括邻接矩阵CFG.A、节点CFG.nodes、边CFG.edges等信息
    print(apk_file)
    a, d, dx = AnalyzeAPK(apk_file)
    CFG = dx.get_call_graph()

    # delete_xref0_nodes(CFG)
    # 这里是为了删除一些孤立点和一些非自定义的函数（与任务相关，可不看）
    # tips:用户自定义的函数，会androguard被标注为InternalMethod,非用户定义的函数被标注为ExternalMethod
    delete_init_and_external_method(CFG, dx, sensitive_api_dic)
    ins_seqs, nodes = {}, list(CFG.nodes)[:]
    # 遍历CFG中每一个节点，并获取节点内的API序列
    for orig_method in nodes:
        m_a = dx.get_method(orig_method.get_method())
        ins_seq = get_instruction_seq_for_func(m_a, sensitive_api_dic)
        ins_seqs[orig_method] = ins_seq
    methods, adj, node_feature = {}, [], {}
    for k in list(ins_seqs.keys()):
        methods[k] = len(methods)
    edges, L = CFG.edges, len(methods)
    for s, t, _ in edges:
        if s != t:
            adj.append((methods[s], methods[t]))  # adj为CFG的邻接矩阵
    for k, v in methods.items():
        node_feature[v] = ins_seqs[k]  # node_feature为CFG中每个节点对应的敏感API序列
    # print('before reading')
    # with open(f'{dir}/FFCG_process_{thread_num}.txt', 'a') as f:
    #     f.write(apk_file + '    ' + str(node_feature) + '\n')
    # print('wirtten')
    return apk_file,adj,node_feature

