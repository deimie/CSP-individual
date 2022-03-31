import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
LAND_COLOR = u"\u001b[44m\u001B[2D"
BUNNY_COLOR = u"\u001b[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n\n\n\n")
    print(LAND_COLOR + "  " * 25)

# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(BUNNY_COLOR + sp + "              _    ")
    print(sp + "  __   ___.--'_`.  ")
    print(sp + " ( _`.'. -   'o` ) ")
    print(sp + " _\.'_'      _.-'  ")
    print(sp + "( \`. )    //\`    ")
    print(sp + " \_`-'`---'\\__,   ")
    print(sp + "  \`        `-\    ")
    print(RESET_COLOR)

# ship function, iterface into this file
def ship():
  ocean_print()
  # loop control variables
  start = 0  # start at zero
  distance = 35  # how many times to repeat
  step = 2  # count by 2

  # loop purpose is to animate ship sailing
  for position in range(start, distance, step):
      ship_print(position)  # call to function with parameter
      time.sleep(.1)
