#%%
class Dog:
    species='Canis familiaris' #class instance
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,sound):
        return f"{self.name} barks {sound}"
#override
class JackRussellTerrier(Dog):
    def speak(self,sound="Arf"):
        return f"{self.name} says {sound}"   
#%%
#inherit
class Bulldog(Dog):
    pass   
# super()
class Duchshund(Dog):
    def speak(self,sound="Yap"):
        return super().speak(sound)   

miles=JackRussellTerrier("Miles",4)
print(miles)
print(miles.speak())
print(miles.speak("Grrr"))
jim=Bulldog('Jim',5)
print(jim)
print(jim.speak("Woof"))
buddy=Duchshund("Buddy",9)
print(buddy)
print(buddy.speak())

