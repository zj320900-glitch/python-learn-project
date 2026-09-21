def exsit_elemnet(list1, n):
    for i in list1:
        if(i == n):
            print(f"{n} 在list1中存在")
            break
    print(f"{n} 在list1中不存在")
test_list = [ 1, 6, 3, 5, 3, 4 ]
exsit_elemnet(test_list, n = "qw")
print(4 not in test_list)