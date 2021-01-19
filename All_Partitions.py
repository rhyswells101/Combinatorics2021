from itertools import chain, combinations

#want partions of length n set.
#Outputs all paritions on [n] only want partitions into two.

something = list(range(1,5)) #range starts at 1 and ges to n-1.



def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]

    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset
        yield [ [ first ] ] + smaller



for n, p in enumerate(partition(something), 1): #input:
    # enumerate() method adds counter to an iterable and returns it.
    print(n, sorted(p)) # sorted puts into ascending order.


print()