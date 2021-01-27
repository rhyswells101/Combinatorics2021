#SEARCHED : Dictionary with multiple values per key
import collections
import itertools


x= {"apple":[1]}
y={"apple": [1,2]}
w={"apple":1, "pear":1}
print(x|y)
#dont what update removes values.


def mergeDict(dict1, dict2):
   ''' Merge dictionaries and keep values of common keys in list'''
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = [value , dict1[key]]
   return dict3

z=mergeDict(x,y)
print(z)

#
# Append multiple value to a key in dictionary
def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

#Create a dictionary where multiple values are
# associated with a key

word_freq = {'is': [1, 3, 4, 8, 10],
             'at': [3, 10, 15, 7, 9],
             'test': [5, 3, 7, 8, 1],
             'this': [2, 3, 5, 6, 11],
             'why': [10, 3, 9, 8, 12]}
# Append multiple values for existing key 'at'
word_freq = add_values_in_dict(word_freq, 'at', [20, 9, 22])
#TODO: remove repeats for at. Warning not the same as intersection.
    # # >>> t
    # # [1, 2, 3, 1, 2, 5, 6, 7, 8]
    # # >>> list(set(t))
    # >>> list1 = [1,2,3,4,5,6]
    # >>> list2 = [3, 5, 7, 9]
    # >>> list(set(list1).intersection(list2))
    # [3, 5]

print('Contents of the dictionary: ')
print(word_freq)
#Append multiple values for a new key 'here'
#adding new term.
# word_freq = add_values_in_dict(word_freq, 'here', [10, 11, 12])
# print('Contents of the dictionary: ')
# print(word_freq)
#TODO: Change seed data to values in form list.

#How to combine Dictionaries:

#update
dict1= {"a":1}
dict2={"b":2}
dict3={"c":3,"d":4 , "e":4}
update_dicts = dict1.copy()
update_dicts.update(dict3)
#print(update_dicts)

#update dict with loop
combine_dicts = {}
for i in [dict1,dict2,dict3]:
    combine_dicts.update(i)
# print(combine_dicts)

# dicts with lists :

dicts_with_lists = dict(list(dict1.items()) + list(dict2.items()) + list(dict3.items()))
print(dicts_with_lists)

#4 put all dictionaries inside a dictionary
#type of unpacking # See PEP 448
all_dicts = {**dict1,**dict2,**dict3}
print(all_dicts)

#5 chain
chain = dict(itertools.chain(dict1.items(),dict2.items(),dict3.items()))
print(chain)

#6 chainmap
chain_map = dict(collections.ChainMap(dict1,dict2,dict3))
print(chain_map)


p={(0,2): {0,1,1,2}} #Dictionaries can hold sets as values.
print(p)
