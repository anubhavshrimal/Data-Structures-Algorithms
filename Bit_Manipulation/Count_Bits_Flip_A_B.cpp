/* 
Count number of bits needed to be flipped to convert from A to B.
*/ 

#include <iostream>

using namespace std;

int count_bits_flip(int a, int b){
    // Perform a xor b
    int c = a ^ b;

    int count = 0;

    // count number of 1s in c
    while (c != 0){
        c &= (c-1);
        count += 1;
    }

    return count;
}

int main(){
    int a = 15; // 15 = (1111)
    int b = 2;  // 2  = (0010)
    cout << "Number of bits needed to be flipped to convert from " << a << 
    " to " << b << " = " << count_bits_flip(a, b) << endl;
    return 0;
}
