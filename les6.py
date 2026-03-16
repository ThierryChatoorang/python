
class Persoon:

    def __init__(self, naam):
        self.naam = naam

    def voorstel(self):
        print(f"Ik ben {self.naam}.")


class Student(Persoon):

    def __init__(self, naam, leeftijd, opleiding):
        super().__init__(naam)          
        self.leeftijd = leeftijd
        self.opleiding = opleiding

    def voorstel(self):                 
        print(f"Ik ben {self.naam}, {self.leeftijd} jaar, opleiding: {self.opleiding}.")


class Docent(Persoon):

    def __init__(self, naam, vak):
        super().__init__(naam)       
        self.vak = vak

    def voorstel(self):                
        print(f"Ik ben {self.naam} en ik geef {self.vak}.")


