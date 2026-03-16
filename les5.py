

class Student:

    def __init__(self, naam, leeftijd):
        self.naam = naam         
        self._leeftijd = leeftijd 

   
    def get_leeftijd(self):
        return self._leeftijd

    
    def set_leeftijd(self, nieuwe_leeftijd):
        if nieuwe_leeftijd < 0:
            print("Leeftijd mag niet negatief zijn!")
            return
        if nieuwe_leeftijd > 130:         
            print("Leeftijd mag niet boven 130 zijn!")
            return
        self._leeftijd = nieuwe_leeftijd

    
    def verjaar(self):
        huidige_leeftijd = self.get_leeftijd()   
        nieuwe_leeftijd = huidige_leeftijd + 1   
        self.set_leeftijd(nieuwe_leeftijd)        


s1 = Student("Ali", 19)

print("=== Basis test ===")
print(s1.get_leeftijd())   

s1.set_leeftijd(20)
print(s1.get_leeftijd())   
s1.set_leeftijd(-5)        
print(s1.get_leeftijd())   

print("\n=== Oefening 1: max 130 ===")
s1.set_leeftijd(131)     
print(s1.get_leeftijd())   

s1.set_leeftijd(130)       
print(s1.get_leeftijd())   

print("\n=== Oefening 2: verjaar() ===")
s2 = Student("Sara", 17)
print(s2.get_leeftijd())   
s2.verjaar()
print(s2.get_leeftijd())   
s2.verjaar()
print(s2.get_leeftijd()) 