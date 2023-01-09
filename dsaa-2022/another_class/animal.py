class Animal:
    def __init__ (self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("hihihihi") # 구현되지 않은 코드에 의도적으로 오류를 발생

class Cat(Animal):
    def talk(self):
        print( "Meow!")

class Dog(Animal):
    def talk(self):
        return "Woof!"

animals = [Cat('black'), Cat('white'),Dog("yellow")]
for animal in animals:
    animal.talk()

