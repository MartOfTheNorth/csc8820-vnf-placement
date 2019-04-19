# -*- coding: utf-8 -*-
"""
Created on 2007-10-15 at 17:44

@author: https://compprog.wordpress.com/2007/10/15/generating-the-partitions-of-a-set/
https://stackoverflow.com/questions/2037327/translating-function-for-finding-all-partitions-of-a-set-from-python-to-ruby
https://en.wikipedia.org/wiki/Bell_number
Eric Temple Bell, who wrote about them in the 1930s.

"""

def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(int(2**len(set_)/2)):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

l = [1, 3, 4]
for p in reversed(sorted(partitions(l))):
    print(p)
print('The Bell number is', len(list(partitions(l))))