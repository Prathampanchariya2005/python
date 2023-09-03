class Car:
    def _init_(self, make, model, year, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.available = available

class CarRentalService:
    def _init_(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def list_available_cars(self):
        available_cars = [car for car in self.cars if car.available]
        return available_cars

    def rent_car(self, make, model, year):
        for car in self.cars:
            if car.make == make and car.model == model and car.year == year:
                if car.available:
                    car.available = False
                    return f"Successfully rented {year} {make} {model}."
                else:
                    return f"{year} {make} {model} is not available for rent."
        return f"{year} {make} {model} not found in our fleet."

    def return_car(self, make, model, year):
        for car in self.cars:
            if car.make == make and car.model == model and car.year == year:
                if not car.available:
                    car.available = True
                    return f"Successfully returned {year} {make} {model}."
                else:
                    return f"{year} {make} {model} is already available."
        return f"{year} {make} {model} not found in our fleet."

def main():
    rental_service = CarRentalService()

    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("Honda", "Civic", 2021)
    car3 = Car("Ford", "Mustang", 2023)

    rental_service.add_car(car1)
    rental_service.add_car(car2)
    rental_service.add_car(car3)

    while True:
        print("\nCar Rental Service Menu:")
        print("1. List available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            available_cars = rental_service.list_available_cars()
            if available_cars:
                print("\nAvailable Cars:")
                for car in available_cars:
                    print(f"{car.year} {car.make} {car.model}")
            else:
                print("No cars available for rent.")

        elif choice == "2":
            make = input("Enter the make of the car: ")
            model = input("Enter the model of the car: ")
            year = input("Enter the year of the car: ")
            result = rental_service.rent_car(make, model, year)
            print(result)

        elif choice == "3":
            make = input("Enter the make of the car: ")
            model = input("Enter the model of the car: ")
            year = input("Enter the year of the car: ")
            result = rental_service.return_car(make, model, year)
            print(result)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()