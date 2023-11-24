import socket,time,os,sys
PORT = 4420
if len(sys.argv) > 2:
    host = str(sys.argv[1])
    file = str(' '.join(sys.argv[2:]))
else: 
    print("> Usage: filesend.py host file")
    sys.exit()
 
# Configure socket connection
z = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
z.connect((host, PORT))
 
flen = str(os.path.getsize(file))
fstr = 'FILE: ' + flen + ' ' + os.path.basename(file) + ' =EOFX='
print("- Send file: " + file + " (" + flen + ")")
z.send(fstr.encode())
time.sleep(1)
try:
    with open(file, 'rb') as f:
        fileData = f.read()
        # Begin sending file
        z.sendall(fileData)
        time.sleep(4)
        z.send('=EOFX='.encode())
    f.close()
    print('>> Transfer: ' + file + ' complete.\n')
except:
    print('> Error sending file: ' + file + '.\n')