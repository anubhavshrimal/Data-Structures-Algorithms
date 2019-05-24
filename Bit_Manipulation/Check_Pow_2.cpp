#include <iostream>

using namespace std;

bool check_pow_2(int num) {
    if ((num & (num-1)) == 0)
    	return true;
    return false;
}

int main() {
    int num = 2;

    check_pow_2(num) ? cout << "Num is a Power of 2" : cout << "Num is not a power of 2";
    cout << endl;

    num = 5;
    check_pow_2(num) ? cout << "Num is a Power of 2" : cout << "Num is not a power of 2";
    cout << endl;

    return 0;
}
