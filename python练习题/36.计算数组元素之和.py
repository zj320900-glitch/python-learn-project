def sum_arr(arr, n):
    return(sum(arr))
def sum_arr2(arr, n):
    sum = 0
    for i in range(0, n):
        sum = sum + arr[i]
    else:
        print(f"数组 {arr} 的和为：{sum}")
arr = []
arr = [1, 2, 3, 4]
n = len(arr)
result = sum_arr(arr, n)
print(f"数组 {arr} 的和为：{result}")
sum_arr2(arr, n)

