{% include navigation.html %}

Our Data Structures Project is a health and wellness website. The website has various tools including planners, timers, and other useful applications for students. The goal of the website is to provide useful aid to students and lighten their load of work.

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
