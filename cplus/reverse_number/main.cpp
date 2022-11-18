#include <iostream>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        
        long lx=x;
        string xstring=to_string(lx);
        string reverse="";
        bool negative=false;
        
        if (x<0){
            negative=true;
            lx*=-1;
            xstring=to_string(lx);
        }
        
        for (long j=xstring.length()-1;j>=0;j--){
            reverse.push_back(xstring[j]);
        }
        
        long lnum=stol(reverse, nullptr, 10);
        
        if (lnum > pow(2,31)){
            lnum=0;            
        }
            
        
        if (negative)
            lnum*=-1;
        
        return int(lnum);
    }
};

int main(){
	Solution test;
	cout<<test.reverse(1234)<<endl;
}
