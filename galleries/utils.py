from random import choice

def random_string(length=127):
    return ''.join(choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in xrange(length))
