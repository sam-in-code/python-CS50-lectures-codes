characters = [
    {"Name":"Robert", "House":"Baratheon", "Sigil":"Stag"},
    {"Name":"Tywin", "House":"Lannister", "Sigil":"Lion"},
    {"Name":"Eddard", "House":"Stark", "Sigil":"Wolf"},
    {"Name":"Daemon", "House":"Tagaeryon", "Sigil":"Dragon"},
    {"Name":"Jon Snow", "House":"Stark", "Sigil":None},
]
for character in characters:
    print(character["Name"], character["House"], character["Sigil"],sep=", ")
    
