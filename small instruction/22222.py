

from tkinter import *
import requests
import gzip
import json
from tkinter import messagebox
from baidufanyi import *
root = Tk()


def main():
    # 输入窗口
    root.title('英语字典')  # 窗口标题
    Label(root, text='请输入英文').grid(row=0, column=0)  # 设置标签并调整位置
    enter = Entry(root)  # 输入框
    enter.grid(row=0, column=1, padx=20, pady=20)  # 调整位置
    enter.delete(0, END)  # 清空输入框
    enter.insert(0, 'love')  # 设置默认文本
    # enter_text = enter.get()#获取输入框的内容

def trans():
    enter=Entry(root)
    enter.insert(0, '湘潭')






    # 布置按键
Button(root, text="确认", width=10, command=trans) \
        .grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text='退出', width=10, command=root.quit) \
        .grid(row=3, column=1, sticky=E, padx=10, pady=5)
root.mainloop()


if __name__ == '__main__':
    main()
