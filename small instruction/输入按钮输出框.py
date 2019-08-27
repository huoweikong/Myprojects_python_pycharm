import tkinter as tk
from baidufanyi import *
window = tk.Tk()

window.title("英汉词典")

window.geometry('500x300')


e = tk.Entry(window, bg='Yellow', show = None)#显示成明文形式
e.pack()

t1 = tk.Text(window, height=3, bg='aqua')
t1.pack()

t2 = tk.Text(window, height=6, bg='snow')
t2.pack()

def trans():
    var = t1.get('1.0','3.end')
    var=baidu_fanyi(var)
    t2.insert('insert', var)


b1 = tk.Button(window, text='翻译', width=15, height=2, command=trans)
b1.pack()



# 第8步，主窗口循环显示
window.mainloop()