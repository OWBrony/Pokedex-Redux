from API_Call.Data_Call import Caller
import pytest
class tester_class(Caller):
    def __init__(self):
        pass

def play_test_V1():
    # name tests
    test_first = tester_class()
    test_second = tester_class()
    test_third = tester_class()
    test_first.get_data("pikachu")
    try:
        assert test_first.pokemon_name == "pikachu"
        print(f"{test_first.pokemon_name.capitalize()}: Pass")
    except:
        print(f"{test_first.pokemon_name.capitalize()}: Fail")
    test_second.get_data("Zygarde-50")
    try:
        assert test_second.pokemon_name.capitalize() == "Zygarde" # This should fail
        print(f"{test_second.pokemon_name.capitalize()}: Pass")
    except:
        print(f"{test_second.pokemon_name.capitalize()}: Fail")
    test_third.get_data("Sliggoo")
    try:
        assert test_third.pokemon_name == "sliggoo"
        print(f"{test_third.pokemon_name.capitalize()}: Pass")
    except:
        print(f"{test_third.pokemon_name.capitalize()}: Fail")

play_test_V1()