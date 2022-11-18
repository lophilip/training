#include <string>
#include <vector>
#include <iostream>

/*
typedef std::cout cout;
typedef std::string string;
typedef std::vector vector;
*/
using namespace std;
class Solution {
public:
    string convert(string s, int numRows) {
        string srow[numRows];
	int row_index=0;
	int s_index=0;
	string final="";

	while (s_index<s.length()){
		//print down
		for (;row_index<numRows && s_index<s.length();row_index++){
			srow[row_index].push_back(s[s_index]);
			s_index++;
		}
		
		//print accross
		for (row_index=numRows-1-1;row_index>=0 && s_index<s.length();row_index--){
			srow[row_index].push_back(s[s_index]);
			s_index++;
		}
		row_index=0;
		row_index++;
		if (row_index>=numRows)
			row_index=numRows-1;
	
	}

	for (int x=0;x<numRows;x++){
		final+=srow[x];
	}
	
	return final;
    }
};


int main(){
	string testcase="AB";
	Solution zig;
	cout<<zig.convert("PAYPALISHIRING",3)<<endl;
	cout<<zig.convert("AB",1)<<endl;
}

