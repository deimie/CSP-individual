{% include navigation.html %}

# Tech Talk 2

## Weeks

{% include techtalks.html %}

### Factorial Code

````
class factorial:

    def __call__(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


n = int(input("Enter a number:"))

obj = factorial()
f = obj.__call__(n)
print("Factorial is:", f)
````

### Factors Code

````
def factors():
  num = int(input("Enter any Number to find its factors: "))
  findFactors(num)

def findFactors(number):
  print("Factors of a Given Number {0} are:".format(number))
  
  for value in range(1, number + 1):
    if number % value == 0:
            print("{0}".format(value), end=" ")
  print()

factors()
````

### Fibonacci with Classes Code

````
class fibonacci:
  def __init__(self):
    self.fiboSeq = [0, 1]
    
  def __call__(self, n):
    if n < len(self.fiboSeq):
      return self.fiboSeq[n]
    else:
      # Compute the requested Fibonacci number
      fib_number = self(n - 1) + self(n - 2) 

      #Builds List
      self.fiboSeq.append(fib_number) 
      return self.fiboSeq[n]


n = int(input('Type the nth term in the fibonacci sequence: '))
fibonacci_of = fibonacci()
#Prints nth term that user inputed
print(fibonacci_of(n))
````
