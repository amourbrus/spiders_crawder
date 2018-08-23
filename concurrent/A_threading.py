import time
import threading
num = 234

# 方式一，通过类创建
# class one_thread(threading.Thread):
#     def run(self):
#         for i in range(5):
#             print("one_thread")
#             time.sleep(1)
#
# obj = one_thread()
# obj.start()

# 方式二 普通创建 ==============
def foo1(n):
    global num
    for i in range(5):
        num += 1  # 共享资源
        print('my name is {} {}'.format(n, num))
        print('foo1111-------------------')
        time.sleep(1)

def foo2(n):
    global num
    for i in range(5):
        num += 1
        print('my name is {} {}'.format(n, num))
        print('foo2222-------------------')
        time.sleep(1)

def main():
    t1 = threading.Thread(target=foo1, args=(11,))  # 验证传参，可迭代的参数，传递的函数名
    t2 = threading.Thread(target=foo2, args=(22,))
    t1.start()
    t2.start()

    for i in range(5):
        print("main threading ", threading.enumerate(), num)  # enumerate 所有的线程号
        time.sleep(1)

if __name__ == '__main__':
    main()
