def order_word(s):
    
    if s == "":
        print("Invalid String!")
    else:
        ordered_str = ""
        li = list(s)
        length = len(li)

        for i in range(0, length):
            for j in range(i+1, length):
                if ord(li[i]) > ord(li[j]):
                    li[i], li[j] = li[j], li[i]

        for i in range(length):
            ordered_str += li[i]

        print(ordered_str)

if __name__ == "__main__":
    str = str(input("Enter a string > "))
    order_word(str)