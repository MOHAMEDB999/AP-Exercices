citiz = []

while True:
    citi = input("Enter the name of a city (or type 'stop' to finish): ")
    if citi.lower() == "stop":
        break
    population = len(citi.replace(" ", "")) * 1_000_000
    citiz.append((citi, population))

citiz.sort(key=lambda x: x[1], reverse=True)

print("\nCities and their populations:")
for citi, population in citiz:
    print(f"{citi}: {population:,} citizens")
