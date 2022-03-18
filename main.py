import menuy 

main_menu = [
  ["Swap", "swap.py"], 
  ["Christmas Tree", "xmasTree.py"]
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menuy.menu(title, menu_list)
  

if __name__ == "__main__":
    menu()