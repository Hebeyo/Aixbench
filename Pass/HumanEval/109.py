def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    my_arr = arr.copy()
    for i in range(len(arr)):
        if sorted(my_arr) == my_arr:
            return True
        my_arr = [my_arr[-1]] + my_arr[0:-1]
    if sorted(my_arr) == my_arr:
        return True
    return False

def check(candidate):
    for item in range(31):
        assert candidate([3, 4, 5, 1, 2]) == True, 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate([3, 5, 10, 1, 2]) == True
        assert candidate([4, 3, 1, 2]) == False
        assert candidate([3, 5, 4, 1, 2]) == False, 'This prints if this assert fails 2 (also good for debugging!)'
        assert candidate([]) == True
'\nStandard answer: \n    if len(arr)==0:\n      return True\n    sorted_array=sorted(arr)\n    my_arr=[]\n    \n    min_value=min(arr)\n    min_index=arr.index(min_value)\n    my_arr=arr[min_index:]+arr[0:min_index]\n    for i in range(len(arr)):\n      if my_arr[i]!=sorted_array[i]:\n        return False\n    return True\n'
check(move_one_ball)