from tool import get_graph_and_nodes_ins_for_apk,get_sensitive_api
import os
from multiprocessing import Pool
import time
def func(thread_num):
    def myCallBack(x):
        apk_file,adj,node_feature = x
        with open(f'{dir}/FFCG_process_{thread_num}.txt', 'a') as f:
            f.write(apk_file + '    ' + str(node_feature) + '\n')

    dir = 'drebin'
    writed_data = f'{dir}/FFCG_process_{thread_num}.txt'
    if os.path.exists(writed_data):
        os.remove(writed_data)
    sensitive_api_dic = get_sensitive_api(f'{dir}/sensitive_api.txt')
    begin = time.time()
    process_pool = Pool(thread_num)
    for apk in os.listdir(dir):
        if not apk.endswith('.apk'):continue

        result = process_pool.apply_async(get_graph_and_nodes_ins_for_apk,args=(f'{dir}/{apk}',sensitive_api_dic,thread_num,),callback=myCallBack)#非阻塞的调用函数
        # adj,node_feature = result.get()
        # with open(f'{dir}/FFCG_process_{thread_num}.txt', 'a') as f:
        #     f.write(apk + '    ' + str(node_feature) + '\n')
    process_pool.close()#调用join之前，先调用close或者terminate方法，否则会出错。执行完close后不会有新的进程加入到pool
    process_pool.join()#join函数等待所有子进程结束。
    time_used = time.time()-begin
    with open(writed_data, 'a') as f:
        f.write('used time:    '+str(time_used))
    print(f'costed time {thread_num}:    '+str(time_used))
if __name__=='__main__':
        func(15)

# 设电脑CPU核心数N=4
# CPU密集型程序，一般设置线程数为N+1
# I/O密集型程序，一般设置线程数为2N

#由于一个叫GIL的存在，使得Python在同一时间只能运行一个线程，所以只占用了一个CPU，由于我的电脑是4核的，所以CPU利用率就是25%了。
# 此程序，提取100个恶意软件FFCG
# 设置线程数为1时，540.13s
# 设置线程数为5时，576.31s
# 设置线程数为8时，576.51s

#使用进程池
# 设置进程数为1时，515.02s
# 设置进程数为5时，184.74s
# 设置进程数为8时，153.593s
# 设置进程数为15时，147.39s

