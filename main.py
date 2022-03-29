import menuy 

main_menu = [
  ["Swap", "weeklyChallenges/week0/swap.py"], 
  ["Christmas Tree", "weeklyChallenges/week0/xmasTree.py"],
  ["Fibonacci", "weeklyChallenges/week1/fibonacci.py"],
  ["InfoDb", "weeklyChallenges/week1/infoDB.py"],
  ["Fibonacci w/ Class", "weeklyChallenges/week2/fibonacciClass.py"],
  ["Factorial", "weeklyChallenges/week2/factorial.py"],
  ["Factors", "weeklyChallenges/week2/factors.py"]
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menuy.menu(title, menu_list)
  

if __name__ == "__main__":
    menu()