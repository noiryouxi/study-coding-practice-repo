#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

    ll d; cin >> d;
    ll ten[18]; ten[0]=1;
    for (int i = 1; i < 18; i++) ten[i] = ten[i-1] * 10;

    for (int i = 2; i <= 18; i++) {
        int n = (i/2);
        vector<ll> ten1;
        vector<ll> v1;
        ll t = d;
        for (int j = 0; j < n; j++) {
            ten1.push_back((ten[i-j-1]-ten[j]) / ten[j]);
        }
        for (int j = 0; j < n; j++) {
            int a;
            if (t >= 0) a = (10-t%10)%10;
            else a = (-10-t%10)%10;
            v1.push_back(a);
            t = (t - a * ten1[j])/10;
        }
        if (t == 0) {
            ll ans = 0;
            for (int j = 0; j < n; j++) {
                if (v1[j] == 0 && j == 0) ans += ten[i-1]+ten[0];
                if (v1[j] > 0) ans += (ten[i-1-j] * v1[j]);
                if (v1[j] < 0) ans -= (ten[j] * v1[j]);
            }
            cout << ans;
            return 0;
        }
    }
    cout << "-1";
}
