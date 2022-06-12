
sum1 = sum2 = total = count1 = count = n = 0


m = input('Enter card number')
n = int(m)
x = n
y = n
z = n

while (x >= 100):
    x //= 10

print("First two digits are")
print(x)

if x == 34 or x == 37:
    print("AMEX")

elif x > 50 and x < 56:
    print("MASTERCARD")

elif x > 39 and x < 50:
    print("VISA")

else:
    print("INVALID")



while( y != 0 ):

    y = y // 10
    count += 1
print(count)

if count == 13 or count == 16 or count == 15:

    print("valid number lenght")

else:
    print("invalid lenght")

while True:
    mod1 = z % 10
    z = (z // 10)
    sum1 = sum1 + mod1
    

    mod2 = z % 10
    z = z // 10

    mod2 = mod2 * 2
    
    d1 = mod2 % 10
    d2 = mod2 // 10
    sum2 = sum2 + d1 + d2
    
    if (z > 0):
        break
    total = sum1 + sum2
        
    print(total)
if(total % 10 != 0):
    print("You put invalid card number")
else:
    print("Valid Card Number")
