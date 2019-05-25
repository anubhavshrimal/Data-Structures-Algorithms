// Find the number of trailing zeros present in the factorial of a number n.

#include <iostream>

using namespace std;

int fact_trailing_zeros(int num){
    int c = 5;
    int count = 0;

    // count number of factors of 5 possible in num!
    // 5 paired with 2 will give 10 i.e. 1 trailing zero
    // powers of 5 will give multiple zeros
    while(num / c != 0){
        count += num / c;
        c *= 5;
    }
    return count;
}

int main(){
 
    int num = 1000;
    cout << num<< "! has " << fact_trailing_zeros(num) << " trailing zeros"<< endl;
    return 0;

}
