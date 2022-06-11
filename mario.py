
while True:
    m = input("Height")
    n = int(m)
    if n >= 1 and n <= 8:
        break
for i in range(n):
    for j in range(n):
        if i + j >= n-1:
            print("#",end="")
        else:
            print(" ",end="")

    print()

