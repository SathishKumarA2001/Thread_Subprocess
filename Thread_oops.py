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
            conn.close()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost",3074))
sock.listen()
print("listening...")
while True:
    conn,addr = sock.accept()
    Thread_Start(conn,addr)
    print("started...",addr[0])

sock.close()