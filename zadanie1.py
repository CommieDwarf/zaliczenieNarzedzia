current = 2021

birth = int(input("Podaj rok urodzenia"))

if birth > current:
    print("Nie prawidłowy rok urodzenia");
else:
    age = current - birth;
    
    if age >= 18:
        print("Masz", age, "lat i jesteś pełnoletni")
    else:
        print("Masz", age, "lat i nie jesteś pełnoletni")
