name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1,arr2):
    name_favorite_animal = zip(name,favorite_animal)
    print name_favorite_animal
make_dict(name, favorite_animal)