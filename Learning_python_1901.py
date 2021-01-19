#Basics of sort function
#https://www.youtube.com/watch?v=D3JvDWO-BY4&list=PLKCboQ_AghikykkG9H3iD4CXOjoxMRkbR&index=80&ab_channel=CoreySchafer
# li = [9,1,2,3,4,7,1]
# s_li=sorted(li)
# print(s_li)
#
# li.sort() # sorted method here
# print(li)
# s_2li=sorted(li, reverse=True)
# print(s_2li)
#
# # why sort method (specific to list) or sort function?
#
# tup=(9,1,2,3,4,7,1)
# s_tup = sorted(tup)
# print(s_tup) #output is list
#
# di = {'animals': 'dog', 'people': 'tom'}
# s_di =sorted(di) # sorts by alphabet
# print(s_di)

# li2= [-2,1,-5,-7,2,4,5]
# s_li2=sorted(li2)
# abs_li2=sorted(li2, key=abs)
# print(abs_li2)
##################################################
#How to import modules
Print("imported learning_python_1901")
test = "test string"
def find_index(to_search,target): # fins the index for a value in sequence
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

print(find_index([2,3,5,-1,0,0,0,0],8))