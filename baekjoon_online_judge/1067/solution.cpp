#include <bits/stdc++.h>
using namespace std;

using cd = complex<long double>;
const long double PI = acosl(-1);

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j |= bit;
        if (i < j) swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        long double ang = 2 * PI / len * (invert ? -1 : 1);
        cd wlen(cosl(ang), sinl(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1);
            for (int j = 0; j < len/2; j++) {
                cd u = a[i+j];
                cd v = a[i+j+len/2] * w;
                a[i+j] = u + v;
                a[i+j+len/2] = u - v;
                w *= wlen;
            }
        }
    }

    if (invert) {
        for (cd & x : a)
            x /= n;
    }
}

vector<long long> multiply(const vector<long long> &a,
                           const vector<long long> &b) {
    vector<cd> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < (int)a.size() + (int)b.size()) n <<= 1;
    fa.resize(n);
    fb.resize(n);
    fft(fa, false);  fft(fb, false);
    for (int i = 0; i < n; i++)
        fa[i] *= fb[i];
    fft(fa, true);

    vector<long long> result(n);
    for (int i = 0; i < n; i++)
        result[i] = (long long)(fa[i].real() + 0.5);
    return result;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<long long> X(2*N), Y(N);

    for (int i = 0; i < N; i++) {
        cin >> X[i];
        X[i+N] = X[i];
    }
    for (int i = 0; i < N; i++)
        cin >> Y[i];

    reverse(Y.begin(), Y.end());

    auto conv = multiply(X, Y);

    long long ans = 0;
    for (int i = N-1; i <= 2*N-1; i++)
        ans = max(ans, conv[i]);

    cout << ans << "\n";
}