
start=1
while True:
    if start==51:
        break
    print (start*2 ,end=' ')
    start +=1
print()

start=1
while True:
    if start==100:
        break
    if start%2==1:
        print (start,end=' ')
    start +=1

print()

sum=0
start=1
while True:
    if start==101:
        break
    if start%2 ==1:
        sum=sum+start
    if start%2==0:
        sum=sum-start
    start +=1
print(sum)