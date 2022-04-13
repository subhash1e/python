gc = 0
gl = 3
secret = 5

while gc < gl:
    g = int(input("guess: "))
    gc+=1
    if(g == secret):
        print('You won')
        break
else:
    print("Game Over")
