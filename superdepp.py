import os.path

PLAYER_COUNT = 10

def read_file(file):
    lines = []

    with open(file, "r") as inp:
        lines = inp.readlines()

    return lines


def get_num(string):
    splits = string.split('=')
    if len(splits) != 2:
        return None

    rmv_spaces = splits[0].split(" ")
    if (len(rmv_spaces) < 1) or (rmv_spaces[0].lower() != "superdepp"):
        return None

    rmv_spaces = splits[1].strip()
    if not rmv_spaces.isnumeric():
        return None

    return int(rmv_spaces)

def get_valid_votes(arr):
    invalids: int = 0
    players = [0] * PLAYER_COUNT

    for string in arr:
        num = get_num(string)
        if (num is None) or (num < 1) or (num > PLAYER_COUNT):
            invalids += 1
        else:
            players[num - 1] += 1

    return [invalids, players]

def superdepp(file):
    lines = read_file(file)
    [invalids, votes] = get_valid_votes(lines)

    for vote_index in range(len(votes)):
        print("Spieler " + str(vote_index + 1) + ": " + str(votes[vote_index]) + " Stimmen")

    max_val = max(votes)
    max_index = votes.index(max_val)

    print("\nSuperdepp ist Spieler " + str(max_index + 1) + " mit " + str(max_val) + " Stimmen!")
    print("Es sind " + str(invalids) + " ungültige SMS eingegangen.")

if __name__ == "__main__":
    path = input("Bitte geben Sie die Datei mit den SMS-Daten an: ")

    while not os.path.isfile(path):
        print("Die Datei " + path + " ist inexsistent!")
        path = input("Bitte geben Sie die Datei mit den SMS-Daten erneut an: ")

    superdepp(path)

    print("\nBitte drücken Sie [ENTER] zum Beenden des Programmes . . . ")
    x = input()
