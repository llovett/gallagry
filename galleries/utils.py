from random import choice
import re

def random_string(length=127):
    return ''.join(choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in xrange(length))

def slugify(string):
    slug = re.sub('[^\w\s-]', '', string).strip().lower()
    slug = re.sub('[-\s]', '_', slug)
    return slug
