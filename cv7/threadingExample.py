import threading


def fun(num):
    for _ in range(50):
        print("Thread %s" % num)

threads = []

for i in range(4):
    t = threading.Thread(target=fun, args=(i, ))
    t.start()
    threads.append(t)



for thread in threads:
    thread.join()
