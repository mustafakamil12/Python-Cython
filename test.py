import prime_finder
import time

start_vanilla = time.time()
prime_finder.prime_finder_vanilla(10000)
end_vanilla = time.time()

print(end_vanilla - start_vanilla)


start_c = time.time()
prime_finder.prime_finder_optimized(10000)
end_c = time.time()

print(end_c - start_c)