
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]



lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``

if "yellow" in lst[2]:
    yellow = True
if 4 in lst[1]:
    four = True
else:
    four = False
if "orange" in lst[0]:
    orange = True

#Test to see if 4 is in the second list of lst. Save to variable ``four``


#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``


L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1

# Test if [5, 8, 7] is in the list L. Save to variable name test2

# Test if 6.6 is in the third element of list L. Save to variable name test3

for inl in L:
    if "hola" in inl:
        test1 = True
    else:
        test1 = False

if [5,8,7] in L:
    test2 = True
else:
    test2 = False

if 6.6 in L[2]:
    test3 = True
else:
    test3 = False



nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]],
'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]
}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.

list_ = nested.keys()
if "data" in list_:
    data = True
else:
    data = False
data_value_lst = nested["data"]
if 24 in data_value_lst:
    twentyfour = True
else:
    twentyfour = False
window_value_lst =  nested["window"]
if "whole" not in window_value_lst:
    whole = True
else:
    whole = False
if "physics" in list_:
    physics = True
else:
    physics = False

# values_lst = list(nested.values())
# all_words_lst = []
# for lst in values_lst:
#     for lst2 in lst:
#         if type(lst2) is list:
#             for lst3 in lst2:
#                 if type(lst3) is list:
#                     for item in lst3:
#                         all_words_lst.append(item)
#                 else:
#                     all_words_lst.append(lst3)
#         else:
#             all_words_lst.append(lst2)
#
#     if "physics" in all_words_lst:
#         physics = True
#     else:
#         physics = False
#


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = nested_d["London"]['Great Britain']



sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'],
'track': ['sprint', 'distance', 'jumps', 'throws'],
'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1

# Assign the string 'platform' to the name v2

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3

# Assign the string 'rings' to the name v4

v1 = sports["swimming"][2]
v2 = sports["diving"][1]
v3 = sports["gymnastics"]["women"]
v4 = sports["gymnastics"]["men"][-1]



nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19},
'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22},
 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []

US_count.append(nested_d["Beijing"]["USA"])
US_count.append(nested_d["London"]["USA"])
US_count.append(nested_d["Rio"]["USA"])



l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = []
for l in l_of_l:
    third.append(l[2])



athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'],
['Felix', 'Bolt', 'Gardner', 'Eaton'],
['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = []
other = []
for ath_lst in athletes:
    for ath in ath_lst:
        if "t" in ath:
            t.append(ath)
        else:
            other.append(ath)

print(t)
print(other)
