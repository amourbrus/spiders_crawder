# 问题导入：共享资源导致资源竞争问题
import threading
import time
g_num = 0

def foo1(n, mutex):
    # mutex.acquire()
    global g_num
    for i in range(n):
        # time.sleep(0.001)
        g_num += 1
        # mutex.release()
    print('foo1 ----->',g_num)


def foo2(n, mutex):
    global g_num

    # mutex.acquire()
    for i in range(n):
        # time.sleep(0.001)

        g_num += 1
        # mutex.release()
    print('foo2---->', g_num)

def main():
    # 创建锁，默认是打开的
    mutex = threading.Lock()
    t1 = threading.Thread(target=foo1, args=(1000000, mutex))
    t2 = threading.Thread(target=foo2, args=(1000000, mutex))
    t1.start()
    t2.start()
    time.sleep(10) # 保证子线程执行完
    # t1.join()
    # t2.join()
    print('finally num --->', g_num)

if __name__ == '__main__':
    main()

# 都在循环外面加锁，都不解锁，就会导致最后的结果阻塞(无finally)，两个都是100000
# 在外部加锁，再解锁，就
# 不加锁，两者数据都是错的（一错都错，全局变量） -- foo1 1279745 foo2 1393459 finally_num  1393459
