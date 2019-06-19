/*
Given N number of people and M different types of unlimited umbrellas.
Each mi in M denotes the exact number of people (mi), the ith umbrella type can accomodate. 
Find out the minimum number of umbrellas needed to accomodate all the N people.
if such a case is not possible then return -1.

Each umbrella has to fill exactly the number of people it can accomodate.
*/

#include<iostream>
#include<vector>

using namespace std;

int min_umbrellas_needed_util(int n, vector<int> umbrellas, vector<int> dp, int count){
    // if dp has already stored the solution for n people, return
    if(n == 0 || dp[n] != 0) return dp[n];
    
    int min_count = INT_MAX, curr_count;
    
    // Iterate over all the umbrella sizes
    for(auto i = umbrellas.begin(); i != umbrellas.end(); i++){
        
        // if umbrella can be accommodated fully 
        if(n - *i > 0)
            curr_count = min_umbrellas_needed_util(n-*i, umbrellas, dp, count+1);
        
        // if all people are accommodated
        else if(n - *i == 0)
            curr_count = count+1;

        // if the umbrella cannot get exact number of people to fit
        else
            curr_count = INT_MAX;
        
        if(curr_count < min_count)
            min_count = curr_count;
    }
    
    // memoize result
    dp[n] = min_count;

    return min_count;
}

int min_umbrellas_needed(int n, vector<int> umbrellas){
    // initialize a dp table for memoization
    vector<int> dp(n+1, 0);

    int count = min_umbrellas_needed_util(n, umbrellas, dp, 0);

    if(count == INT_MAX) return -1;
    return count;
}

int main() {
    vector<int> umbrellas{5,4,2,1};
    int n = 8;

    cout <<"Number of umbrellas needed to accomodate " << n << " people: " << min_umbrellas_needed(n, umbrellas) << endl;

    return 0;
}
