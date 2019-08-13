import json


class Reader:
    def __init__(self):
        self.state = {}
        self.reload()

    def reload(self):
        with open("Settings/Settings.json") as set_:
            self.state = json.load(set_)

    def get_parameter(self, key):
        return self.state[key]

    def set_parameter(self, key, value):
        self.state[key] = value
        with open("Settings/Settings.json", "w") as set_:
            json.dump(self.state, set_)


if __name__ == '__main__':
    reader = Reader()
    print(reader.get_parameter("Disk"))
