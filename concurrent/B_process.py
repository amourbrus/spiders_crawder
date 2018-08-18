import multiprocessing
import os
import time

num = 200 # 验证进程间不共享全局变量

def foo1(*args, **kwargs):
    global num
    print("foo1---{}".format(num-50))
    print("args--",args)  # 智慧执行一次
    print("kwargs--",kwargs)
    for i in range(10):
        i += 1
        print("now is foo1 ---pid={}, ppid={}".format(os.getpid(), os.getppid()))
        time.sleep(0.01)  # for cpu not to idle run


def foo2(*args, **kwargs):
    global num
    print("foo2---{}".format(num+100))
    for i in range(10):
        i +=1
        print("now is foo2 ---pid={}, ppid={}".format(os.getpid(), os.getppid()))
        time.sleep(0.01)  # for cpu not to idle run 空转

def main():
    p1 = multiprocessing.Process(target=foo1, args=("hello", "it's me", 12), kwargs={"name":"red","age":19})
    p2 = multiprocessing.Process(target=foo2)
    p1.start()
    p2.start()
    # p2.join()  # 等待p2跑完，注掉之后三者一起轮流跑
    for i in range(10):
        i += 1
        print('it is main -----')
        time.sleep(0.01)

if __name__ == '__main__':
    main()
