Dict={
    "Fast":"Quick",
    "Try":"to do again",
    "Marks":[1,2,4,6],
    "anotherDict":{'fry':"to roast"}, #nested dictionary
    1: 2

}
# print (Dict["Fast"])
# print (Dict["Marks"])
# print(Dict['anotherDict']['fry'])

# print(Dict.keys()) #prints keys
# print(Dict.values()) #prints values
# print(list(Dict.keys()))#changes into list
# print(Dict.items()) #print (key, value) for all elements of dictionary

print(Dict)
updadeDict={
    2:3,
    "ABC":"Pin",
    'Marks':[3,6,7,5] #Updates the 'Marks' key in Dict
}
Dict.update(updadeDict) #Updates the dictionary 'Dict' by adding key value pairs from 'updateDict'
print(Dict)

print(Dict.get('Marks')) #prints value associated with key 'Marks'
print(Dict['Marks']) #prints value associated with key 'Marks'

# The difference between .get and [] syntax in dictionary
print(Dict.get('Marks2')) #Returns 'None' as 'Marks2' is not present in dictionary
# print(Dict['Marks2']) #throws an error as 'Marks2' is not present in dictionary