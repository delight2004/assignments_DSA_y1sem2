combined=[]
def domestic_animals():
    n=int(input("Enter number of domestic animals:"))
    domestic=[]
    for i in range(n):
        animal=input(f"Enter domestic animal {i+1}: ")
        domestic.append(animal)
        combined.append(animal)
    return domestic

def wild_animals():
    n=int(input("Enter number of wild animals:"))
    wild=[]
    for i in range(n):
        animal=input(f"Enter wild animal {i+1}: ")
        wild.append(animal)
        combined.append(animal)
    return wild

def combined_list():
    domestic=domestic_animals()
    wild=wild_animals()
    print("Combined list of animals",combined)
combined_list()