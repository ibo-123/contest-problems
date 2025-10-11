#include<iostream>
using namespace std;

int main(){
   short int x;
   cin>>x;
   for(int i=0;i<x;i++){
        string y;
        short int a=0,b=0;
        cin>>y;
        for(int j=0;j<5;j++){
                if(y[j]=='A'){
                        a++;
                }
                else b++;
        }
        if (a>b){
                cout<<"A\n";
        }
        else cout<<"B\n";
   }
}