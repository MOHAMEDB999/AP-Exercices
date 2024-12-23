people = int(input("How many people need to ride: "))
capacity = int(input("Ask the user how many people can fit in one taxi: "))
if capacity != 0 :
  taxis = people // capacity
  if people % capacity != 0 :
    taxis = taxis+1

  print(f"Number of taxis needed is :{taxis}")
else :
  print(" The people can't fit in the taxi ")
