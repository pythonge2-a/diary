class Words:
    def __init__(self, filename, length=10):
        with open(filename, "r") as fp:
            self.words = fp.readlines()
        self.words = [v.strip() for v in self.words if v.strip()]
        self.length = length
        self.count = 0
    def __next__(self):
        self.count += 1
        if self.count > self.length:
            raise StopIteration()
        return random.choice(self.words)
    def __iter__(self):
        self.count = 0
        return self
