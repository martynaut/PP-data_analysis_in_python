from multiprocessing import Pool, freeze_support
import time

def sum_num(num):
    return num[0] + num[1]


start = time.time()
freeze_support()
if __name__ == '__main__':
    with Pool(2) as p:
        print(p.map(sum_num, [(1,2), (3,4), (5,6)]))
print("Time taken = {0:.5f}".format(time.time() - start))