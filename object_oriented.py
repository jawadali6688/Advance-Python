class Car:
    total_cars = 0
    
    def __init__ (self, model, brand):
        self.model = model
        self.__brand = brand
        Car.total_cars += 1
    
    def add_bettery(self):
         return f"You have added a new bettery in {self.__brand} {self.model}"
     
    def full_Name(self):
        return f"Your Car is {self.__brand} and Model is {self.model} "
    
    def get_brand(self):
        return f"Brand is {self.__brand}!!"
    
    def fuel_type(self):
        return f"Fuel Types is Petrol Or Diesel!!"
    @property
    def model1(self):
        return f"{self.model}"
    @staticmethod
    def general_description():
        return f"Cars are means of Transport!!"
    
    
 
class ElectricCar(Car):
    def __init__ (self, model, __brand, bettery):
        super().__init__(model, __brand)        
        self.bettery = bettery 
    
    def change_bettery(self):
        return f"Successfully changed bettery of {self.__brand}"
    
      
    def fuel_type(self):
        return f"Electric Charge!!" 

class SolarCar(Car):
    def __init__(self, brand, model, solar_type):
        super().__init__(brand, model)
        self.solar_type = solar_type
    
    def solar_check(self):
        return f"Solar type is {self.solar_type}"   
new_car = Car("2020", "Tesla")
extra_new_car = Car("2022", "Tesla")
# print(new_car.model, new_car.brand)
# print(new_car.add_bettery())


# print(extra_new_car.add_bettery())
# print(extra_new_car.full_Name())

tesla_car = ElectricCar("5040", "Tesla", "20kwh")
tesla_car1 = ElectricCar("5040", "Tesla", "20kwh")

# print(tesla_car.full_Name())
# print(tesla_car.bettery)
# print(tesla_car.change_bettery())
# print(new_car.full_Name())

# print(new_car.get_brand())
# print(new_car.__brand)
# print(new_car.fuel_type())
# print(tesla_car.fuel_type())
# print(Car.total_cars)
# print(Car.general_description())
# print(new_car.model1)
# print(isinstance(new_car, Car))
# print(isinstance(tesla_car, ElectricCar))
# print(isinstance(extra_new_car, Car))
# print(isinstance(tesla_car1, Car))

new_solar_car = SolarCar("Tesla", "2024", "200 WAT Solar Type")
print(new_solar_car.add_bettery())

