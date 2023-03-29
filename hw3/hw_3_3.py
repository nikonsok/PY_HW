# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
def custom_range(inc_data, *args):
    if len(args) == 1:
        start = 0
        stop = inc_data.index(args[0])
        step = 1
    elif len(args) == 2:
        start = inc_data.index(args[0])
        stop = inc_data.index(args[1])
        step = 1
    elif len(args) == 3:
        start = inc_data.index(args[0])
        stop = inc_data.index(args[1])
        step = args[-1]
    if step < 0:
        inc_data = inc_data[::-1]
        start = len(inc_data) - 1 - start
        stop = len(inc_data) - 1 - stop
        step = abs(step)
    result = []
    i = start
    while i < stop:
        result.append(inc_data[i])
        i += step
    return result