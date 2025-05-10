"""
Two_sum exercises: 
            here you need to check the target sum for two number or indices in array or list
            example:
            input: [2,4,6,3,2,8] target : 6
            output : [0,1], [1,4]
"""
num_arr = [1,4,5,3,7,4,7,3,4,6]

def two_sum_brute_force(num_arr, target):
    for i in range(len(num_arr)):
        for j in range(i+1,len(num_arr)):
            if (num_arr[i] + num_arr[j] == target):
                print(f"these indices {i}, {j} add for the {target} ")

two_sum_brute_force(num_arr, 8)

def two_sum_compliment_method(num_arr, target):
    num_dict = {}

    for i, num in enumerate(num_arr):
        diff = target - num
        if diff in num_dict:
            print(f"indices are {num_dict[diff]}, {i}")
        num_dict[num] = i

two_sum_compliment_method(num_arr, 8)