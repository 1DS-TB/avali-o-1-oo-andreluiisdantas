class Animal():
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som do animal"

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        return f"{self.nome} emite AUAU"

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        return f"{self.nome} emite MIAU"

class Vaca(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        return f"{self.nome} emite MUUU"

class Pato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        return f"{self.nome} emite QUAC QUAC"

def animal_falando(animal):
    print(animal.emitir_som())

Lista = [
    Cachorro("Bob"),
    Vaca("Tia Chica"),
    Pato("Bombado"),
    Gato("Mingau")
]

for animal in Lista:
    animal_falando(animal)