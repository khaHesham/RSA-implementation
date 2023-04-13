import RSA as RSA
import math
import time


def factorize(n):
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return i, n // i
    return None



key_sizes = [2**i for i in range(2,7)]

for key_size in key_sizes:
    with open("analysis.txt", "a") as file:
    # Write some text to the file
        file.write(f"key size : {key_size} \n")

        pub , prv=RSA.generate_keys(key_size)
        file.write(f"public-key : {pub} privat-key : {prv} \n")

        t1 = time.time()
        p, q = factorize(pub[0])
        t2 = time.time()

        file.write(f"p = {p}, q = {q}\n")
        file.write(f"elapsed time in seconds : {(t2-t1)} \n")
        file.write(f"elapsed time in millis : {(t2-t1)*1000} \n")
        file.write("\n\n\n")





