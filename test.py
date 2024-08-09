test_cases = int(input())

for _ in range(test_cases):
    queries_num = int(input())
    q_array = [int(x) for x in input().split()]
    new_arr = [1]
    is_joint_found = False
    joint = 0
    max_ = q_array[0]
    
    for j in range(1, queries_num):
            if q_array[j] >= max_ and not is_joint_found:
                max_ = q_array[j]
                new_arr.append(1)
            else:
                if q_array[j] > q_array[0] or q_array[j] < joint:
                    new_arr.append(0)
                else:
                    is_joint_found = True
                    joint = q_array[j]
                    new_arr.append(1)  
    print("".join(str(el) for el in new_arr))
