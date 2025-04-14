from superhero import Superhero, FlyingHero
from vehicles import Car, Plane, Boat

print("-- Superheroes --")
hero = Superhero("IronMan", "Advanced Tech", "Marvel")
hero.display_info()
hero.use_power()

flyer = FlyingHero("Superman", "Flight", "DC", 3000)
flyer.display_info()
flyer.use_power()
print("Flight Speed:", flyer.get_flight_speed())

print("\n-- Vehicles in Action --")
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()