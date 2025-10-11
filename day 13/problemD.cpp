#include<iostream>
using namespace std;

int main(){
         int x, y , m, n;
        cin>>x;
        for(int i=0;i<x;i++){
                bool z = false,l=true;
                y=2;
                cin >> n;
                while(n--)
                {
                        cin >> m;
                        if (y == m)
                        {
                                z = false;
                                l=false;
                                
                        }
                        else
                        {
                                if (m == 0) y = m;
                                else y=2;

                        }
                        if (y==0 && l) z=true;
                }
                        if (!z) cout << "YES\n";
                        else  cout << "NO\n";

        }
}