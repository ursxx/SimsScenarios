import json
import random
import sys
import time


def show_random_name(names, gender):
    time.sleep(1)
    print(random.choice(names[gender]), random.choice(names["surnames"]))


def show_random_appearance(appearances):
    time.sleep(1)
    cechy = random.choice(appearances["character"]) + ", " \
            + random.choice(appearances["character"]) + ", " \
            + random.choice(appearances["character"])
    return "Kolor włosów Sima/Simki: " + random.choice(appearances["hairColour"]) + \
           "\nAspiracja Życiowa Sima/Simki: " + random.choice(appearances["aspirations"]) + \
           "\nCechy osobowości Sima/Simki: " + cechy


def show_random_life(gameplay):
    time.sleep(1)
    return "Miejsce zamieszkania Sima/Simki: " + random.choice(gameplay["map"]) + \
           "\nWygenerowane wyzwanie: " + random.choice(gameplay["challenge"])


with open("simsScenarios.json") as json_file:
    namesData = json.load(json_file)

with open("simsScenarios2.json") as json_file:
    appearancesData = json.load(json_file)

with open("simsScenarios3.json") as json_file:
    gameplayData = json.load(json_file)

print("")
print("Generator scenariusza do The Sims 4")
print("Witaj w skromnym programie, w którym wygeneruję Ci wyzwanie do rozgrywki w The Sims 4.\n"
      "Na początku będziesz musiał wybrać płeć Sima, dopiero potem zostanie wygenerowana rozgrywka. Miłej zabawy :)")
print("")
gender_choice = input("Wybierz płeć [kobieta, mężczyzna]: ")
print("")

if gender_choice == "kobieta" or gender_choice == "mężczyzna":
    show_random_name(namesData, gender_choice)
else:
    print("Nie ma takiego wyboru. Do wyboru kobieta lub mężczyzna.")
    sys.exit(0)

print(show_random_appearance(appearancesData))
print(show_random_life(gameplayData))
print("")
print("Miłej rozgrywki :)")
