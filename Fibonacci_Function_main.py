# make a function for calculating the Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    # get the input
    n = int(input('Enter the number: '))

    # store the results
    fibonacci_number = fibonacci(n)

    # print the output
    print('The Fibonacci number for', n, 'is', fibonacci_number)

if __name__ == "__main__":
    main()
