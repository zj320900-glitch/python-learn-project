def Merge(dict1, dict2):
    return(dict2.update(dict1))
dict1 = {"a": 10, "b": 8}
dict2 = {"d": 6, "c": 4}
print(Merge(dict1, dict2))
print(dict2)
def Merge1(dict1, dict2):
    res = {**dict1, **dict2}
dict3 = {'a': 10, 'b': 8} 
dict4 = {'d': 6, 'c': 4} 
dict5 = Merge1(dict1, dict2) 
print(dict5)