from Tkinter import *
import time


root = Tk()
root.title("Plug Control")
root.geometry("260x160")

def on1() :
    execfile("sock1ON.py")
    return

def off1() :
    execfile("sock1OFF.py")
    return

def on2() :
    execfile("sock2ON.py")
    return

def off2() :
    execfile("sock2OFF.py")
    return

def on3() :
    execfile("sock3ON.py")
    return

def off3() :
    execfile("sock3OFF.py")
    return

def on4() :
    execfile("sock4ON.py")
    return

def off4() :
    execfile("sock4OFF.py")
    return

def onALL() :
    execfile("sockALLON.py")
    return

def offALL() :
    execfile("sockALLOFF.py")
    return

def quit():
    root.quit()

Button(root, text="Quit", command=quit).pack(side=BOTTOM)
sockALL = Frame(root)
sockALL.pack(side=BOTTOM)
sock4 = Frame(root)
sock4.pack(side=BOTTOM)
sock3 = Frame(root)
sock3.pack(side=BOTTOM)
sock2 = Frame(root, bg="red")
sock2.pack(side=BOTTOM)
sock1 = Frame(root)
sock1.pack(side=BOTTOM)
Button(sockALL, text='ALL ON', command=onALL).pack(side=LEFT)
Button(sockALL, text='ALL OFF', command=offALL).pack(side=LEFT)
Button(sock4, text='4   ON', command=on4).pack(side=LEFT)
Button(sock4, text='4   OFF', command=off4).pack(side=LEFT)
Button(sock3, text='3   ON', command=on3).pack(side=LEFT)
Button(sock3, text='3   OFF', command=off3).pack(side=LEFT)
Button(sock2, text='2   ON', command=on2).pack(side=LEFT)
Button(sock2, text='2   OFF', command=off2).pack(side=LEFT)
Button(sock1, text='1   ON', command=on1).pack(side=LEFT)
Button(sock1, text='1   OFF', command=off1).pack(side=LEFT)

root.mainloop()


