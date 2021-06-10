from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print('\n')

def foo(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line:')

    p1 = Process(target=foo, args=('Bob',))
    p2 = Process(target=foo, args=('Alice',))

    p1.start()
    p2.start()

    #p1.join()
    #p2.join()
