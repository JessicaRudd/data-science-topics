# Inheritence
class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale.")

# Fish class inherits from Animal class
class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    #inheriting a method from parent class and adding to it for the Fish class
    def breath(self):
        super().breath()
        print("doing this underwater")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)