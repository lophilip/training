//hakerrank nation bank sorting

#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;


vector<int> counting_sort(vector <int> sort, int max){
	vector <int> count(max+1);
	vector <int> rsum (max+1);
	vector <int> sorted(sort.size());

	fill(count.begin(),count.end(),0);
	fill(rsum.begin(),rsum.end(),0);
	fill(sorted.begin(),sorted.end(),0);

	//first do count
	for (int x=0;x<sort.size();x++){
		count[sort[x]]++;		
	}
	rsum=count;

	//do running sum
	for (int x=1;x<rsum.size();x++)
		rsum[x]+=rsum[x-1];
	
	//fill out sorted array
	for (int i=sort.size()-1; i>=0; i--){		
		sorted[rsum[sort[i]]-1]=sort[i];
		rsum[sort[i]]--;
	}

	return sorted;
	
}

vector <int> make_frequency_table(vector <int> data,int max){
	vector <int> count(max+1);

	fill(count.begin(),count.end(),0);

	for (long x=0; x<data.size(); x++)
		count[data[x]]++;
	
	return count;	
	
}

vector <int> update_frequency_table(vector <int> data, int add, int ndel){
	vector <int> output=data;

	output[add]++;
	if (output[ndel]>0)
		output[ndel]--;

	return output;
}

double get_median_frequency_table(vector<int>freqtbl, int window_size){
	bool odd=false;
	int median_index1=0;
	int median_index2=0;
	int value1=0;
	int value2=0;

	double median;

	if (window_size%2)
        	odd=true;

	median_index1=window_size/2;
	if (odd==false)
		median_index2=median_index1+1;

	int index_sum1=0;
	int index_sum2=0;
	int i=0;
	int j=0;
	while (index_sum1<=median_index1 || index_sum2<=median_index2){
		index_sum1+=freqtbl[i];
		index_sum2+=freqtbl[j];
		if (index_sum1<=median_index1)
			i++;
		if (index_sum2<=median_index2)
			j++;
	}
	value1=i;
	value2=j;

	if (odd)
		median=value1;
	else
		median=(value1+value2)/2.0;

	return median;

}



int activityNotifications(vector<int> expenditure, int d) {
    
    int alarm=0;
    int total_exp=0;
    double median;
    vector<int> freqtbl(201);
    bool tblgen=false;
    

        
    for (int x=0; x+d<expenditure.size(); x++){

	if (tblgen==false){
	        vector <int> subset={};
        		for (int j=x; j<expenditure.size() && j<(x+d); j++){
		            subset.push_back(expenditure[j]);			   
        		}
			
			freqtbl=make_frequency_table(subset,200);
			tblgen=true;
	}else{
		freqtbl=update_frequency_table(freqtbl,expenditure[x+d-1],expenditure[x-1]);
	}
	
        
        median=get_median_frequency_table(freqtbl,d);
        total_exp=expenditure[x+d];
	            
                    
        if (total_exp>=(2*median))
	        alarm++;
        
    }
    return alarm;
}





int main(){

	//vector <int> exp{2,3,4,2,3,6,8,4,5};
	//int d = 5;
	//vector <int> exp{1,2,3,4,4};
	//int d =4;
	vector <int> exp{10,20,30,40,50};
	int d =3;
	cout<<activityNotifications(exp,d)<<endl;
	return 0;

}
