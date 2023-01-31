# https://cs50.harvard.edu/python/2022/psets/8/jar/

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size
#        return str(self.size)

    #  Raise ValueError if adding n > capacity
    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size = self.size + n

    #  Raise ValueError if subtracting n < size
    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size = self.size - n

    # max capacity of jar (total after calculation)
    @property
    def capacity(self):
        return self._capacity 

    @capacity.setter
    def capacity(self, capacity):
        if not capacity > 0:
            raise ValueError
        self._capacity = capacity

    # current number of cookies in jar
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError
        else:
            self._size = size
            
def main():
    jar = Jar()
    print("Capacity: 12")
    d = int(input("Deposit: "))
    jar.deposit(d)
    w = int(input("Withdraw: "))
    jar.withdraw(w)
    print(jar)

if __name__ == "__main__":
    main()
