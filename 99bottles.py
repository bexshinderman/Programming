a = input('Enter first num in range: ')
b = input('Enter last num in range: ')
a = int(a)
b = int(b)


for x in reversed(range(a,b+1)):
    #x = int(x)
    print(x, "bottles of weird on the wall ")
    if x == 1:
        print("...and now there's none :( ")
    if x == 0:
        exit()
    
