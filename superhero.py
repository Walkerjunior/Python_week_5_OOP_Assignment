class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def display_info(self):
        print(f"{self.name} from {self.universe} uses {self.power}!")

    def use_power(self):
        print(f"{self.name} is using {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, power, universe, flight_speed):
        super().__init__(name, power, universe)
        self.__flight_speed = flight_speed  # Encapsulation

    def use_power(self):
        print(f"{self.name} soars through the skies at {self.__flight_speed} km/h!")

    def get_flight_speed(self):
        return self.__flight_speed