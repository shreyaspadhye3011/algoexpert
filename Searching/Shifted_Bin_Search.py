# Approach III: Algoexpert: Notice that for any mid, at least one of right or left will be properly sorted (as the whole array is sorted). Use this knowledge and number's comparison to boundaries to pivot between left or right component
# O(log N)

# Important Observation: 
# 1) Any position of mid (or any index) for a "shifted sorted array" will always split the array in at least one sorted half (the other will have a dip and rise)
# 2) This knowledge can be used to check whether the element can exist in the sotrted half. If yes, search sorted half, If not, search the other half
# a) Notice that if a[left] <= a[mid], then left side is sorted -- Draw and check -- because if a[left] <= a[mid], there cannot be a dip and rise (shifted origin) in the left half because then every element to right of mid will be higher than mid and thus higher than left. Thus the array is not sorted, then
# b) Similarly, if a[mid] <= a[right], right is sorted -- though not required -- will be in else as one half will definitely be sorted

# Learning: Always analyze your solutions. Finding a solution may not be good enough if it beats the complexity bound / purpose.
def shiftedBinarySearch(array, target):
	left = 0
	right = len(array) - 1
	while left <= right:
		mid = (left + right) // 2
		if array[mid] == target:
			return mid
		# left half is sorted half
		elif array[left] <= array[mid]:
			# check if element exists in left half range
			if target >= array[left] and target < array[mid]:
				# explore left
				right = mid - 1
			else:
				# explore right
				left = mid + 1
		# right half is sorted
		else:
			# check if element exists in right half range
			if target > array[mid] and target <= array[right]:
				# explore right
				left = mid + 1
			else:
				# explore left
				right = mid - 1	
	return -1
			

#########################################################################


# Approach II: Find shift index (where the origin has shifted to) and do binary search on both parts of the array - [start : shift_index] & [shift_index : end]
# Complexity: O(N) - becuase findShiftIndex is O(N)
# doesn't help. O(N) search is as good as linear


#########################################################################

# Approach I: Find shift index (where the origin has shifted to) and keep doing binary search
# Complexity: O(N) - becuase findShiftIndex is O(N). Doesn't help. What's the point of doing all this? Just do linear search if you're going to take O(N) time

# Important learnings / observations:
# 1. mid can directly be calculated if you know start_index & length. You don't really need to know the end (eases calculation in current problem)
# 2. length always changes to length / 2
# These 2 observations really help visualize the problem and make calculations easier. As now you only need to worry about proper mid indexing when the start is at an offset

# Remember: For Bin search: mid is always `(start + end) / 2` ie it is (len - 1) / 2 

# Status - All test cases passing on AlgoExpert

def shiftedBinarySearch(array, target):
    result = -1
    start = findShiftIndex(array)
    arr_len = len(array)
    curr_len = arr_len
    # keep searching unless there are elements in the search space
    while curr_len > 0:
        # notice through an example -- mid indexing is always based on start
        mid = (start + int((curr_len-1)/2))%arr_len
        if array[mid] == target:
            return mid
        elif array[mid] < target:   # check right
            start = mid + 1        
            # Notice: It should actually be "(mid + 1) % arr_len" but it still works cz mid calculation above done with % arr_len
        curr_len = int(curr_len/2)
    return result

# find index where origin has shifted to. it'll basically be a dip
# todo: add logic to handle equality?
def findShiftIndex(array):
  array_len = len(array)
  if array_len == 0: return 0
  current = array[0]
  for idx in range(1, array_len):
    if array[idx] < current:
        # shift spotted
        return idx
    current = array[idx]
  return 0



################################# OLD: ########################################


# print(shiftedBinarySearch([46, 61, 71, 72, 73, 0, 1, 21, 33, 46], 33))  # 8
# print(shiftedBinarySearch([46, 61, 71, 72, 73, 0, 1, 21, 33, 46], 73))  # 4
# print(shiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 0, 1, 21], 33))  # 0
# print(shiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 0, 1, 21], 0))  # 7
# print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 61))  # 1 
# print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 610))  # -1 
print(shiftedBinarySearch([0, 1, 21, 33, 45, 65, 99], 99))  # 6
# print(shiftedBinarySearch([5, 23, 111, 1], 111))  # 2

def v1shiftedBinarySearch(array, target):
    result = -1
    start = findShiftIndex(array)
    # print("Start: {}".format(start))
    arr_len = len(array)
    curr_len = arr_len
    count = 0
    end = start - 1
    if start == 0:
        end = arr_len - 1
    # keep searching unless there are elements in the search space
    while curr_len > 0:
        # notice through an example -- mid indexing is always based on start
        mid = (start + int((curr_len-1)/2))%arr_len
        print("Current length: {}".format(curr_len))
        print("checking {}: {}".format(mid, array[mid]))
        if array[mid] == target:
            return mid
        elif array[mid] > target:   # check left
            # not really requied but kept for completeness. mid calculation only done by start and length
            end = mid - 1
            # Notice: should actually be  (mid - 1) >= 0 ? mid - 1 : arr_len - 1
        else:
            start = mid + 1         # check right
            # Notice: It should actually be "(mid + 1) % arr_len" but it still works cz mid calculation above done with % arr_len
            print("Right. & new start: {}".format(start))
        curr_len = int(curr_len/2)
        # curr_len = int((start + end) / 2) % arr_len
        count += 1
    return result


# with all comments and logic
def oldShiftedBinarySearch(array, target):
    result = -1
    start = findShiftIndex(array)
    arr_len = len(array)
    curr_len = arr_len
    end = arr_len - 1
    count = 0
    if start == 0:
        end = start - 1
    # keep searching unless there are elements in the search space
    while curr_len > 0:
        # notice through an example -- mid indexing is always based on start
        mid = (start + int(curr_len/2))%arr_len
        # print("Current length: {}".format(curr_len))
        # print("checking {}: {}".format(mid, array[mid]))
        if array[mid] == target:
            return mid
        elif array[mid] > target:   # check left
            end = mid - 1
        else:
            start = mid + 1         # check right
            # print("Right. & new start: {}".format(start))
        
        # NOT REQUIRED! curr_len will always change to curr_len/2 in binary search
        # if start <= end:
        #     curr_len = end - start + 1
        # else:
        #     curr_len = ((end + arr_len) - start) + 1
        # print("?> Count: {}".format(count))
        curr_len = int(curr_len/2)
        count += 1
    return result