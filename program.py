
def fizzbuzz():
    x = 1
    while (x <= 100):
        if(x % 15 == 0):
            print("Fizzbuzz")
        elif(x % 3 == 0):
            print("Fizz")
        elif(x % 5 == 0):
            print("buzz")
        else:
            print(x)   
        x = x+1

 
fizzbuzz()