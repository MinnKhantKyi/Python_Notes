def create_phone_number(n):
    length = len(n)
    if length == 10:
        result = "("
        
        for i in range(length):
            if n[i] >= 0 and n[i] <= 9:
                
                if i < 3:
                    result += str(n[i])                    
                
                if i == 3:
                    result += ") " + str(n[i])
                
                if i > 3 and i < 6:
                    result += str(n[i])

                if i == 6:
                    result += "-" + str(n[i])

                if i > 6:
                    result += str(n[i])
                                        
            else:
                print("Numbers in the array must be between 0 and 9.")

        return result
    else:
        print("Size of array must be 10.")


if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9,0]
    result = create_phone_number(list)
    print(result)


# Similar Code in Codewar
# def create_phone_number(n):
#   str1 =  ''.join(str(x) for x in n[0:3])
#   str2 =  ''.join(str(x) for x in n[3:6])
#   str3 =  ''.join(str(x) for x in n[6:10])
#   return '({}) {}-{}'.format(str1, str2, str3)