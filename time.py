print ("Kolik je hodin?")
time = int(input("Kolik je?: "))
if time < 6:
    print("Je noc.")
elif time < 8:
    print("Je ráno.")
elif time < 12:
    print("Je dopoledne.")
elif time == 12:
    print("Je poledne.")
elif time < 18:
    print("Je odpoledne.")
elif time < 20:
    print("Je večer.")
elif time < 24:
    print("Je noc.")
else:
    print("To není realný čas!")
    