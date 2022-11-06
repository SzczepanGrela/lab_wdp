
x=int(input("Podaj wysokość: "))
szerokosc=(2*x)-2
for i in range(1,x+1):
    for j in range(1,szerokosc-i):
        print(" ",end=' ')
    for k in range(1,2*i):
        print("*",end=' ')
    print("\n")