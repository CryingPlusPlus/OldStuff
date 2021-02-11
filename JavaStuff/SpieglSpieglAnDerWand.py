while True:
    str = input()
    if str == "quit":
        break
    if str == "":
        str = "Spieglein Spieglein an der Wand"

    print(str[::-1])