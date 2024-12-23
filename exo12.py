a = int(input("width: "))
if a < 0 :
    print("invalid w")
    exit()

b = int(input("Height: "))
if b < 0 :
    print("invalid h")
    exit()

print((" " + "#" * a) * b)
