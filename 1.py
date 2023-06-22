from tkinter import *
from tkinter import messagebox
import base64
screen=Tk()
screen.geometry("420x420")
screen.title("Incryption and Decryption")
screen.configure(bg="grey")
def encrypt():
    password=code.get()
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="pink")
        Message=A.get(1.0,END)
        encode_message=Message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")
        Label(screen1,text="code is encrypted",font="impack 10 bold").place(x=5,y=6)
        B=Text(screen1,font="30" ,bd=4,wrap=WORD)
        B.place(x=2,y=30,width=390,height=180)
        B.insert(END,encrypt)

    elif(password!="1234"):
        messagebox.showerror("Ooops","Invalid secret key")
    elif(password==""):
        messagebox.showerror("Error","plz enter the secret key")

def decrypt():
    password=code.get()
    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("encryption")
        screen2.geometry("400x250")
        screen2.configure(bg="yellow")
        Message=A.get(1.0,END)
        encode_message=Message.encode("ascii")
        base64_bytes=base64.b64decode(encode_message)
        encrypt=base64_bytes.decode("ascii")
        Label(screen2,text="code is encrypted",font="impack 10 bold").place(x=5,y=6)
        B=Text(screen2,font="30" ,bd=4,wrap=WORD)
        B.place(x=2,y=30,width=390,height=180)
        B.insert(END,encrypt)

    elif(password!="1234"):
        messagebox.showerror("Ooops","Invalid secret key")
    elif(password==""):
        messagebox.showerror("Error","plz enter the secret key")


def reset():
    A.delete(1.0,END)
    code.set("")


       
#Label
Label(screen,text="enter the text for encryption and decryption",font="impack 14 bold",).place(x=5,y=6)
#Text
A=Text(screen,font="20")
A.place(x=5,y=45,width=410,height=120)
#lebel
Label(screen,text="Enter secret key",font="impack 13 bold").place(x=138,y=185)
#entry
code=StringVar()
Entry(textvariable=code,bd=4,font="20").place(x=110,y=220)
#button
Button(screen,text="ENCRYPT",font="arial 15 bold",bg="red",fg="white",command=encrypt).place(x=15,y=280,width=180)
Button(screen,text="DECRYPT",font="arial 15 bold",bg="green",fg="white",command=decrypt).place(x=220,y=280,width=180)
Button(screen,text="RESET",font="arial 15 bold",bg="blue",fg="white",command=reset).place(x=60,y=350,width=280)
mainloop()
