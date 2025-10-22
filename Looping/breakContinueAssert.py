for i in range(12):
    print("2 x ", i, " = ", 2*i)
    if(i==10):
        break

print("\n\n")

for i in range(12):
    if(i==10):
        print("OOPS error")
        continue
    
    print("3 x ", i, " = ", 3*i)


k=5
assert k<4, "errordfgfdhfgf"
print("Program continues...")
