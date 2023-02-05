def poke_go(name, number_of_pokemon = 0):
    if number_of_pokemon == 0:
        return "You have caught no Pokemon, " + name
    elif number_of_pokemon < 5:
        return "You are just starting out, " + name
    elif number_of_pokemon < 250:
        return "You are getting better, " + name
    else:
        return "You are the very best, like no one ever was, " + name

print(poke_go("NewGamer98"))
print(poke_go("PokeMASTER222", number_of_pokemon = 100))
print(poke_go("GaryFOak", 250))
