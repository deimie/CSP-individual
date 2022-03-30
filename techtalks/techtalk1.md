{% include navigation.html %}

# Tech Talk 1

## Weeks

{% include techtalks.html %}

### InfoDB Code

````
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
````

### Fibonacci Code

````
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
````
