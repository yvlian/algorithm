from tool import get_graph_and_nodes_ins_for_apk,get_sensitive_api
import os
from threading import Thread,Lock
import time
from queue import Queue

print('++++++单线程++++')
begin = time.time()
dir = 'drebin'
writed_data = f'{dir}/FFCG.txt'
if os.path.exists(writed_data):
    os.remove(writed_data)
sensitive_api_dic = get_sensitive_api(f'{dir}/sensitive_api.txt')
f = open(writed_data,'a')
for apk in os.listdir(dir):
    if apk.endswith('.txt'):continue
    adj, index2node = get_graph_and_nodes_ins_for_apk(f'{dir}/{apk}', None,f,sensitive_api_dic)
f.close()
time_used = time.time()-begin
with open(writed_data, 'a') as f:
    f.write('used time:    '+str(time_used))
print('used time:    '+str(time_used))