import multiprocessing
import time

def foo1(q):
    buf = "hello"
    for x in buf:
        q.put(x)
        print("what put in is {}".format(x))
        time.sleep(0.01)

def foo2(q):
    while True:
        v = q.get()
        print("what get is {}".format(v))
        if q.empty():
            break

def main():
    # 创建一个队列，队列可以理解为管道，一端写内容，另外一端取内容
    # 返回值，就是队列对象，可以传参，写了一个数字，不写代表个数不做限制
    q = multiprocessing.Queue()
    # 队列对象不能在父进程与子进程间通信，这个如果想要使用进程池中使用队列则要使用multiprocess的Manager类
    # q = multiprocessing.Manager().Queue()

    p1 = multiprocessing.Process(target=foo1,args=(q,))
    p2 = multiprocessing.Process(target=foo2,args=(q,))
    p1.start()
    p1.join() # ensure foo1 finish first then foo2 can get q
    p2.start()

if __name__ == '__main__':
    main()
