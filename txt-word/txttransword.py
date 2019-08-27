#创建并写入word文档
import docx

#创建内存中的word文档对象
from_txt = input("请输入要转换的txt： \n   --->")
to_word = from_txt + '_t2w'
with open(r'/Users/aiqiangyun/Documents/pdf-txt/%s.txt' % from_txt) as f:
    str1 = f.readlines()
file = docx.Document()

for line in str1:
        # 写入若干段落
    file.add_paragraph(line)



        # 保存

file.save(r"/Users/aiqiangyun/Documents/txt-word/%s.docx" % to_word)


