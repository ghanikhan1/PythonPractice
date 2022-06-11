
while True:
    
    m = input("Change owed : " )
    n = float(m)
    if n > 0:
        break
n = n*100
print(n)
n = round(n)
print(n)
coins = 0

while (n >= 25):
    n = n-25
    coins = coins+1

while(n >= 10):
    n = n-10
    coins += 1
    
while(n >= 5):
    n = n-5
    coins += 1
    
while(n >= 1):
    n = n-1
    coins += 1
    
print('Total coins used', coins)    