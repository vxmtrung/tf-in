import socket,time,os
 
# Server configuration
host = socket.gethostbyname(socket.gethostname())        # Listen on this host
port = 4420             # Main port to listen on
 
d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
d.bind((host, port))
d.listen(1)
s,a = d.accept()
 
f = s.recv(1024)
z = f.decode()
if z.endswith("=EOFX="):
    x = str(z).split()
    e = str(x[1])
    n = str(" ".join(x[2:-1]))
    print("-- Receive file: " + n + " (" + e + ")")
    g = open(n, 'wb')
    while True:
        l = s.recv(1024)
        try: 
            if l.decode().endswith('=EOFX=') == True: break
        except: pass
        g.write(l)
    g.close()
    if e == str(os.path.getsize(n)): print(">> Size verified.")
    else: print("!! Size mismatch.")
    s.close()