def descending_order(num):
    ordered_num = ""
    li = []
    
    for i in range(len(num)):
        li.append(num[i])

    length = len(li)

    for i in range(0, length):
        for j in range(i+1, length):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]
    
    for i in range(length):
            ordered_num += li[i]

    print(ordered_num)

if __name__ == "__main__":
    num = str(input("Enter a number > "))
    descending_order(num)