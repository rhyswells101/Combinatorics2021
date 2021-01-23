#SEARCHED : Dictionary with multiple values per key

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
word_freq = add_values_in_dict(word_freq, 'at', [20, 21, 22])
print('Contents of the dictionary: ')
print(word_freq)
#Append multiple values for a new key 'here'
#adding new term.
word_freq = add_values_in_dict(word_freq, 'here', [10, 11, 12])
print('Contents of the dictionary: ')
print(word_freq)