#include<iostream>
using namespace std;

int main(){
        int x,y,z,w,ma;
        cin>>x;
        for(int i=0;i<x;i++){
               cin>>y;
               w=0;
               ma=0;
               for(int j=0;j<y;j++){
                  cin>>z;
                  if(z==1){
                        if (w>ma){
                                ma=w;
                                w=0;
                        }
                        w=0;
                  }
                  else if(z==0){
                        w++;
                  }
               }
               if (w>ma){
                  ma=w;
               }
               cout<<ma<<endl; 
        }
}