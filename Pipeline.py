import Filter


class Pipeline:
    def __init__(self):
        print("Initializing pipeline...")
        self.filters = list()

    def add(self, filter: FilterObject.Filter):
        print("Adding filter to pipeline...")
        self.filters.append(filter)

    def execute(self, data):
        print("Executing pipeline...")
        for filter in self.filters:
            filter.execute(data)
        print("Finished pipeline...")