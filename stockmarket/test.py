def generator():
    response = input("enter smth").lower()
    if response == "yes":
        generator()
    elif response == "no":
        pass
    else:
        print("Error. Input correct value")
        generator()

generator()