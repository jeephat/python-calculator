class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for _ in range(abs(b)):
            result = self.add(result, a)
        if b < 0:
            result = -result
        return result


    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result = self.add(result, 1)
        return result

    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Modulo by zero is not allowed.")
        while a >= b:
            a = self.subtract(a, b)
        while a < 0:  # Handle negative modulo cases
            a = self.add(a, b)
        return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))