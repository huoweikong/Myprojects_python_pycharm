f = open('iteracast.txt', 'a')
while True:
    input1 = input()
    if input1=='exit':
        f.close()
        break
    f.write(input1 + '\n')
f = open('iteracast.txt','r')
'''while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)'''
# print(f.read())
z = f.readlines()
print(z)
for i in z:
    print(i, end='')
f.close()

f1 = open('iteracas.txt', 'w')
f1.writelines(["1", "2", "3"])
#    此时test1.txt的内容为:123
f1.close()
f1 = open('iteracas.txt', 'r')

z=f1.readlines()
print(z)
for i in z:
    print(i, end='')
f1.close()

