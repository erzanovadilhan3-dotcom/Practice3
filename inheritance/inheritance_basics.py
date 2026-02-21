class animal():
    def __init__(self,name,voice):
        self.name=name
        self.voice=voice
class fish(animal):
    pass
kitty=fish("Lara", "meow")
print(kitty.name)