def domestic_animals():
    """Collects a list of domestic animals from user input."""

    n = int(input("Enter number of domestic animals: "))
    domestic = []
    if n <=0:
        print("Invalid number of animals")
        return []
    for i in range(n):
        animal = input(f"Enter animal {i+1}: ")
        domestic.append(animal)
        
    print("Domestic animals:")
    return domestic

# Example usage (to see the list):
animal_list = domestic_animals()
if animal_list:  # Check if the list is not empty (meaning input was valid)
    for animal in animal_list:
        print(animal)
