import art


def add(n1, n2):

    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


def calculator() :
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What's the first number?"))

    while should_accumulate :

        for key in operations :
            print(key)
        pick_op =input("Pick an operation :")
        num2 = float(input("What's the next number?"))
        result = operations[pick_op](num1, num2)
        print(f"{num1} {pick_op} {num2} = {result}")
        choice = input(f"Type 'y' if you want to calculate with {result}, or type 'n' to start a new calculation : ").lower()
        if choice == "y":
            num1 = result
        elif choice == "n":
            should_accumulate = False
            print("\n" * 20 )
            calculator()


calculator()

