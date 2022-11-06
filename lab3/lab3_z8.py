

x= int(input("Podaj szerokosc: "))
y= int(input("Podaj długość: "))


for i in range(1,y+1):
    for j in range(1,x+1):
        print("*",end=' ')
    print("\n")