#include <bits/stdc++.h>
using namespace std;

static const long long MOD = 1'000'000'007;

string S;
int N, M;

vector<pair<string, string>> codons; // (DNA codon, amino acid)

// pos[c][i] : i 이상에서 문자 c가 처음 나오는 위치
int pos[4][2501];

// dp[i] : i부터 시작해서 만들 수 있는 서로 다른 단백질 개수
long long dp[2501];

int idx(char c) {
    if (c == 'A') return 0;
    if (c == 'C') return 1;
    if (c == 'G') return 2;
    return 3; // T
}

void precompute_pos() {
    memset(pos, -1, sizeof(pos));
    for (int i = 0; i < N; i++) {
        int mask = 0;
        for (int j = i; j < N && mask != 15; j++) {
            int c = idx(S[j]);
            if (!(mask & (1 << c))) {
                mask |= (1 << c);
                pos[c][i] = j;
            }
        }
    }
}

// idx부터 codon을 부분수열로 만들 수 있으면 다음 위치 반환
int next_index(int idx0, const string &codon) {
    for (int i = 0; i < 3; i++) {
        if (idx0 >= N) return -1;
        int p = pos[idx(codon[i])][idx0];
        if (p == -1) return -1;
        idx0 = p + 1;
    }
    return idx0;
}

long long solve(int start) {
    if (start >= N) return 0;
    long long &ret = dp[start];
    if (ret != -1) return ret;
    ret = 0;

    string last_amino = "";
    int best_next = -1;

    for (auto &[dna, amino] : codons) {
        if (amino != last_amino) {
            if (!last_amino.empty() && best_next != -1) {
                ret = (ret + 1 + solve(best_next)) % MOD;
            }
            last_amino = amino;
            best_next = -1;
        }

        int nxt = next_index(start, dna);
        if (nxt != -1) {
            if (best_next == -1 || nxt < best_next)
                best_next = nxt;
        }
    }

    if (!last_amino.empty() && best_next != -1) {
        ret = (ret + 1 + solve(best_next)) % MOD;
    }

    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> S;
    N = S.size();

    cin >> M;
    codons.resize(M);
    for (auto &p : codons)
        cin >> p.first >> p.second;

    sort(codons.begin(), codons.end(),
         [](auto &a, auto &b) {
             return a.second < b.second;
         });

    memset(dp, -1, sizeof(dp));
    precompute_pos();

    cout << solve(0) << '\n';
    return 0;
}