import cs50

# This program requests input from the user to determine the height of a half 
# pyramid of blocks (represented by "#"s). It will then draw a pyramid of
# the determined height.

def main():
    # The height of the pyramid cannot be less than zero or greater than 23.
    # If so, reprompt the user until conditions are met.
    while True:
        print("Height: ", end="")
        height = cs50.get_int()
        if height>=0 and height <=23:
            break
    
    # This for loop will draw multiple rows "r".
    for row in range(height): #row = 0
        # This for loop will draw the correct items for the left pyramid, either a space or a
        # "#" per column "column" in the designated row.
        for column in range(row, height + row + 1): #column = 0
            if column < height:
                print(" ", end="")
            else:
                print("#", end="")
        print("  ", end="")
        
        # This for loop will draw the correct items for the right pyramid, either a space or a
        # "#" per column "column" in the designated row.
        for column in range(height):
            if column <= row:
                print("#", end="")
        print()
        
if __name__ == "__main__":
    main()