def fw(sp : str):
    x = int(0)
    y = int(0)
    sp = sp + " "
    while(sp!=""):
        x = sp.find(" ")
        y +=1
        sp = sp[x+1:]
    print(y)

if __name__ == "__main__":
   fw("Eat bananas regularly")


