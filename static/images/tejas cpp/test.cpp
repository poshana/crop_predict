// {} Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++
class Solution{
	public:
	int count(int N)
	{
	    int c=0;
		//write your code here
		for (int X=N; X>0;X--){
		    if(X&N>0){
		        c++;
		    }
		}
		return c;
	}
};

// { Driver Code Starts.

int main() {
 int t=1;
 cin>>t;
 for(int i=1;i<=t;i++){
   int N;
   cin>>N;
   Solution obj;
   int ans=obj.count(N);
   cout << ans << "\n";
 }
}
  // } Dri
