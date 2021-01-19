from itertools import combinations

def segmentations(a, k):
    n = len(a)
    assert 1 <= k <= n, (n, k)

    def split_at(js):
        i = 0

        for j in js:
            yield a[i:j] # a is the inital set [1,2,3,4]
            #slice of s from i to j is replaced by the contents of the iterable t
            i = j

        yield a[i:]

    for separations in combinations(range(1, n), k - 1):
        yield list(split_at(separations))


print(segmentations([1,2,3,4], 2)) # doesnt output yet, check k- partion bookmark and moreitertool