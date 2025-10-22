str = "hello"
visited = ""

for i in str:
    if i not in visited:
        count = 0
        for j in str:
            if j == i:
                count += 1
        print(f"{i} : {count}")
        visited += i
