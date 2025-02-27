class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.wheels = 4

    def print_car(self):
        print(f"I am a {self.brand} {self.model}")


def main():
    supra = Car("Toyota", "Supra")
    supra.print_car()
    lamborghini = Car("lamborghini", "urus")
    lamborghini.print_car()

if __name__ == '__main__':
    main()