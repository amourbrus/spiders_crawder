### 多线程
A_threading.py
*多线程实现多任务   普通创建方法
1,import threading
2,t = threading.Thread(target=func,[args=(xxx,)])
3,t.start()
线程id,threading.enumerate()>>>返回当前程序的线程信息,>list
通过类创建线程,,定义类
线程共享全局变量  ---> 锁
子线程传参*
**通过类创建一个
1,定义类,继承threading.Thread
2,这个类的threading.Thread中,有一个run(),派生类要重写
3,只有这个run()函数是线程函数
4,通过start()间接调用**
B_process.py
进程核心代码
1,import multiprocessing
2,p1=multiprocessing.Process(target=func, args=(x,))
3,p1.start()

进程号 os.getpid()获取当前的进程号, os.getppid()获取父进程号

给子进程传参  参数使用和线程一样
进程间不共享全局变量   num为例说明   >>> 因此有进程间通信queue
队列对象不能在父进程与子进程间通信，这个如果想要使用进程池中使用队列则要使用multiprocess的Manager类
  # q = multiprocessing.Manager().Queue()

### 协程
```python
import gevent
from gevent import monkey

# 打补丁  只要有阻塞耗时(大部分)的地方，就算不是gevent.sleep(), 也会自动切换
monkey.patch_all()
# 终极版   主线程不会等待协程，所以需要join
  gevent.joinall([
      gevent.spawn(work1, 4),
      gevent.spawn(work2, 6)
  ])
```
协程池和进程池 -- 整合接口---> C_pool.py
