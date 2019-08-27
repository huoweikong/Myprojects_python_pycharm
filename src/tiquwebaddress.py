
import re
info = '<a href="http://www.baidu.com">baidu</a>'
rr=re.compile(r'http://www.\S+.c.{1,2}')

print(rr.findall(info))
rr2=re.compile(r'>\w*<')
print(rr2.findall(info))

text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', '[ ]', text))
print(re.subn(r'\s+', '[ ]', text))

s = "我是一个人(中国人)aaa[真的]bbbb{确定}"
a = re.subn('\(.*\)|\[.*\]|\{.*\}', '', s)
#a = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", s)
print(a)