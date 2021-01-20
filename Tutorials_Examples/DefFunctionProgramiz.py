# def function_name(parameters):
# 	"""docstring"""
# 	statement(s)
#
# def greet(name): # need to def function before run
#     """
#     This function greets to
#     the person passed in as
#     a parameter
#     """
#     print("hello, " + name + ". good morning!")
# print(greet("Rhys")) #Rhys is the arguement


# def add_numbers(x,y):
#    result = x + y
#    return result #function terminates and control returns to original place where it was called.
#
# num1 = 5
# num2 = 6
# resultEnd = add_numbers(num1, num2) # result is returned to resultEnd
# print("The sum is", resultEnd)

############ When I want to determine function value for all subsets at once.
# def greet(*names):
#     """This function greets all
#     the person in the names tuple."""
#
#     # names is a tuple with arguments
#     for name in names:
#         print("Hello", name)
#
#
# greet("Monica", "Luke", "Steve", "John")

######################################### FOR PROJECT
#
I=[1,2]
J=[3]
# def msa_function(element1,element2): # for given decomp I,J
#     #check if I,J are equal
#  #   if len(element)==1
#   #      return 0
#    # elif
#
# def msa2_function(element): #For subset I irrespective of decomp.
def Merge(dict1, dict2):
    return(dict2.update(dict1))


#Set Pn as the powerset ordered by length.

OneSets0= [x for x in Pn if len(x)==1]
dict_OneSetsValue0={x: 0 for i in OneSets0}

# def twosetfunction0(twoset): #assigns a choice of 2sets the value 1.
#     return {twoset:0}
# def twosetfunction1(twoset): #assigns a choice of 2sets the value 1.
#     return {twoset:1}
#list two sets and turn to tuples.to store in dictionary
# L=tuple([1,3])
# make a choice for 2 sets with 0 and those with value 1.
TwoSets0 = # x needs to be a tuple,string,
TwoSets1 =
#pass respectively through twosetfunction0 & twosetfunction1.
value = twosetfunction1(L)
TwoSetsValue0= {x: 0 for i in TwoSets0} # x needs to be a tuple,string,
TwoSetsValue1= {x: 1 for i in TwoSets1}
print(Merge(TwoSetsValue0,TwoSetsValue1))

#print("The output is:",value )




#############################################
#

#



#

