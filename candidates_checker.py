import sys;
storage = {}

if len(sys.argv) != 2:
    print("Error: wrong number of arguments")
    exit(1)

candidates = int(sys.argv[1])

for i in range(0, candidates):
    print('Add a new candidate:')
    name = input('name: ')
    age = input('age: ')
    storage[name.strip()] = int(age.strip())

for key, value in storage.items():
    if value < 18:
        print(f"{key} is not eligible (underaged)")
    elif value > 60:
        print(f"{key} is not eligible (over the legal age)")
    else:
        print(f"{key} is eligible")