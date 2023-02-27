# Pokemon Class
class Pokemon:
    def __init__(self, count: int, name: str, stats: list, types: list, weaknesses: list, evol: list, movesets: list):
        self.count, self.name, self.stats, self.types, self.weaknesses, self.evol, self.movesets = count,name, stats, types, weaknesses, evol, movesets


class Player:
    def __init__(self, name: str):
        self.chargesLeft = 3  # Charges Left
        self.name = name  # Player's username
        self.pokemons = []
        self.startIndex = 0

    def getPokemonCount(self):
        return ['1st', '2nd', '3rd'][self.startIndex]
