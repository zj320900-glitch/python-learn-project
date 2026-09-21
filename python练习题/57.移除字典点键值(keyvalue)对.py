test_dict = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4} 
print("字典移除前：" + str(test_dict))
del test_dict["Zhihu"]
print("字典移除后：" + str(test_dict))
test_dict = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4}
print ("字典移除前 : " + str(test_dict)) 
removed_value = test_dict.pop("Zhihu")
print ("字典移除后 : " + str(test_dict)) 
print ("移除的 key 对应的 value 为 : " + str(removed_value))

test_dict = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4}
print ("字典移除前 : " + str(test_dict)) 
new_dict = {key:val for key, val in test_dict.items() if key != "Zhihu"}
print ("字典移除后 : " + str(new_dict)) 
