import random
a = [ random.uniform(0, 6) for i in range(4)]


b = [random.uniform(4, 6), random.uniform(3,4), random.uniform(1,2), random.uniform(0,1)]


c = list(map(lambda x : round(x, 1), b))

print(c)



print(round(0.123456789, 2))