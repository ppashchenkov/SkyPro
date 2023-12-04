from smartphone import Smartphone

catalog = [
    Smartphone("Android", "Pixel 4", "+7-999-777-5541"),
    Smartphone("Android", "Pixel 7", "+7-999-777-5542"),
    Smartphone("Android", "Pixel 7a", "+7-999-777-5543"),
    Smartphone("Apple", "iPhone12", "+7-999-777-5544"),
    Smartphone("Apple", "iPhone13", "+7-999-777-5545")
]

for phone in catalog:
    print(f"{phone.model} - {phone.model}. {phone.number}")