from API_Call.Data_Call import Caller
class tester_class(Caller):
    def __init__(self):
        pass

def play_test_V1():
    # name tests
    test_first = tester_class()
    test_second = tester_class()
    test_third = tester_class()
    test_first.get_data("pikachu")
    assert test_first.pokemon_name == "pikachu"
    test_second.get_data("Zygarde-50")
    assert test_second.pokemon_name == "Zygarde" # This should fail
    test_third.get_data("Sliggoo")
    assert test_third.pokemon_name == "sliggoo"

play_test_V1()