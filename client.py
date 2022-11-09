import socket

port=9999
hostIp=socket.gethostname()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((hostIp,port))
print("1-Sign Up")
print("2-Log In")
op=input("enter option:")
s.send(op.encode("ascii"))
if op=='1':
    username=input("enter new username:")
    password=input("enter new password:")
    s.send(username.encode("ascii"))
    s.send(password.encode("ascii"))
    con=s.recv(1).decode("ascii")
    if con==".":
        print("you have created an account!")
        print("now log in to access your account")
    s.close
elif op=='2':
    username=input("enter username:")
    password=input("enter password:")
    s.send(username.encode("ascii"))
    s.send(password.encode("ascii"))
    con=s.recv(1).decode("ascii")
    if con=="s":
        print("You have logged in sucessfully!")
        input("press any key to close the connection")
        s.send(".".encode("ascii"))
        s.close
        print("connection closed")
    elif con=="f":
        print("wrong password!!")
        s.close
        print("connection closed")
    elif con=="n":
        print("user name not found!!")
        s.close
        print("connection closed")
    

