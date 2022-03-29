{% include navigation.html %}

Our Data Structures Project is a health and wellness website. The website has various tools including planners, timers, and other useful applications for students. The goal of the website is to provide useful aid to students and lighten their load of work.

### Week 2
Factorial Code
```
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
```

Factors Code
```
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
```

Fibonacci with Classes Code
```
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
```

### Week 1
InfoDB Code
```
InfoDb = []

InfoDb.append({  
               "FirstName": "Evan",  
               "LastName": "Sanchez",  
               "DOB": "September 28",  
               "Residence": "San Diego",  
               "Email": "evans54795@stu.powayusd.com",  
               "Owns_Cars":["2018 Volt"]  
              })  

InfoDb.append({  
               "FirstName": "Hassan",  
               "LastName": "Allam",  
               "DOB": "May 5",  
               "Residence": "San Diego",  
               "Email": "hassana07646@stu.powayusd.com",  
               "Owns_Cars":["2011 Sonata"]  
              })  

def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"]) 
  
    print("\t", "Cars: ", end="")  
  
    print(", ".join(InfoDb[n]["Owns_Cars"]))  
  
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion

for i in InfoDb:
  print(i)
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  
    print("Recursive loop")
    recursive_loop(0)  
```

Fibonacci Code
```
n = int(input('Type the nth term in the fibonacci sequence: '))

def fibonacci(n):
  a=0
  b=1
  fibList = [0]

  # there are no negative nth terms allowed
  if n <=0:
    print('Input must be greater than 0.')
    fibonacci() # restart the program

  # instead of using logic for the whole sequence, it's       easier to make the 1st term always return 0.
  elif n == 1:
    print(fibList)
    return
  
  else:
    fibList.append(1)
    
    # for loop will go through each number of the sequence      and append them into the list.
    for i in range(2,n):
      c = a + b
      a = b
      b = c
      fibList.append(c)
  print(fibList) # print final result
      
fibonacci(n)
```

### Week 0
Menu Code
```
import swap

main_menu = [
    ["Swap", "swap.py"],
    ["Keypad", "keypad.py"],
    ["Christmas Tree", "xmasTree.py"],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)


def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])

    choice = input("Type your choice> ")

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")

    buildMenu(banner, options)


if __name__ == "__main__":
    menu()
    #menuc()
```
