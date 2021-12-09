
class Filter:
    def __init__(self, name, filter):
        self.name = name
        self.filter = filter

    def execute(self, data):
        print("Executing filter: " + self.name)
        self.filter(data)
