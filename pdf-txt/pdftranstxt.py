import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

'''
 解析pdf 文本，保存到txt文件中/Users/aiqiangyun/Documents/pdf-txt
'''
from_pdf=input("请输入PDF文件名：（不含后缀）\n  --->")
to_txt = from_pdf+'_done'
path = (r'/Users/aiqiangyun/Documents/pdf-txt/%s.pdf'%from_pdf)
def parse():
    fp = open(path, 'rb') # 以二进制读模式打开
    #用文件对象来创建一个pdf文档分析器
    praser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages(): # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(r'/Users/aiqiangyun/Documents/pdf-txt/%s.txt'%to_txt, 'a') as f:
                        results = x.get_text()
                        #print(results)
                        f.write(results + '\n')
def clearhuanhang():
    file3 = open('/Users/aiqiangyun/Documents/pdf-txt/%s.txt' % to_txt, 'r', encoding='utf-8')
    file4 = open('/Users/aiqiangyun/Documents/pdf-txt/%s4.txt' % to_txt, 'w')
    try:
        for line in file3.readlines():
            line = line.strip('\n')
            file4.write(line)
    finally:
        file3.close()

def clearBlankLine():
    file1 = open('/Users/aiqiangyun/Documents/pdf-txt/%s.txt'%to_txt, 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open('/Users/aiqiangyun/Documents/pdf-txt/%s2.txt'%to_txt, 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()

if __name__ == '__main__':
    parse()
    #clearhuanhang()