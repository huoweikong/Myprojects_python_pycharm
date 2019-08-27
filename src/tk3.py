from tkinter import *

root = Tk()

photo = PhotoImage(file='182.gif')
theLabel = Label(root,
                 text="xuepydaoQQ",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=("苹方", 20),
                 fg='white')
theLabel.pack()
'''
textLabel = Label(root, text="您所下载的电影需要年满十八岁才能观看",
                  justify=LEFT,
                  padx=10,
                  pady=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='182.gif')
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)
'''
mainloop()
