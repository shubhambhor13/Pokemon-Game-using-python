pokemon_data = [ 
    {"name": "Charizard", "HP": 78, "attack": 84, "defense": 78, "special_attack": 109, "special_defense": 85, "type": "Fire", "level": 36, "move_power": 90},
    {"name": "Blastoise", "HP": 79, "attack": 83, "defense": 100, "special_attack": 85, "special_defense": 105, "type": "Water", "level": 36, "move_power": 85},
    {"name": "Venusaur", "HP": 80, "attack": 82, "defense": 83, "special_attack": 100, "special_defense": 100, "type": "Grass", "level": 36, "move_power": 80},
    {'name': 'Gengar', 'HP': 120,'attack': 65,'defense': 60,'special_attack': 130,'special_defense': 75,'type': 'Ghost','level':36, 'move_power': 100  },
    {'name': 'Dragonite','HP': 182,'attack': 134,'defense': 95,'special_attack': 100,'special_defense': 100,'type': 'Dragon','level':38, 'move_power': 120 },
    {'name': 'Snorlax','HP': 200,'attack': 110,'defense': 65,'special_attack': 65,'special_defense': 110,'type': 'Normal','level':45, 'move_power': 150 },
    {'name': 'Alakazam','HP': 110,'attack': 50,'defense': 45,'special_attack': 135,'special_defense': 95,'type': 'Psychic','level':40, 'move_power': 90 }
]

def calculate_damage (level,attack,move_power,defense):
    damage = (((2 * level / 5 + 2)) * attack * move_power / defense) / 50 + 2
    return damage

def adjust_for_type_effectiveness(attacker_type, defender_type, damage):
    effectiveness_chart = {
         ("Fire", "Grass"): 2.0, ("Fire", "Water"): 0.5,("Fire", "Dragon"): 0.5,
         ("Water", "Fire"): 2.0, ("Water", "Grass"): 0.5, ("Water", "Dragon"): 0.5, 
         ("Grass", "Fire"): 0.5, ("Grass", "Water"): 2.0, ("Grass", "Dragon"): 1.0, ("Grass", "Poison"): 0.5,
         ("Poison", "Grass"): 2.0, ("Poison", "Fire"): 1.0, ("Poison", "Water"): 1.0,("Poison", "Ghost"): 1.0,
         ("Psychic", "Fire"): 1.0, ("Psychic", "Water"): 1.0, ("Psychic", "Grass"): 1.0, ("Psychic", "Ghost"): 2.0,
         ("Ghost", "Normal"): 0.0, ("Normal", "Ghost"): 0.0, ("Ghost", "Psychic"): 2.0, ("Psychic", "Ghost"): 1.0,
    }
    effectiveness = effectiveness_chart.get((attacker_type, defender_type), 1.0)
    return int(damage * effectiveness), effectiveness

def battle(pokemon1,pokemon2):
    print(f"\nBattle between {pokemon1['name']} and {pokemon2['name']} begins!")

    while pokemon1['HP']>0 and pokemon2['HP']>0:
        
        damage = calculate_damage(pokemon1['level'], pokemon1['attack'], pokemon1['move_power'], pokemon2['defense'])
        damage, effectiveness = adjust_for_type_effectiveness(pokemon1['type'], pokemon2['type'], damage)
        pokemon2['HP'] -= damage
        print(f"{pokemon1['name']} attacks {pokemon2['name']} dealing {damage} damage (effectiveness: {effectiveness}).")
        print(f"{pokemon2['name']} has {max(0, pokemon2['HP'])} HP left.\n")
        if pokemon2['HP'] <= 0:
            print(f"{pokemon2['name']} has fainted! {pokemon1['name']} wins!")
            return pokemon1['name']
        
        
        damage = calculate_damage(pokemon2['level'], pokemon2['attack'], pokemon2['move_power'], pokemon1['defense'])
        damage, effectiveness = adjust_for_type_effectiveness(pokemon2['type'], pokemon1['type'], damage)
        pokemon1['HP'] -= damage
        print(f"{pokemon2['name']} attacks {pokemon1['name']} dealing {damage} damage (effectiveness: {effectiveness}).")
        print(f"{pokemon1['name']} has {max(0, pokemon1['HP'])} HP left.\n")
        if pokemon1['HP'] <= 0:
            print(f"{pokemon1['name']} has fainted! {pokemon2['name']} wins!")
            return pokemon2['name']
        
def display_menu():
    print("\nPokémon Battle Simulator")
    print("1. Start Battle")
    print("2. Exit")

while True:
        display_menu()
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            if len(pokemon_data) < 2:
                print("You need at least two Pokémon to start a battle!")
            else:
                
                print("\nAvailable Pokémon:")
                for i, pokemon in enumerate(pokemon_data):
                    print(f"{i + 1}. {pokemon['name']} (Type: {pokemon['type']}, HP: {pokemon['HP']})")

                
                p1_index = int(input("\nSelect the first Pokémon (enter number): ")) - 1
                p2_index = int(input("Select the second Pokémon (enter number): ")) - 1

                if p1_index < 0 or p1_index >= len(pokemon_data) or p2_index < 0 or p2_index >= len(pokemon_data):
                    print("Invalid Pokémon selection.")
                else:
                    
                    pokemon1 = pokemon_data[p1_index].copy()
                    pokemon2 = pokemon_data[p2_index].copy()
                    battle(pokemon1, pokemon2)

        elif choice == '2':
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select 1, 2, or 3.")