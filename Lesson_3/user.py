class User:
    first_name = "no name"
    last_name = "no name"

    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name

    def say_name(self):
        print(self.first_name)

    def say_last_name(self):
        print(self.last_name)

    def say_full_ame(self):
        print(self.first_name, self.last_name)
        