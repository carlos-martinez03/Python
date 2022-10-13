1  # Program make a simple calculator


class Calculate:
    x, y = 0, 0

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        Calcular = Calculate(num1, num2)

        if choice == "1":
            print(num1, "+", num2, "=", Calcular.add())

        elif choice == "2":
            print(num1, "-", num2, "=", Calcular.subtract())

        elif choice == "3":
            print(num1, "*", num2, "=", Calcular.multiply())

        elif choice == "4":
            print(num1, "/", num2, "=", Calcular.divide())
        break
    else:
        print("Invalid Input")
