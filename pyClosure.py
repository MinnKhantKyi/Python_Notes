# Closure is a method that is used to input data into a function 
# without using parameter(s) passing

def myFun(n):
    
    def adding(data):
        return data+n
    
    return adding

add10 = myFun(10)
# add10 = myFun(10)
#           def adding(data):
#               return add+10
#           return adding
# Now add10 = adding(data):
#               return data+10

print('')
print('Closure in Python')
print('')

print('add10(5)  by closure     > ',add10(5))
print('')

print('Cell and object address -> ',add10.__closure__)
print('Data in add10           -> ',add10.__closure__[0].cell_contents)
print('')