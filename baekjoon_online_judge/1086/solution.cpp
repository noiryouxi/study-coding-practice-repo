#include <bits/stdc++.h>
using namespace std;

long long dp[1<<15][100];
int N, K;
string nums[15];
int lenArr[15];
int modArr[15];
int pow10mod[51];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for(int i=0;i<N;i++){
        cin >> nums[i];
        lenArr[i] = nums[i].size();
    }
    cin >> K;

    for(int i=0;i<N;i++){
        int r=0;
        for(char c: nums[i])
            r = (r*10 + (c-'0')) % K;
        modArr[i]=r;
    }

    pow10mod[0]=1%K;
    for(int i=1;i<=50;i++)
        pow10mod[i]=(pow10mod[i-1]*10)%K;

    dp[0][0]=1;

    for(int mask=0;mask<(1<<N);mask++){
        for(int r=0;r<K;r++){
            if(dp[mask][r]==0) continue;
            for(int i=0;i<N;i++){
                if(mask&(1<<i)) continue;
                int nmask=mask|(1<<i);
                int nr=(r*pow10mod[lenArr[i]]+modArr[i])%K;
                dp[nmask][nr]+=dp[mask][r];
            }
        }
    }

    long long numerator=dp[(1<<N)-1][0];

    long long denominator=1;
    for(int i=1;i<=N;i++) denominator*=i;

    if(numerator==0){
        cout<<"0/1";
        return 0;
    }

    long long g=gcd(numerator,denominator);
    cout<<numerator/g<<"/"<<denominator/g;
}