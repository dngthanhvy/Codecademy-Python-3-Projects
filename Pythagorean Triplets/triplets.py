# Ex input: [12, 1, 6, 5, 7, 4]
# Triple loop to avoid duplicates


def triplets(input_list):
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            for k in range(j+1, len(input_list)):
                if input_list[i]**2 + input_list[j]**2 == input_list[k]**2:
                    return True
    return False


input_list = list(map(int, input().split()))
print(triplets(input_list))
