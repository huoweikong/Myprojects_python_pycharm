import re

with open('PEDV表位.txt') as f:
    lines=str(f.readlines())
print(lines)
#line='(fsd)我爱你（中国）\n'
pattern = re.compile(r"[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+")
string = re.sub(pattern, "", lines)
print(string)

with open('qukuohao2.txt','w') as f:
    f.write(string)
