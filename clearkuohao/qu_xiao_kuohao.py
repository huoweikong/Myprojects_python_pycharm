import re

def clear1():
    p = re.compile(r'［.*?］')
    from_txt = input("请输入绝对路径文件TXT：\n ---->")
    to_txt = from_txt[0:-4] + '_clearbrackets.txt'
    f = open('%s' % from_txt, 'r')
    str1 = f.read()
    f.close()
    str2 = p.sub('', str1)
    with open('%s' % to_txt, 'a') as f:
        f.write(str2)

def clearbrackets():
    p = re.compile(r'（[0-9图表]+.*?[0-9]*）')
    from_txt = input("请输入绝对路径文件TXT：\n ---->")
    to_txt = from_txt[0:-4] + '_clearbrackets.txt'
    f = open('%s' % from_txt, 'r')
    str1 = f.read()
    f.close()
    str2 = p.sub('', str1)
    with open('%s' % to_txt, 'a') as f:
        f.write(str2)

def clear2():
    p = re.compile(r'（[0-9图表]+.*?[0-9]*）')
    from_txt = input("请输入绝对路径文件TXT：\n ---->")
    to_txt = from_txt[0:-4] + '_clearbrackets2.txt'
    f = open('%s' % from_txt, 'r')
    str1 = f.read()
    f.close()
    str2 = p.sub('', str1)
    with open('%s' % to_txt, 'a') as f:
        f.write(str2)

def clear3():
    # ^(?!.*hello) 代表不匹配hello
    #（[(\u4e00-\u9fa5)a-zA-Z]{1,2}.{1,20}[0-9年]{1,2}）
    p = re.compile(r'（.*?）')
    from_txt = input("请输入绝对路径文件TXT：\n ---->")
    to_txt = from_txt[0:-4] + '_clear3-3.txt'
    f = open('%s' % from_txt, 'r')
    str1 = f.read()
    f.close()
    str2 = p.sub('', str1)
    with open('%s' % to_txt, 'a') as f:
        f.write(str2)

if __name__ == '__main__':
    select = input("请输入文献类型：(1~3)\n"
                   "1 ［4］\n"
                   "2 (1)|(2-4)|(图1)|(表2)\n"
                   "3 （Doudna和Charpentier，2014）|（Varshavsky等人，2006年）\n"
                   "----->")
    if select == '1':
        clear1()
    elif select == '2':
        clear2()
    elif select == '3':
        clear3()


