class Organism:
    alive = True


class Animal(Organism):
    def eat(self):
        print("THis animal is eating")

    def sleep(self):
        print("This is animal is sleeping")


class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating")

    def sleep(self):
        print("This rabbit is sleeping")


rabbit = Rabbit()

rabbit.eat()
rabbit.sleep()
print(rabbit.alive)


# Method chaining
class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")


car = Car()

car.turn_on() \
    .drive() \
    .brake()