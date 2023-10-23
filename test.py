import threading
import time
print(time.time())
def work(number, mss):
    res = 1
    for i in range(1, number + 1):
        res *= i
    print(mss)

def innerwork(number, marta, mss):
    
    for i in range(marta):
        work(number, mss)
    print(time.time())


# work(2, 't1 ishladi')
# work(5, 't2 ishladi')
# work(1, 't3 ishladi')
# t1 = threading.Thread(target=innerwork, args=(10, 5, 't1 ishladi',))
# t2 = threading.Thread(target=innerwork, args=(100, 20, 't2 ishladi',))
# t3 = threading.Thread(target=innerwork, args=(50, 8, 't3 ishladi',))
innerwork(10, 5, 't1 ishladi',)
innerwork(10, 5, 't1 ishladi',)
innerwork(10, 5, 't1 ishladi',)
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()

print("Done!")