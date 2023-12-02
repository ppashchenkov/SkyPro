from address import Address
class Mailing:
    to_address = Address(_index=0, _city="no", _street="no", _house="0", _appartment="0")
    from_address = Address(_index=0, _city="no", _street="no", _house="0", _appartment="0")
    cost = 0
    track = "no"

    def __init__(self, _to_address, _from_address, _cost, _track ):
        self.to_address = _to_address
        self.from_address = _from_address
        self.cost = _cost
        self.track = _track
        