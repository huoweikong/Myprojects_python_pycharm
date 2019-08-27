'''输出基因信息表中特定的基因信息

这里以本题为例：在基因的信息A文件中，找出B文件中存在的基因名的信息
文件B中只包含基因名，这里讲文件B按行读取，保存在一个列表中，列表中的每一个元素对应一个基因名'''
import os
get_name=[]
for _name in open('/home/miaoyr/perl_practice/test2_file/2.1name.txt'):
        get_name.append(_name.replace('\n',''))
print (get_name)
f=open('2-1-output.txt','w')
for name in get_name:
        m_name="'$3~/^"+name+"/ {print $0}'"
        cmd="'awk' %s '/home/miaoyr/perl_practice/test2_file/2.1Predicted_Targets_Info.txt'" % m_name
        output=os.popen(cmd).readlines()
        f.writelines(output)
f.close()
