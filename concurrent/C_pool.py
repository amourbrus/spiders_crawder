import time
import os
import random
import multiprocessing
# from multiprocessing.dummy import Pool
# pool = Pool()
def work(n):
    print("{} 开始执行：pid={}".format(n,os.getpid()))
    s_time = time.time()
    time.sleep(random.random)
    s_time = time.time()
    print("{} 耗时:{}".format(n, e_time-s_time))

def main():
    pool = multiprocessing.Pool(4)
    for i in range(10):
        pool.apply_async(work, args=(i,))

    pool.close()
    pool.join()
# 协程池 ==============================
# '''
# 由于gevent的Pool的没有close⽅法，也没有异常回调参数
# 引出需要对gevent的Pool进⾏⼀些处理，实现与进程池⼀样接⼝，实现线程和协程
# 的⽆缝转换
# '''
from gevent.pool import Pool as BasePool
import gevent.monkey
gevent.monkey.patch_all() # 打补丁，替换内置的模块

class Pool(BasePool):
# '''协程池
# 使得具有close⽅法
# 使得apply_async⽅法具有和线程池⼀样的接⼝
# '''
    def apply_async(self, func, args=None, kwds=None, callback=None
, error_callback=None):
        return super().apply_async(func, args=args, kwds=kwds, call
back=callback)
    def close(self):
# '''什么都不需要执⾏'''
        pass

if __name__ == '__main__':
    main()
