class Animal:
    alive = True

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