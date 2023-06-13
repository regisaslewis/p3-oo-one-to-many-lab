class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self._owner = owner
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        Pet.all.append(self)
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise Exception
        self._owner = value

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [n for n in Pet.all if n.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        pet.owner = self

    ## The instructions ask for the method to be sort_pets_by_name(self), but the tests asks for get_sorted_pets(self)
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key= lambda n: n.name)