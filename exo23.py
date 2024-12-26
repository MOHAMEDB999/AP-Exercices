while True:
    try:
        N = int(input("give a positive int: "))
        if N <= 0:
            print("Input lazem ykon positive")
            print("TRY AGAIN ")
            continue
        break
    except ValueError:
        print("Invalid input. enter a positive int.")

for i in range(-N, N + 1):
    if i != 0:
        print(i)

