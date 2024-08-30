drive = ""     # \\\\.\\C:
fileD = open(drive, "rb")
size = 512              # Size of bytes to read
byte = fileD.read(size) 
offs = 0                # Offset location
drec = False            # Recovery mode
count = 0                # Recovered file ID
try:
    while byte:
        found = byte.find(b'') #Input file signature
        if found >= 0:
            drec = True
            print('------ Found Item at location: ' + str(hex(found+(size*offs))) + ' ------')
            fileN = open(str(count) + '.[extention _file]', "wb")
            fileN.write(byte[found:])
            while drec:
                byte = fileD.read(size)
                bfind = byte.find(b'\xff\xd9')
                if bfind >= 0:
                    fileN.write(byte[:bfind+2])
                    fileD.seek((offs+1)*size)
                    drec = False
                    count += 1
                    fileN.close()
                else: fileN.write(byte)
        byte = fileD.read(size)
        offs += 1
except:
    print("Error")

print("Finish")
fileD.close()