import math  # importing math library

testcases = int(input())  # reading no'of testcases
while (testcases > 0):  # iterate over a loop for tranking testcases
    testcases -= 1  # even time decrement the testcase by one
    no_of_employees = int(input())  # reading no'of employees
    ranks_of_employees = list(map(int, input().split()))  # reading their respective ranking
    left_constraint = [
                          1] * no_of_employees  # left_constraint is the list with size no_of_employees initially filled with all 1's
    right_constraint = [
                           1] * no_of_employees  # right_constraint is the list with size no_of_employees initially filled with all 1's
    both_constraints = []  # by appling both the constraints (left,right)neighbours it holds the max of left_constraint and right_constraint
    for left in range(1,
                      no_of_employees):  # iterating the loop for filling the left_constraint list from index 1 to no_of_employees
        if ranks_of_employees[left] > ranks_of_employees[
            left - 1]:  # if we find the rank of the employee is greater than the left neighbour
            left_constraint[left] = left_constraint[
                                        left - 1] + 1  # then increment the left_constraint value of current with left_constraint value of left neighbours by one
    for right in range(no_of_employees - 2, -1,
                       -1):  # iterating the loop for filling the right_constraint list from index no_of_employees-2 to 0
        if ranks_of_employees[right] > ranks_of_employees[
            right + 1]:  # if we find the rank of the employee is greater than the right neighbour
            right_constraint[right] = right_constraint[
                                          right + 1] + 1  # then increment the right_constraint value of current with right_constraint value of right neighbours by one
    for both in range(0, no_of_employees):
        both_constraints.append(max(left_constraint[both], right_constraint[
            both]))  # finding the maximum of left_constraint and right_constraint and append to the final both_constraints list
    if testcases == 0:
        print(sum(both_constraints),
              end="")  # just suming the both_constraints list to get required maximum gifts to be needed to give for the employees
    else:
        print(sum(both_constraints))


