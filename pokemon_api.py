import requests as r
import os

pokemons_api = r.get('https://pokeapi.co/api/v2/pokemon/')
if pokemons_api.status_code == 200:
    pokemons_data = pokemons_api.json()
else:
    print('API call unsuccessful, try again!')

#This is where we create each pokemon object within pokemon class
class Pokemon():
    def __init__(self, name, weight, typ, abilities):
        self.name = name
        self.weight = weight
        self.typ = typ
        self.abilities = abilities

#This is where we start to create the pokedex(where all the poke info goes)
#Creating a dictionary for each added, also being able to remove, and show the pokedex



class Pokedex():
    def __init__(self):
        self.pokemon_dict = {}
        self.poke_type_list = {}

    def pre_add(self):
        name_poke = input('which pokemon would you like to add to your pokedex? Enter none if you are done adding.').lower()
        poke_data = r.get(f'https://pokeapi.co/api/v2/pokemon/{name_poke}')
        if poke_data.status_code == 200:
            if name_poke not in self.pokemon_dict.keys():
                self.add_to_dex(poke_data)
                self.add_to_type_dict(poke_data)
            else:
                print(f'\033[0;31mSorry, {name_poke} is already in pokedex!')
        else:
            print('\033[0;31mSorry, that is not a pokemon! Try again:')

    def add_to_dex(self, poke_data):
        poke_data = poke_data.json()
        pokemon = Pokemon(poke_data['name'], poke_data['weight'], [x['type']['name'] for x in poke_data['types']], [x['ability']['name'] for x in poke_data['abilities']])
        self.pokemon_dict[pokemon.name] = pokemon

    def add_to_type_dict(self, poke_data):
        poke_data = poke_data.json()
        pokemon = Pokemon(poke_data['name'], poke_data['weight'], [x['type']['name'] for x in poke_data['types']], [x['ability']['name'] for x in poke_data['abilities']])
        for typ in pokemon.typ:
            if typ in self.poke_type_list.keys():
                self.poke_type_list[typ].append(pokemon)
            else:
                self.poke_type_list[typ] = [pokemon]

    def show_poke(self):
        for name_poke in self.pokemon_dict:
            print(f'{name_poke} --> Weight: {self.pokemon_dict[name_poke].weight}, Types: {self.pokemon_dict[name_poke].typ}, Abilities: {self.pokemon_dict[name_poke].abilities}')

    def remove_poke(self):
        removed = input('\033[0;33mWhich pokemon would you like to remove from the pokedex?').lower()
        if removed in self.pokemon_dict.keys():
            pokemon = self.pokemon_dict[removed]
            for x in pokemon.typ:
                if x in self.poke_type_list.keys():
                    currentlist = self.poke_type_list[x]
                    for y in currentlist:
                        if y.name == pokemon.name:
                            currentlist.remove(y)
            del self.pokemon_dict[removed]
        else:
            print(f'\033[0;31mSorry, {removed} is not in Pokedex! Try again:')


    def find(self):
        typ_response = input('\033[0;33mWhich pokemon type would you like to see? ').lower()
        if typ_response in self.poke_type_list.keys():
            for x in self.poke_type_list[typ_response]:
                print(x.name)
        else:
            print(f'\033[0;31mSorry, {typ_response} either isn\'t a type, or you haven\'t found a pokemon of that type!')




pokedex1 = Pokedex()







while True:
    response = input('\033[0;32m\n\n\nHi Pokemon Master! What would you like to do:'
                     '\033[0;34m\n\tAdd pokemon [add]'
                     '\n\tRemove pokemon [remove]'
                     '\n\tSee all pokemon [pokedex]'
                     '\n\tFind pokemon by type [find] '
                     '\n\tQuit [quit]'
                     '\033[0;35m\n\nPlease select option here:').lower()
    if response == 'add':
        pokedex1.pre_add()
    elif response == 'remove':
        pokedex1.remove_poke()
    elif response == 'pokedex':
        pokedex1.show_poke()
    elif response == 'find':
        pokedex1.find()
    elif response == 'quit':
        quit()
    else:
        input('Please select option from menu! Press enter to go back to main menu:')




