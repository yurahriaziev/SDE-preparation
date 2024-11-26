def count_balanced_subsegments(capacity):
    if not capacity or len(capacity) < 3:
        return 0
    
    n = len(capacity)
    count = 0
    i = 0

    while i < n:
        start = i
        while i < n and capacity[i] == capacity[start]:
            i += 1
        block_length = i - start

        if block_length >= 3:
            count += (block_length - 2) * (block_length - 1) // 2

        left = start - 1
        right = i
        while left >= 0 and right < n and capacity[left] == capacity[right]:
            if block_length >= 3:
                count += 1
            left -= 1
            right += 1

    return count

t1 = [9,3,3,3,9]
t2 = [3,3,3,3,3]
t3 = [1,2,3,4,5]
t4 = [4, 4, 4, 5, 5, 5, 5, 6]
t5 = [4,4,1]
t6 = [4,4,4]
t7 = [0,0,0]
t7 = [3,3]
t8 = [9,9,9,3,3,3]
print(count_balanced_subsegments(t8))