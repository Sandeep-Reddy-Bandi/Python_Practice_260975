# This problem is just like a stair case problem(How many ways to reach n stair using 1,2 or 3 steps at a time)
def countWays(n):  # Function to calculate how many ways to reach city B from city A
    result = [0] * (n + 2)
    result[0] = 1
    result[1] = 1
    result[2] = 2

    for i in range(3, n + 1):
        result[i] = result[i - 1] + result[i - 2] + result[i - 3]

    return result[n]


testcases = int(input())  # input no'of test cases
for testcase in range(1, testcases + 1):

    stations = int(input())  # input no'of stations in between A and B
    if testcase < testcases:
        print(countWays(stations + 1))  # we need to add 1 to stations
    else:
        print(countWays(stations + 1), end="")
