f=open("C:\Users\djami\PycharmProjects\DavidScheduler\DObject","r+")
f_out=open("C:\Users\djami\PycharmProjects\DavidScheduler\DObject","w+")
for line in f:
    tokens=line.split(' ')
    f_out.write(("wordcount:" +str(len)(tokens)) +line)

f.close()
f_out.close()