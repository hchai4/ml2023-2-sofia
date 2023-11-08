class NumberProcessor:
    def __init__(self):
        self.data = []

    def read_n_numbers(self, n):
        for i in range(n):
            number = int(input("Enter a number: "))
            self.data.append(number)
    
    def search_x(self, x):
        if x in self.data:
            return self.data.index(x) + 1
        else: 
            return -1