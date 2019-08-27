

import re

tt="Tina is a good girl, she is cool, clever, and so on..."
rr=re.compile(r'\w*oo\w*')

print(rr.findall(tt))
p = re.compile(r'\d{3}-\d{6}')
print(p.findall('010-628888'))
print(p.search('010-628888').group())

a = re.search("a(\d+)b",'a3333b').group()
print(a)
b = re.findall(r"a(\d+?)b",'a3333b')
print(b)

src='那个人看起来好像一条狗，哈哈'


print(src.replace('，哈哈','.'))