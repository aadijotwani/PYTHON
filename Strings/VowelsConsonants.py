str = input("Please enter a String: ")

count = 0
for i in str:
    # if(i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'a' or i == 'i' or i == 'o' or i == 'u'):
    #     count += 1
    if i in 'AEIOUaeiou':
        count +=1


print("Vowels = ", count)