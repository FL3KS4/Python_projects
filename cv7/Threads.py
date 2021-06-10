import threading
import math
import time
import queue
from datetime import datetime
import multiprocessing

testSheet = []

def is_prime(n):
    if (n < 2) or (n % 2 == 0 and n > 2):
        return (n, False)    
    elif n == 2:
        return (n, True)  
    elif n == 3:
        return (n, True)   
    else:
        for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return (n, False)       
        return (n, True)


def prepareData(x):
    for i in range(1,x+1):
        testSheet.append(i)

def seqTest(n):
    start = time.time()
    prepareData(n)

    for i in testSheet:
        is_prime(i)

    end = time.time()
    return((end - start) * 1000)



def threader(n, out):
    out.append(is_prime(n))


def threadTest(n):  
    start = time.time()
    prepareData(n)

    threads = []
    primeSUM = []
    
    for i in testSheet:
        t = threading.Thread(target=threader, args=(i, primeSUM))
        threads.append(t)

    for thread in threads:
            thread.start()   

    for thread in threads:
            thread.join()
         
    end = time.time()
    return((end - start) * 1000)


def MTPrepare(n,proc, fun):
     with multiprocessing.Pool(processes=proc) as pool:
        return pool.map(fun, n)

def MTTest(n,process,fun):
    start = time.time()
    prepareData(n)

    MTPrepare(testSheet,process,is_prime)

    end = time.time()
    return((end - start) * 1000)


def testit(n, process, fun):
    
    a = (seqTest(n))

    b = 0#threadTest(n)

    c = MTTest(n,process, fun)

    print (a,b,c)

    f = open("tests.txt", "a")
    f.write("___________________________________________________\n")
    f.write("|Numbers \t" + " | Function \t"  + " | Time(ms) \n")
    f.write("|"+str(n)+" | Seq Test \t\t\t" + " | "+str(a)+"\n")
    f.write("|"+str(n)+" | Thread Test \t\t" + " | "+str(b)+"\n")
    f.write("|"+str(n)+" | MultiProces Test \t" + " | "+str(c)+ " | Processes: " +str(process)+"\n")
    f.write("___________________________________________________\n")
    f.close()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    testit(4000000, 4, is_prime)

