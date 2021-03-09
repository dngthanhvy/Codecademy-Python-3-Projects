import pokemon
import trainer


# Pokemon list
charmander = pokemon.Pokemon("Charmie", 47, "Fire", 200)
bulbasaur = pokemon.Pokemon("Bulbie", 48, "Water", 180)
ash_pokemon = [charmander, bulbasaur]

togepi = pokemon.Pokemon("Togepi", 50, "Grass", 230)
staryu = pokemon.Pokemon("Staryu", 47, "Water", 210)
misty_pokemon = [togepi, staryu]

ash = trainer.Trainer("Ash", ash_pokemon, 0, 1)
misty = trainer.Trainer("Misty", misty_pokemon, 1, 2)

