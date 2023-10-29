N = int(input("Enter a positive integer N: "))
numbers = []

for i in range(N):
    num = int(input("Enter number {} of {}: ".format(i + 1, N))
    numbers.append(num)

X = int(input("Enter an integer X: "))

if X in numbers:
    index = numbers.index(X) + 1
    print("The index of {} is: {}".format(X, index))
else:
    print("-1")
