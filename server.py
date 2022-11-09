import socket
import SHA256


host=socket.gethostname()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=9999
s.bind((host,port))
s.listen(5)

while True:
    cli,addr=s.accept()
    print("connected {}".format(addr))
    op=cli.recv(1).decode('ascii')
    if op=='1':
        username=cli.recv(1024).decode('ascii')
        password=cli.recv(1024).decode('ascii')
        password="".join(list(SHA256.SHA256(password)))
        toapp=username+"-"+password+"\n"
        f=open("hash.txt","a")
        f.write(toapp)
        f.close()
        cli.send(".".encode("ascii"))
        cli.close()
    
    elif op=='2':
        username=cli.recv(1024).decode('ascii')
        password=cli.recv(1024).decode('ascii')
        flag=1
        f=open("hash.txt","r")
        for line in f:
            usepass=line.strip("\n").split("-")
            if(usepass[0]==username):
                f.close()
                flag=0
                if(usepass[1]=="".join(list(SHA256.SHA256(password)))):
                    cli.send("s".encode("ascii"))
                    cli.recv(1).decode("ascii")
                    cli.close()
                else:
                    cli.send("f".encode("ascii"))
                    cli.close()
                break
        if flag:
            cli.send("n".encode("ascii"))
            f.close()
            cli.close()
    