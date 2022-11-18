#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maximumToys(vector<int> prices, int k) {

	vector<int>sorted_p=prices;

	sort(sorted_p.begin(),sorted_p.end());

	int cost=0;
	int item=0;

	for (int i=0;i<sorted_p.size();i++){
		if ((cost+sorted_p[i])<k){
			cost+=sorted_p[i];
			item++;
		}else
			break;
	}

	return item;


}

int main(){
	vector <int> prices={1,2,3,4};
	int k=7;
	cout<<maximumToys(prices,k)<<endl;
	return 0;
}
