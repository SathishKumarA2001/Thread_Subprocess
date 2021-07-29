from threading import Thread, current_thread
import socket

def Thread_Start(conn,addr):
    p = Process(conn,addr)
    p.start()
    p.join()

class Process(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        conn = conn
        addr = addr
    
    def run(self):
            print("\n",current_thread(),addr[0])
            #presentation layer
            conn.send("Welcome to Programmers show, type what you want to say: \n".encode())
            #print the messages from client using with list 
            stack = []
            while True:
                try:
                    recv = conn.recv(4096)
                    recv = recv.decode()
                    #close the connection if client sends Hex value ctrl+q
                    if recv == '\x11':
                        conn.close()
                except OSError:
                    print("connection closed in this thread {}".format(addr[0]))
                    break

                while True:
                    #It appends the character to stack
                    stack.append(recv)

                    #It prints the stack after client clicks enter
                    if recv == '\r\n':
                        #Convert list to string function  
                        stack_part = stack 
                        def listtostr(stack_part):
                            str = ""
                            for i in stack_part:
                                str+=i
                            return str
                        stack_part = listtostr(stack_part)
                        #Firewall #Don't allow more than 10 characters..
                        if len(stack_part) > 10:
                            print("Machine overloaded by {}...".format(addr[0]))
                            msg = "Don't overload the server"
                            conn.send(msg.encode())
                        else:
                            print(stack_part)
                        stack.clear()
                    break


#session layer
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost",3074))
sock.listen()
print("listening...")
while True:
    conn,addr = sock.accept()
    #New Thread started
    Thread_Start(conn,addr)
    print("started...",addr[0])
    break
sock.close()