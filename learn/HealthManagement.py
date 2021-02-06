a = int(input("Choose the number from Below the following: \n 1. Harry \n 2. Pranjal \n 3. Monil \n"))

def getdate():
    import datetime
    return datetime.datetime.now()

if a==1:
    f=open("harrye.txt","rt")
    content=f.read()
    print(getdate())
    print(content)
    f.close()
    t=open("harryd.txt","rt")
    creator=t.read()
    print(getdate())
    print(creator)
    t.close()

elif a==2:
    f = open("pranjale.txt","rt")
    content=f.read()
    print(getdate())
    print(content)
    f.close()
    t = open("pranjald.txt","rt")
    creator=t.read()
    print(getdate())
    print(creator)
    t.close()

elif a==3:
    f = open("monile.txt","rt")
    content=f.read()
    print(getdate())
    print(content)
    f.close()
    t = open("monild.txt","rt")
    creator=t.read()
    print(getdate())
    print(creator)
    t.close()

else:
    print("Invalid Choice")
