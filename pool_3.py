from multiprocessing import Pool, freeze_support
import time

def sum_num(num1, num2):

    return num1 + num2


start = time.time()
freeze_support()
if __name__ == '__main__':
    with Pool(2) as p:
        print(p.starmap(sum_num, zip([1,3,5], [2,4,6])))
print("Time taken = {0:.5f}".format(time.time() - start))