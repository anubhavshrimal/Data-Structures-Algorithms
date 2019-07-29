/*
Find the two non-repeating elements in an array of repeating elements
*/

#include<iostream>
#include<vector>
#include<utility> 

using namespace std;

pair< int, int > find_non_repeating_numbers(vector<int> &arr) {
	pair< int, int > result = {0,0};
	
	if (arr.size() == 0)
		return result;
	
	int xor_all = 0;

	// if non repeating elements are 'a' and 'b' ;xor_all = a^b
	for (auto element : arr) {
		xor_all ^= element;
	}

	// number with one set bit of xor_all
	int right_set_bit = xor_all & ~(xor_all - 1);

	for (auto element : arr) {
		if (element & right_set_bit)
			result.first ^= element;
		else
			result.second ^= element;
	}

	return result;
}

int main() {

	vector<int> arr = {2, 3, 7, 9, 11, 2, 3, 11};

	pair<int, int> result = find_non_repeating_numbers(arr);

	cout << result.first << " " << result.second << endl;

	return 0;
}