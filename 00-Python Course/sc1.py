class Math:
    @staticmethod
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

print(Math.is_prime(7))
