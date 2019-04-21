# Module 2
#   Programming Assignment 2
#     Prob-2.py

# Jonathan Ciarlo

# Follow the steps below. Add your code in the blank line after each comment

# define the main function with no parameters
def main():
    # create a variable and assign it the value returned by an input function
    # that asks the user for a number. Don't forget to use the int() function.
    x = int(input("Enter a number: "))
    # print out a message that says: "The sqare of ? is ?" where the question
    # marks are replaced with the value read in from the user and its square.
    print("The square of", (x), "is", (x * x))
    # copy your input statement from above and replace "int" with "float"
    x = float(input("Enter a number: "))
    # copy the print statment from above
    print("The square of", (x), "is", (x * x))
    # copy your input statement from above and replace "int" with "eval"
    x = eval(input("Enter a number: "))
    # copy the print statment from above
    print("The square of", (x), "is", (x * x))
# call the function main
main()