a = int(input("jugdor a"))
b = int(input("jugador b"))

if (a and b) <= 7 :
    
    if a == 6 and (a-b) == 2:
        print("gana a")
    if b == 6 and (b-a) == 2:
        print("gana a")   
    if a == 7 and b < 5 :
        print("invalido")
    if b == 7 and a < 5 :
        print("invalido")
    
    if a == 7 and (a - b) == 1:
        print ("gana a")
    if b == 7 and (b - a) == 1 :
        print ("gana b")
    
    if a == 7 and (a - b) == 2:
        print ("gana a")
    if b == 7 and (b - a) == 2 :
        print ("gana b")
    
    
    
    if a == b :
        print("invalido")
    if a < 6 and b < 6:
        print("no ha terminado")
    if a == 6 and (a - b) == 1:
        print("no ha terminado")
    if b == 6 and (b - a) == 1:
        print("no ha terminado")

else:    
    print ("Invalido")
    