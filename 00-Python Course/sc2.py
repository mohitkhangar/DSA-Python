class Tax:
    rate = 0.1
    @classmethod
    def new_rate(cls, rate):
        cls.rate = rate
Tax.new_rate(0.2)
print(Tax.rate)
