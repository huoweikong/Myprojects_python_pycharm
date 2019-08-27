import math


N = int(math.sqrt(1997))
for i in range(1,N+1):
     x = i
     for j in range(1,N+1):
        y = j

        if x ** 2  + y ** 2 == 1997:
            print("x为%d, y为%d" %(x,y))
            print(x+y)


