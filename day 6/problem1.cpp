#include <bits/stdc++.h>
using namespace std;

int main()
{
        ios::sync_with_stdio(false);
        cin.tie(nullptr);

        int t;
        cin >> t;
        while (t--)
        {
                long long a, b;
                cin >> a >> b;
                long long best = -1;

                // Case 1: k = b
                __int128 m1 = (__int128)a * b; // avoid overflow
                if (m1 <= (__int128)1e18)
                {
                        long long s1 = (long long)(m1 + 1);
                        if (s1 % 2 == 0)
                                best = max(best, s1);
                }

                // Case 2: k = b/2 (only if b even)
                if (b % 2 == 0)
                {
                        __int128 m2 = (__int128)a * (b / 2);
                        if (m2 <= (__int128)1e18)
                        {
                                long long s2 = (long long)(m2 + 2);
                                if (s2 % 2 == 0)
                                        best = max(best, s2);
                        }
                }

                cout << best << "\n";
        }
        return 0;
}
