class Pokemon:

    def __init__(self, name, level, element, max_hp, curr_hp):
        self.name = name
        self.level = level
        self.element = element
        self.max_hp = max_hp
        self.curr_hp = curr_hp
        self.is_knocked_out = False

    def lose_health(self, hp_loss):
        self.curr_hp -= hp_loss
        print(f"{self.name} took {hp_loss} damage.")
        if self.curr_hp < 0:
            self.curr_hp = 0
            self.knocked_out()

    def gain_health(self, hp_gained):
        self.curr_hp += hp_gained
        print(f"{self.name} gained {hp_gained} HP.")
        if self.curr_hp > self.max_hp:
            self.curr_hp = self.max_hp

    def knocked_out(self):
        self.is_knocked_out = True
        print(f"{self.name} is K.O.")

    def revive(self):
        self.is_knocked_out = False
        print(f"{self.name} was revived.")
        self.curr_hp = 1

    def attack(self, pokemon):
        if ((pokemon.element == "Fire") & (self.element == "Grass")) | ((pokemon.element == "Water") & (self.element == "Fire")) | ((pokemon.element == "Grass") & (self.element == "Water")):
            print(f"{self.name} attacked {pokemon.name}. It is super effective!")
            pokemon.lose_health(self.level // 2)
        elif ((pokemon.element == "Fire") & (self.element == "Water")) | ((pokemon.element == "Water") & (self.element == "Grass")) | ((pokemon.element == "Grass") & (self.element == "Fire")):
            print(f"{self.name} attacked {pokemon.name}. It's not really effective...")
            pokemon.lose_health(self.level * 2)
        else:
            pokemon.lose_health(self.level)


