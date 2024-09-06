#Author: Paige Bates
#Date Written: 09/06/2024
#Create a Python app that has a super class called Vechicle and a class called Automobile. 

class Vechicle:
    def __init__ (self, vechicle_type):
        self.vechicle_type = vechicle_type
class Automobile(Vechicle):
    def __init__(self, vechicle_type, year, make, model, doors, roof):
        super().__init__(vechicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    vechicle_type = input("Enter Type:")
    year = input("Enter year:")
    make = input("Enter make:")
    model = input("Enter model:")
    doors = input("Enter 2 or 4 doors:")
    roof = input("Enter solid or sun roof:")
    
    car = Automobile(vechicle_type, year, make, model, doors, roof)
    print(f"Type: {car.vechicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Doors: {car.doors}")
    print (f"Roof: {car.roof}")
if __name__ == "__main__":
    main()

