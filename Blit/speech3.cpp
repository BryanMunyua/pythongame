#include <iostream>
using namespace std;

int factorial (int a);

int main()

{
	int x;
	
	cout << "Enter a number: ";
		cin>> x;
		
	 factorial(x);
	 

return 0;	
}
	 int factorial (int a)
	{
		
		if (a>1){
			
		int product = 1;
		for (int n=a ; n>0 ; n--){
			
			product = product * n;
			
			if (n == 1){
				cout << "The factorial is: "<< product;
			}
		} 
		
		}
		else{
			cout<<1;
			
		}

	}
