for i in range (5,-1,-1):
    for j in range(i):
        print("* ", end="")

    for k in range(6-i):
        print("# ", end="")
    print()


n = 5
for i in range(1, 6):
    print(" "*(n-i), end="")
    print("* " * i)
