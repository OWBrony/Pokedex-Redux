import requests
import json
from Constants import *

class Caller():
    def __init__(self):
        # Pokemon name
        self.pokemon_name = ""
        # Pokemon abilities
        self.first_ability = ""
        self.second_ability = ""
        self.hidden_ability = ""
        # Pokemon stats
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.spec_attack = 0
        self.spec_defense = 0
        self.speed = 0
        # The base stat total 
        self.stat_total = (self.health + self.attack + self.defense +
        self.spec_attack + self.spec_defense + self.speed)
        # This will hold the sprite to display
        self.sprite = None

    def _find_special_mon(self,name):
        """This is to change pokemon names that have special characters
        into the correct format to search for."""
        if name == "farfetch'd":
            return "farfetchd"
        elif name == "mr. mime" or name == "mr.mime" or name == "mr mime":
            return "mr-mime"
        elif name == "nidoran f" or name == "nidoran ♀" or name == "nidoran♀" or name == "nidoran female":
            return "nidoran-f"
        elif name == "nidoran m" or name == "nidoran ♂" or name == "nidoran♂" or name == "nidoran male":
            return "nidoran-m"

    def _add_suffix(self,name,suffix):
        """This to add regional suffixes to pokemon names."""
        new_name = name + "-" + suffix
        return new_name

    def check_data(self,name,suffix_bool = False,suffix_name = ""):
        """This is to change the given Pokemon's name into
        an appropriate format."""
        if name.lower() in SPECIAL_MONS:
            corrected = self._find_special_mon(name.lower())
            if suffix_bool == True:
                corrected = self._add_suffix(corrected,suffix_name)
            return corrected
        else:
            if suffix_bool == True:
                final = self._add_suffix(name.lower,suffix_name)
                return final
            else:
                return name.lower()

    def get_data(self, name):
        """This is to get the data for the pokemon the user wants.
        The user will either search or click on a pokemon.
        The function sould get a pokemon name passed in."""
        pokemon = name
        # check_data should correct the name of a pokemon that is passed in.
        # either dealing with names with special characters and/or lowering
        # the case of the name so it can be passed to the API.
        corrected = self.check_data(pokemon)
        response_API = requests.get(f"{BASE_URL}{corrected}")
        if not response_API:
            return
        else:
            data = response_API.json()
            # set the pokemon's data
            self.set_info(pokemon, data)
            return data
    
    def set_info(self, name, data):
        """This is to set all the info for the pokemon"""
        self.pokemon_name = name
        # check how many abilities the pokemon has.
        self.first_ability = data["abilities"][0]["ability"]["name"]
        if data["abilities"][1]["is_hidden"] == False:
            self.second_ability = data["abilities"][1]["ability"]["name"]
            self.hidden_ability = data["abilities"][2]["ability"]["name"]
        elif data["abilities"][1]["is_hidden"] == True:
            self.hidden_ability = data["abilities"][1]["ability"]["name"]
            self.second_ability = None
        # set the Pokemon stats
        self.sprite = data["sprites"]["front_default"]
        self.health = data["stats"][0]["base_stat"]
        self.attack = data["stats"][1]["base_stat"]
        self.defense = data["stats"][2]["base_stat"]
        self.spec_attack = data["stats"][3]["base_stat"]
        self.spec_defense = data["stats"][4]["base_stat"]
        self.speed = data["stats"][5]["base_stat"]