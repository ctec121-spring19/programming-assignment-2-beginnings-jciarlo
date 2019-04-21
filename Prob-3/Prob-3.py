# Module 2
#   Programming Assignment 2
#     Prob-3.py

# Jonathan Ciarlo

def example():
    print("\nExample Output")

    # print a blank line
    print()

    # create three variables and assign three values in a single statement
    v1, v2, v3 = 21, 12.34, "hello"

    # print the variables
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)


def studentCode():
    # replace <name> with your name
    print("\nJonathan's Output")
    
    # print a blank line
    print()

    # replicate the assignment statement above, but use your own variable
    # names and values
    v1, v2, v3 = 34, 2.34, "hola"
    # print the values of the 3 variables
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)
    # Get 3 values from the user and assign them to the variables defined
    # above. See the page in Canvas on Simulataneous Assignment
    # BONUS POINTS for using the split() method
    
    print()
    
    v1, v2, v3 = input("Enter 3 values sperated by commas: ").split()
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)
    print()

example()
studentCode()

