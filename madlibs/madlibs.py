#beginning of the madlibs game code in python
# get Input
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
gamename = f"MadLibs"
famous_person = input ("Famous Person: ")
print("Welcome to{}".format(gamename))
madlib = f"Computer programming is so {adj}! It makes me so excited all the time \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)