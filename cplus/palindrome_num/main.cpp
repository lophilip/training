#include <iostream>
#include <vector>
#include <math.h>

class Solution {
public:
    bool isPalindrome(int x) {  //can not use string
	int original=x;
	std::vector <int> digit;

	int remainder=-1;

	double long reverse_num=0;

	if (x<0)
		return false;
	
	while (x>0){
		remainder = x%10;
		digit.push_back(remainder);
		x=x/10;
	}

	for (int x=0;x<digit.size();x++){
		reverse_num+=digit[x]*pow(10,digit.size()-1-x);
	}
	
	if (reverse_num==original)
		return true;
	return false;
        
    }
};

int main(){
	Solution solution;
	std::cout<<solution.isPalindrome(10)<<std::endl;
	return 0;
}
