import random

cesta = ''
krok = 0
x = 1


while x < 9999:
    krok = random.randint(0, 11)
    x + 1
    if krok == 0 or krok == 5 or krok == 8:
        cesta = cesta +"↑"
    elif krok == 1 or krok == 6 or krok == 9:
        cesta = cesta +"↓"
    elif krok == 2 or krok == 7 or krok == 10:
        cesta = cesta +"→"
    elif krok == 3 or krok == 8 or krok == 11:
        cesta = cesta +"←"
    elif krok == 4:
        x = 10000
        cesta = cesta +"X"
    
print(cesta)

for i in range(2):
    cesta = cesta.replace("→←", "").replace("↓↑", "").replace("→↑←", "↑").replace("←↑→", "↑").replace("→↓←", "↓").replace("←↓→", "↓").replace("↑↓", "").replace("→↑→↓", "→→").replace("←→", "")


print(cesta)
