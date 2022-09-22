# LAB 1 - THE PAINT SHOP
# Code a Python program that calculates the amount of paint you need to cover the walls in your family room. 
# The salesperson at the home improvement store told you to buy 1 gallon of paint for every 150 square feet of 
# wall you need to paint.

# Assuming that the room is rectangular in shape, the program should take in as input the width of your 
# two sets of walls and the height of the room.

# The program should output the number of gallons required to paint the room. 
# Paint is sold only by the gallon.

#Purpose/Concepts: Input and output to screen, string concatentation, datatype casting, simple math operations

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    print("Welcome to Bryan's Paint Shop!")
    print("At BPS, we're here to help you calculate all your painting needs!")
    print("One gallon of paint costs $14.99. Our prices are the cheapest around!")
    print("Please enter the size of your flooring in square feet")

    finalGallon = 0.00

    floorInput = input("How many square feet is your floor? *Note* Must follow pattern of: 150, 300, 450, 600, 750, etc)")
    wallInput = input("How many square feet is ONE of your walls? *Note* Must follow pattern of: 150, 300, 450, 600, 750, etc)")

    floorGallon =int(floorInput) /150
    wallGallon =int(wallInput) /150 * 2

    trueGallon = int(floorGallon + wallGallon)

    FinalGallon = trueGallon

    print("You have purchased:")
    print(FinalGallon, "Gallons of Paint")
 
    TrueTotal = float(FinalGallon * 14.99)
    print("Your total is:")
    print("$", TrueTotal)
    print("Thank you for shopping at Bryan's Paint Shop! We hope to see you again :)")
main()