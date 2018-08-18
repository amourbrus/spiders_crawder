"""
创建进程和销毁进程耗时严重
"""
import time, multiprocessing, random, os

def work(n):
    print("%d 开始执行： pid = %d" % (n, os.getpid()))
    s_time = time.time()  # 开始时间
    time.sleep(random.random())

    e_time = time.time()   # 结束时间
    print("%d 结束， 耗时 %.2f, pid = %d" % (n, e_time - s_time, os.getpid()))

def main():
    # 创建进程，指定进程函数
    # 耗时在创建进程，销毁进程
    for i in range(10):
        p = multiprocessing.Process(target=work, args=(i, ))
        p.start()


if __name__ == '__main__':
    main()
