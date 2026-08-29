class Example:
    company = "ABC"

    def show(self):
        print("Instance method")

    @classmethod
    def company_name(cls):
        print(cls.company)

    @staticmethod
    def greet():
        print("Hello")
