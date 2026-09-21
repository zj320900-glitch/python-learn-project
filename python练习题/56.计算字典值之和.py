def sum_dict(dict1):
    sum = 0
    for i in dict1:
        sum += dict1[i]
    return sum
dict1 = {"a": 100, "b": 200, "c": 300}
sum = sum_dict(dict1)
print(sum)
