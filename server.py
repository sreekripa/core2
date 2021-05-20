# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=12345
# s.bind((HOST_NAME,PORT))
# s.listen(4)
# while True:
#     client,address=s.accept()
#     print(address)


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=12345
# s.bind((HOST_NAME,PORT))
# s.listen(4)
# while True:
#     client,address=s.accept()
#     client.send(bytes("hey,how r u , i am doing python ","utf-8"))
#     print(address)


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=12345
# s.bind((HOST_NAME,PORT))
# s.listen(4)
# client,address=s.accept()
# while True:
#     message=input("server:")
#     client.send(bytes(message,"utf=8"))
#     message_from_client=client.recv(50)
#     print("client"+message_from_client.decode("utf=8"))



# import socket
# from tkinter import *
# def send(listbox,entry):
#     message=entry.get()
#     listbox.insert("end",message)
#     entry.delete(0,END)
# root=Tk()
# entry=Entry()
# entry.pack(side=BOTTOM)
# listbox=Listbox(root)
# listbox.pack()
# button=Button(root,text="send",command=lambda :send(listbox,entry))
# button.pack(side=BOTTOM)
# root.mainloop()
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=12345
# s.bind((HOST_NAME,PORT))
# s.listen(4)
# client,address=s.accept()
# while True:
#     message=input("server:")
#     client.send(bytes(message,"utf=8"))
#     message_from_client=client.recv(50)
#     print("client"+message_from_client.decode("utf=8"))


# import socket
# from tkinter import *
# def send(listbox,entry):
#     message=entry.get()
#     listbox.insert("end",message)
#     entry.delete(0,END)
#     client.send(bytes(message, "utf=8"))
#
# def recive(listbox):
#     message_from_client = client.recv(50)
#     listbox.insert('end',message_from_client.decode("utf-8"))
#
# root=Tk()
# entry=Entry()
# entry.pack(side=BOTTOM)
# listbox=Listbox(root)
# listbox.pack()
# button=Button(root,text="send",command=lambda :send(listbox,entry))
# button.pack(side=BOTTOM)
#
# rbutton=Button(root,text="recive",command=lambda :recive(listbox))
# rbutton.pack(side=BOTTOM)
#
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=12345
# s.bind((HOST_NAME,PORT))
# s.listen(4)
# client,address=s.accept()
# root.mainloop()




import socket
from tkinter import *
def send(listbox,entry):
    message=entry.get()
    listbox.insert("end","server:"+message)
    entry.delete(0,END)
    client.send(bytes(message, "utf=8"))

def recive(listbox):
    message_from_client = client.recv(50)
    listbox.insert("end","client:"+message_from_client.decode("utf-8"))

root=Tk()
entry=Entry()
entry.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()
button=Button(root,text="send",command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)

rbutton=Button(root,text="recive",command=lambda :recive(listbox))
rbutton.pack(side=BOTTOM)

root.title("SERVER")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.bind((HOST_NAME,PORT))
s.listen(4)
client,address=s.accept()
root.mainloop()