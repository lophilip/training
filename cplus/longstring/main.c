#include <string>
#include <iostream>
#include <vector>
#include <set>

class Solution {
public:
    
   	int lengthOfLongestSubstring(std::string s) 
	{

		long index=0;
		long length=0;
		long i=0;
		long j=0;

		std::set <char> stringset={};


		while (j<s.length()){

			if (stringset.find(s[j])==stringset.end())
			{//not found
				stringset.insert(s[j]);
				j++;
				if (stringset.size()>length)
					length=stringset.size();
			}
			else 
			{ //found				
				stringset.erase(s[i]);
				i++;
			}

		}
	
                
		return length;
	}
    	
};



int main()
{
	int answer;
	Solution s;
	std::string test1="abcabcbb";
	answer=s.lengthOfLongestSubstring(test1);
	std::cout<<answer;
}
