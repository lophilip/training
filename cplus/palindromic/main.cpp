#include <string>
#include <vector>
#include <iostream>

class Solution {
public:
    std::string longestPalindrome_slow(std::string s) {	//brute force method
	int i=0;
	int j=0;
	int longest=0;
	int longest_index=0;
	
	std::string check_string="";
	
	std::vector <std::string> pal;

	for (i=0;i<s.length();i++){
		for (j=0;j<s.length()-i;j++){
			check_string=s.substr(i,j+1);
			std::string temp_string="";
		
			
			//check for palindrome
			for (int x=check_string.length()-1;x>=0;x--)
				temp_string+=check_string[x];
			if (temp_string==check_string)
			{
				std::string new_string = check_string;
				pal.push_back(new_string);
			}
		}	

	}

	
        for (int x=0;x<pal.size();x++){
		if (pal[x].length()>longest){
			longest=pal[x].length();
			longest_index=x;
		}
	}
	return pal[longest_index];
    }

	
};


int main(){
	Solution test;
	std::string entry="abcdbbfcba";
	std::string long_entry="ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwius";

	std::cout<<test.longestPalindrome_slow(entry)<<std::endl;

	std::cout<<test.longestPalindrome_slow(long_entry)<<std::endl;

}
