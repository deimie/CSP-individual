class factorial:

    def __call__(self, n):
        f = 1
        for i in range(1, n + 1): # for loop will take number of iterations and multiply each term that many times
            f = f * i
        return f #returns output


n = int(input("Enter a number:")) # defines n as user input

obj = factorial()
f = obj.__call__(n) # 
print("Factorial is:", f) #prints output