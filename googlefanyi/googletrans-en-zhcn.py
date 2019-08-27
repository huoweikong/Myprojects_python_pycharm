#使用方法
from googletrans import Translator
translator = Translator(service_urls=['translate.google.cn'])

with open('txt2.txt') as f:
    source=f.read()
#source = '我还是不开心！'

text = translator.translate(source, src='en', dest='zh-cn').text

with open('txt3.txt','a') as f:
    f.write(text)

print(text)
