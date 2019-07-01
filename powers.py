cap = input("Enter a number: ")
capnum = int(cap)
mult = input("Enter a multiple: ")
multiple =  int(mult)
i = 0;
foo = 0;
while foo<capnum:
    print(foo) #by changing foo to i we can list the ith power, or by using foo we can list the powers up until our cap.
    foo = multiple**i
    i+= 1
    
