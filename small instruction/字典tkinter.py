from tkinter import *
class App:
  def __init__(self,root):
    #定义帧
    frame = Frame(root)
    frame.pack()
    self.frame = frame
    w = Label(frame,text = "calculator")
    w.pack()
    self.newinput()
    #调用回调函数
    button1 = Button(frame,text='1',fg="red",command = lambda : self.buttoncb(1))
    button1.pack()
    button2 = Button(frame,text='2',fg="red",command = lambda : self.buttoncb(2))
    button2.pack()
    button = Button(frame,text='Quit',fg="red",command = root.quit)
    button.pack()
  def newinput(self):
    v = StringVar()
    e = Entry(self.frame,textvariable = v)
    self.v = v
    e.pack()
  #定义回调函数
  def buttoncb(self,i):
    #print "button"
    val = self.v.get()
    self.v.set(val+str(i))
root=Tk()
a = App(root)
root.mainloop()