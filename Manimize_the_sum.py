import math  # importing math library
import heapq  # import heapq library as it contains priority queue (min heap,max heap)

length_of_array, maximum_no_of_operations = map(int,
                                                input().split())  # reading the size of the array and k no'of operations
array_list = list(map(int, input().split()))  # reading the array elements
# for max heap we need use '-' values
for element in range(0, length_of_array):
    array_list[element] = -array_list[element]

heapq.heapify(array_list)  # we are creatinng the max heap from the array_list elements

while (
        maximum_no_of_operations > 0):  # maximum_no_of_operations is not equal to zero then change the array(reduce any element by its half)
    maximum_no_of_operations -= 1  # decrement the maximum_no_of_operations by one in each iteration
    maximum_element = array_list[
        0]  # Everytime it will pop the maximum element in the array_list and store that poped element in the maximum_element
    heapq.heapreplace(array_list,
                      -math.floor(-maximum_element / 2))  # and insert the floor value of the poped element by its half

print(-sum(array_list),
      end=" ")  # finally we need to print the sum of all the elements in the array_list after maximum no_of modications


