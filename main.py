import swap

main_menu = [
    ["Swap", "swap.py"],
    ["Keypad", "keypad.py"],
    ["Christmas Tree", "xmasTree.py"],
]

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menuy.menu(title, menu_list)

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

if __name__ == "__main__":
    menu()

