#include <vector>
#include <iostream>
using namespace std;
void countSwaps(vector<int> a) {
    bool finished=false;
    long num_swap=0;
    
    while (finished==false){
        finished=true;
        for (int i=0;i<a.size()-1;i++){
	    count<<i<<endl;
            if (a[i]>a[i+1]){		
                int temp = a[i];
                a[i]=a[i+1];
                a[i+1]=temp;
                finished=false;
                num_swap++;                
            }                
        }
        
    }
    
    cout<<"Array is sorted in "<<num_swap<<" swaps."<<endl;
    cout<<"First Element: "<<a[0]<<endl;
    cout<<"Last Element: "<<a[a.size()-1]<<endl;

}


int main(){
	vector <int> input={3,2,1};
	countSwaps(input);
	
}
