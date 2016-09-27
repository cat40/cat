class stringf(str):
    def rstrippattern(self, pattern):
        while self.endswith(pattern):
            self = self[:-len(pattern)]
        return self
    def lstrippattern(self, pattern):
        while self.startswith(pattern):
            self = self[:len(pattern)]
        return self
