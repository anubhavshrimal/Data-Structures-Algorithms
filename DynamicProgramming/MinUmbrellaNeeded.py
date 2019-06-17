"""
Given N number of people and M different types of unlimited umbrellas.
Each mi in M denotes the exact number of people (mi), the ith umbrella type can accomodate. 
Find out the minimum number of umbrellas needed to accomodate all the N people.
if such a case is not possible then return -1.

Each umbrella has to fill exactly the number of people it can accomodate.
"""

def min_umbrellas_needed_util(n, umbrellas, dp, count):
    # if dp has already stored the solution for n people, return
    if n == 0 or dp[n] != 0:
        return dp[n]
    
    min_count = float('inf')
    curr_count = None
    
    # Iterate over all the umbrella sizes
    for m in umbrellas:
        # if umbrella can be accomodated fully 
        if n - m > 0:
            curr_count = min_umbrellas_needed_util(n-m, umbrellas, dp, count+1)
        
        # if all people are accomodated
        elif n - m == 0:
            curr_count = count+1

        # if the umbrella cannot get exact number of people to fit
        else:
            curr_count = float('inf')
        
        if curr_count < min_count:
            min_count = curr_count

    # memoize result
    dp[n] = min_count

    return min_count


def min_umbrellas_needed(n, umbrellas):
    # initialize a dp table for memoization
    dp = [0] * (n+1)

    count = min_umbrellas_needed_util(n, umbrellas, dp, 0)

    if count == float('inf'):
        return -1

    return count

umbrellas = [5,4,2,1]
n = 8

print(f"Number of umbrellas needed to accomodate {n} people: {min_umbrellas_needed(n, umbrellas)}")

