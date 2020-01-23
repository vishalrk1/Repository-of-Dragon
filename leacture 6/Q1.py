import random
k=[2,3,4,5,6]
w="Hello word"
print(random.seed(9001))
print("Random number of k:",random.choice(k))
print("Random number between 20 to 40: ",random.randrange(20,40))
print(random.uniform(2,10))