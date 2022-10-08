import time
import sys

MAX_VAL = 10_000

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    skills = populate_skills(lines)
    skill_names = ["SKILL_BREAKDANCING", "SKILL_APICULTURE", "SKILL_BASKET", "SKILL_XBASKET", "SKILL_SWORD", "TOTAL_XP"]
    algo = sys.argv[1]

    total_time = 0
    for i in range(len(skills)):
        sys.stdout.write(f"{skill_names[i]}\n")
        if algo == "standard":
            time_taken = time_hoare(skills[i])
            total_time += time_taken
            write_array(skills[i])
        elif algo == "custom":
            time_taken, skills[i] = time_custom(skills[i])
            total_time += time_taken
            write_mixed_array(skills[i])
        else:
            print("Invalid algorithm")
            return
        sys.stdout.write(f"time taken: {time_taken}\n\n")

    sys.stdout.write(f"total time taken: {total_time}\n")


# populate the skills array from stdin lines
def populate_skills(lines):
    skills = [[] for i in range(6)]
    for i in range(len(lines)):
        sum = 0
        nums = lines[i].split()
        for j in range(len(nums)):
            n = int(nums[j])
            sum += n
            skills[j].append(n)
        skills[5].append(sum)
    return skills


 # write the array returned from custom sort to the file         
def write_mixed_array(arr):
    for i in range(len(arr)-1, MAX_VAL, -1):
        sys.stdout.write(str(arr[i]) + "\n")
    for i in range(MAX_VAL, -1, -1):
        for j in range(arr[i]):
            sys.stdout.write(str(i) + "\n")


# write the array to the file
def write_array(arr):
    for i in range(len(arr)-1, -1, -1):
        sys.stdout.write(str(arr[i]) + "\n")


# function to time the custom sort
def time_custom(a):
    start_time = time.time_ns()
    a = count_sort(a, MAX_VAL)
    time_taken_in_microseconds = ( time.time_ns()- start_time ) / 1000.0 
    return time_taken_in_microseconds, a


# function to time the standard sort
def time_hoare(a):
    start_time = time.time_ns()
    quicksort_hoare(a, 0, len(a) - 1)
    time_taken_in_microseconds = ( time.time_ns()- start_time ) / 1000.0 
    return time_taken_in_microseconds


# custom sort
def count_sort(a, maxval):
    count = [0] * (maxval+1)
    big_numbers = []
    for num in a:
        if num > maxval:
            big_numbers.append(num)
            continue
        count[num] += 1

    quicksort_hoare(big_numbers, 0, len(big_numbers) - 1)

    # result = []
    # for i in range(len(count)):
    #     for j in range(count[i]):
    #         result.append(i)
    return count + big_numbers


# standard sort
def quicksort_hoare( arr, lo, hi ):
    if lo < hi: 
        new_pivot_index = partition_hoare( arr, lo, hi )     
        quicksort_hoare( arr, lo, new_pivot_index )
        quicksort_hoare( arr, new_pivot_index + 1, hi )

def partition_hoare( arr, lo, hi ):
    pivot = arr[ ( hi + lo ) // 2 ] 
    left = lo - 1   
    right = hi + 1  
    while True:
        left += 1
        while arr[left] < pivot: left += 1
        right -= 1
        while arr[right] > pivot: right -= 1
        if left >= right: return right 
        arr[left], arr[right] = arr[right], arr[left] 

if __name__ == '__main__':
    main()