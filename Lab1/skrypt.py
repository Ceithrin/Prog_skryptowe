import sys

def is_prime(number):
    try:
        number = int(number)
    except:
        return False

    if number < 2:
        return False

    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    for i in sys.argv:
        if is_prime(i):
            print(i)