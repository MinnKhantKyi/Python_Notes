import random

# random() -> return floating point between 0.0 and 1.0
print('random() > ',random.random())
print(' ')

# randint(start,end) -> return integer between start and end
print('randint(start[0],end[10]) > ',random.randint(0,10))
print(' ')

# randrange(start,end,step) -> return integer between start and end by step
print('randrange(start[0],end[20],step[2]) > ',random.randrange(0,20,2))
print(' ')

# sample(population,k) -> population = list,set or tuple,etc. k = count of elements
words = ['P','y','t','h','o','n']
wordsCap = ['Python','Kotlin','Javascript','Php','React.js','Vue.js','C++','C']
print('sample(population,k) > ',random.sample(words,4))
print('sample(population,k) > ',random.sample(wordsCap,2))
print(' ')

# choice(dataSet) -> dataSet = list,set or tuple,etc.
print('choice(dataSet) > ',random.choice(wordsCap))
print(' ')
print('choice(dataSet) > ',random.choices(wordsCap))
print(' ')

# shuffle(dataSet) -> dataSet = list,set or tuple,etc.)
print('Before shuffle > ',words)
print(' ')
random.shuffle(words)
print('After shuffle > ',words)
print(' ')

# seed() -> generate Pseudo Random Number. Default parameter = system current time
random.seed()
print('seed() > ',random.random())
print(' ') 
random.seed(4)
print('seed() > ',random.random())
print(' ')

# uniform(start,end) -> return floating point between start and end
print('uniform(start[0.0],end[10.0]) > ',random.uniform(0.0,10.0))
print(' ')

# triangular(start,end,step) -> return floating point between start and end
print('triangular(start[0.0],end[20.0],step[2.5]) > ',random.triangular(0.0,20.0,2.5))
print(' ')