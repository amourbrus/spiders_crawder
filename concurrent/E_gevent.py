import gevent
import time
from gevent import monkey

"""
from greenlet import greenlet
import time

def test1():
    while True:
        print("-----A------")
        gr2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print("-----B------")
        print("---B----")
        gr1.switch(0.5)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()

# DONE

import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)

g1 = gevent.spawn(f,5)
g2 = gevent.spawn(f,5)
g3 = gevent.spawn(f,5)
g1.join()
g2.join()
g3.join()
"""
# gevent协程调用的策略，利用这个单任务等待的时间，用于切换任务

# 打补丁  只要有阻塞耗时(大部分)的地方，就算不是gevent.sleep(), 也会自动切换
monkey.patch_all()

def work1(n):
    for i in range(n):
        print("1111111")
        time.sleep(0.2)
def work2(n):
    for i in range(n):
        print("2222222")
        time.sleep(0.5)

def main():
    # 主线程不会等待协程
    # 不让主线程结束
    # 协程本质上是单任务，永远执行在main()循环中
    # s1 = gevent.spawn(work1, 5)
    # s2 = gevent.spawn(work2, 6)
    # while True:
    #     print("333333333")
    #     gevent.sleep(0.2)

    # gevent.sleep(20)     # 5s后主线程结束了，程序也会停止
    # s1.join()    # waiting for s1 run over
    # s2.join()


    # 终极版   主线程不会等待协程，所以需要join
    gevent.joinall([
        gevent.spawn(work1, 4),
        gevent.spawn(work2, 6)
    ])


if __name__ == '__main__':
    main()
