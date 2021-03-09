import pokemon


class Trainer:

    def __init__(self, name, pokemon_list, active_pokemon, num_potion):
        self.name = name
        self.pokemon_list = pokemon_list
        self.active_pokemon = active_pokemon  # index of the pokemon_list
        self.num_potion = num_potion

    def switch_active_pokemon(self, pokemon_index):
        if (pokemon_index <= len(self.pokemon_list) - 1) and pokemon_index >= 0:
            print(f"{self.name} switched {self.pokemon_list[self.active_pokemon].name} with {self.pokemon_list[pokemon_index].name}.")
            self.active_pokemon = pokemon_index
        else:
            print("Wrong index input.")

    def use_potion(self):
        if self.num_potion > 0:
            print(f"{self.name} used a potion on {self.pokemon_list[self.active_pokemon].pokemon.name}!")
            self.pokemon_list[self.active_pokemon].pokemon.gain_health(50)
            self.num_potion -= 1
        else:
            print(f"{self.name} doesn't have any potion!")

    def attack(self, enemy_trainer):
        print(f"{self.name} wants to attack {enemy_trainer.name}!")
        self.pokemon_list[self.active_pokemon].pokemon.attack(enemy_trainer.pokemon_list[enemy_trainer.active_pokemon])
