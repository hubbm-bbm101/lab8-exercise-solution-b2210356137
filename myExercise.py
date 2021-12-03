import sys
dict = {}
with open(sys.argv[1], "r+") as f:
    for elements in f:
        name, education = elements.split(":")
        dict[name] = education[:]
    for person in sys.argv[2].split(","):
        try:
            print(f"Name: {person}, University: {dict[person]}",end='')
        except:
            print(f"No record of '{person}' was found!")