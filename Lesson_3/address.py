class Address:
    index = 0
    city = "no"
    street = "no"
    house = "0"
    appartment = "0"

    def __init__(self, _index, _city, _street, _house, _appartment):
        self.index = _index
        self.city = _city
        self.street = _street
        self.house = _house
        self.appartment = _appartment
