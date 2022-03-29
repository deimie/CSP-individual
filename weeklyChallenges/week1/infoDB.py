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