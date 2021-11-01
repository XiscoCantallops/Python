import getch

while True:
    char = getch.getch() # User input, but not displayed on the screen
    # or     char = getch.getche() # also displayed on the screen
    print(char)
