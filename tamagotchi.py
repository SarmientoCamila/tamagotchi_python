class Tamagotchi():
    def __init__(self, name, hunger=100, happiness=100, energy=100, age=0, stage=0):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.age = age
        self.stage = stage

    
    def serialize(self):
        if self.hunger <= 0 or self.energy <= 0:
            return {
                "name": self.name,
                "status": "Murió"
            }
        else:
            return {
                "name": self.name,
                "hunger": self.hunger,
                "happiness": self.happiness,
                "energy": self.energy,
                "age": self.age,
                "stage": self.get_status()  
            }

    def get_status(self):
        if self.age == 0:
            return f"{self.name} es un bebé Tamagotchi."
        elif self.age < 15:
            return f"{self.name} es un niño Tamagotchi."
        elif self.age < 18:
            return f"{self.name} es un adolescente Tamagotchi."
        elif self.age < 20:
            return f"{self.name} es un adulto Tamagotchi."
        else:
            return f"{self.name} es un Tamagotchi anciano y no puede crecer más."
    def feed(self):
        if self.hunger < 100:
            self.hunger += 10
        if self.hunger > 100:
            self.hunger = 100
    def play(self):
        if self.happiness < 100:
            self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
    def sleep(self):
        if self.energy < 100:
            self.energy += 10
        if self.energy > 100:
            self.energy = 100
    def age_up(self):
        if self.age < 20:
            self.age += 1
        if self.age >= 20:
            self.age = 20   
    def is_alive(self):
        return self.hunger > 0 and self.energy > 0
    def die(self):
        self.hunger = 0
        self.energy = 0
        self.happiness = 0
        self.age = 0
        self.stage = 0
        return {
            "name": self.name,
            "status": "Murió"
        }
   