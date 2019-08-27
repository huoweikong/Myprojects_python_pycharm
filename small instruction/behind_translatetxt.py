import re

with open('test.txt') as f:
    str = f.read()
w = re.findall(r'\n', str)
w = re.sub(r'\n', ' ', str)

with open('qu-n.txt','w') as f:
    f.write(w)
print(w)