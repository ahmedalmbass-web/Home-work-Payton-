
class Calculator:
    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(base: int, exp: int):
        if exp < 0:
            raise ValueError("Negative exponent is not allowed")
        return base ** exp

    def get_item(self, items: list, index: int):
        if len(items) == 0 or index < 0 or index >= len(items):
            raise IndexError("Index out of range")
        return items[index]

    def get_average(self, numbers: list[int]):
        if len(numbers) == 0:
            raise ValueError("List is empty")
        return sum(numbers) / len(numbers)


if __name__ == "__main__":
    calc = Calculator()

    try:
        print(calc.div(10, 0))
    except Exception as e:
        print(e)

    try:
        print(Calculator.power(2, -1))
    except Exception as e:
        print(e)

    try:
        print(calc.get_item([10, 20, 30], 5))
    except Exception as e:
        print(e)

    try:
        print(calc.get_average([]))
    except Exception as e:
        print(e)
