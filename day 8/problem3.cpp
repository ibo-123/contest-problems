#include<iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
     long long x, a, b, c, total;
    cin >> x;
    for (int i = 0; i < x; i++)
    {
        cin >> a >> b >> c;
        total=c-((c-b)%a);
        cout << total << endl;
    }
}