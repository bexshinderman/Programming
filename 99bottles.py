a = input('Enter first num in range: ')
b = input('Enter last num in range: ')

for x in reversed(range(a,101)):
 
    print(str(x)+" bottles of weird on the wall ")
    if x == 1:
        print("...and now there's none :( ")
    
