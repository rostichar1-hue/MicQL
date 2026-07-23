import json

class Index:
    def __init__(self, table, field):
        self.table = table
        self.field = field
        self.data = {}

    def build(self, rows):
        self.data = {}
        for idx, row in enumerate(rows):
            key = row.get(self.field)
            if key not in self.data:
                self.data[key] = []
            self.data[key].append(idx)

    def lookup(self, value):
        return self.data.get(value, [])
