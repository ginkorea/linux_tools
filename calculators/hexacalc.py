import argparse


class HexCalculator:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Hexadecimal Calculator")
        parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"],
                            help="Operation to perform: add, subtract, multiply, divide")
        parser.add_argument("num1", type=str, help="First hexadecimal number")
        parser.add_argument("num2", type=str, help="Second hexadecimal number")
        self.args = parser.parse_args()

    @staticmethod
    def hex_to_decimal(hex_num):
        return int(hex_num, 16)

    @staticmethod
    def decimal_to_hex(decimal_num):
        return hex(decimal_num)

    def add_hex(self):
        decimal_sum = self.hex_to_decimal(self.args.num1) + self.hex_to_decimal(self.args.num2)
        return self.decimal_to_hex(decimal_sum)

    def subtract_hex(self):
        decimal_diff = self.hex_to_decimal(self.args.num1) - self.hex_to_decimal(self.args.num2)
        return self.decimal_to_hex(decimal_diff)

    def multiply_hex(self):
        decimal_product = self.hex_to_decimal(self.args.num1) * self.hex_to_decimal(self.args.num2)
        return self.decimal_to_hex(decimal_product)

    def divide_hex(self):
        decimal_quotient = self.hex_to_decimal(self.args.num1) / self.hex_to_decimal(self.args.num2)
        return self.decimal_to_hex(decimal_quotient)

    def calculate(self):
        if self.args.operation == "add":
            return self.add_hex()
        elif self.args.operation == "subtract":
            return self.subtract_hex()
        elif self.args.operation == "multiply":
            return self.multiply_hex()
        elif self.args.operation == "divide":
            return self.divide_hex()


def main():
    calculator = HexCalculator()
    result = calculator.calculate()
    print("Result in hexadecimal:", result)
    print("Result in decimal:", calculator.hex_to_decimal(result))


if __name__ == "__main__":
    main()
