import random
odd = 0
even = 0

def gen_and_count():
    global odd
    global even
    for i in range(10000):
        if is_odd(random.randrange(101)):
            odd += 1
        else:
            even += 1
    print('Even:', even)
    print('Odd:', odd)


def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False
