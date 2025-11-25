#include <bits/stdc++.h>
using namespace std;

int N;
pair<long long, long long> p[22];
bool visited[22];
long long sx, sy;  // sum of all points

double answer;

void dfs(int idx, int cnt, int target) {
    if (cnt == target) {
        long long vx = sx, vy = sy;

        for (int i = 0; i < N; i++) {
            if (visited[i]) {
                vx -= 2 * p[i].first;
                vy -= 2 * p[i].second;
            }
        }

        double val = sqrt((long double)vx * vx + (long double)vy * vy);
        answer = min(answer, val);
        return;
    }

    if (idx == N) return;

    // 선택하는 경우
    visited[idx] = true;
    dfs(idx + 1, cnt + 1, target);

    // 선택하지 않는 경우
    visited[idx] = false;
    dfs(idx + 1, cnt, target);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        cin >> N;
        sx = sy = 0;

        for (int i = 0; i < N; i++) {
            cin >> p[i].first >> p[i].second;
            sx += p[i].first;
            sy += p[i].second;
        }

        answer = 1e100;

        // 대칭 제거: 첫 번째 점을 반드시 S에 포함시키기
        memset(visited, false, sizeof(visited));
        visited[0] = true;

        dfs(1, 1, N / 2); // 첫 점을 포함했으므로 1개 선택된 상태에서 시작

        cout << fixed << setprecision(12) << answer << "\n";
    }
    return 0;
}