import threading

#input passwords to be hashed from users
passwd=list(map(str ,raw_input("Enter passwords to be hashed").split()))

#Number of password to be hashed
l=len(passwd)


#list of hashed passwords
hashpasswd=[]


#Coping the passwords to  plain_passwd text file
def plainpasswdtransfer(passwd):
    pp=open("plain_passwd.txt","w")
    for i in range(l):
        pp.write(passwd[i])
        pp.write("  ")
    pp.close()
    print("Passwords transferred to file Successfully")
    p=open("plain_passwd.txt","r")
    f=p.read()
    print "The plain passwd are :",f
    p.close()


# Applying Hashing on passwords
def hashingpasswd(passwd):
    for j in range(l):
        pt=passwd[j]
        ct=""
        for k in pt:
            ascpt=ord(k)
            ascpt=ascpt-15
            chrpt=chr(ascpt)
            ct=ct+chrpt
        #add hashed text to hashpasswd list
        hashpasswd.append(ct)


#Copying hashed passwords to hash_passwd.txt
def copyhashtxt(hasharray):
    hashfile=open("hash_passwd.txt","w")
    for i in range(len(hasharray)):
        hashfile.write(hasharray[i])
        hashfile.write("  ")
    hashfile.close()
    print "Hashed passwords transferred Successfully to file"
    hashfile=open("hash_passwd.txt","r")
    hr=hashfile.read()
    print "contents of hash file are : ",hr
    hashfile.close()

# Main function of program

#thread controlling transfer of passwords to plaintext file
t1=threading.Thread(target=plainpasswdtransfer , args=(passwd,))

#thread controlling hashing of received passwords
t2=threading.Thread(target=hashingpasswd , args=(passwd,))

#thread controlling transfer of hashed passwords to hash file
t3=threading.Thread(target=copyhashtxt , args=(hashpasswd,))

t1.start()
print "Thread 1 started Successfully"

t2.start()
print "Thread 2 started Successfully"
t2.join()
print "Thread 2 executed Successfully"

t3.start()
print "Thread 3 started Successfully"
t1.join()
print "Thread 1 executed Successfully"

t3.join()
print "Thread 3 executed Successfully"

print "All threads executed Successfully "

'''
Output:

Thread 1 started Successfully
Thread 2 started Successfully
Thread 2 executed Successfully
Thread 3 started Successfully
Passwords transferred to file Successfully
The plain passwd are : maithil  virat  rohit  ms  hardik
Thread 1 executed Successfully
Hashed passwords transferred Successfully to file
contents of hash file are :  ^RZeYZ]  gZcRe  c`YZe  ^d  YRcUZ\
Thread 3 executed Successfully
All threads executed Successfully
'''