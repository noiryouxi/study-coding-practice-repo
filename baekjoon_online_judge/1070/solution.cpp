#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = (ll)4e18;

struct Edge {
    int to;
    ll cap;
    int rev;
};

struct Dinic {
    int N;
    vector<vector<Edge>> G;
    vector<int> level, it;

    Dinic(int n) : N(n), G(n), level(n), it(n) {}

    void addEdge(int u, int v, ll cap) {
        G[u].push_back({v, cap, (int)G[v].size()});
        G[v].push_back({u, 0, (int)G[u].size() - 1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        level[s] = 0;
        q.push(s);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto &e : G[u]) {
                if (e.cap > 0 && level[e.to] < 0) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] >= 0;
    }

    ll dfs(int u, int t, ll f) {
        if (u == t) return f;
        for (int &i = it[u]; i < (int)G[u].size(); i++) {
            auto &e = G[u][i];
            if (e.cap > 0 && level[e.to] == level[u] + 1) {
                ll ret = dfs(e.to, t, min(f, e.cap));
                if (ret > 0) {
                    e.cap -= ret;
                    G[e.to][e.rev].cap += ret;
                    return ret;
                }
            }
        }
        return 0;
    }

    ll maxFlow(int s, int t) {
        ll flow = 0;
        while (bfs(s, t)) {
            fill(it.begin(), it.end(), 0);
            while (true) {
                ll f = dfs(s, t, INF);
                if (!f) break;
                flow += f;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<string> grid(N);
    for (int i = 0; i < N; i++) cin >> grid[i];

    vector<ll> cost(26);
    for (int i = 0; i < 26; i++) cin >> cost[i];

    const ll K = (ll)1e12; // 충분히 큰 값
    auto id = [&](int r, int c, int inout) {
        return (r * M + c) * 2 + inout;
    };

    int S = 2 * N * M;
    int T = S + 1;
    Dinic dinic(T + 1);

    int dr[4] = {1, -1, 0, 0};
    int dc[4] = {0, 0, 1, -1};

    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            char ch = grid[r][c];
            if (ch == '-') continue;

            int in = id(r, c, 0);
            int out = id(r, c, 1);

            if (ch == '*') {
                dinic.addEdge(in, out, INF);
                dinic.addEdge(out, T, INF);
            } else {
                ll w = K + cost[ch - 'A'];
                dinic.addEdge(in, out, w);
            }

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                if (grid[nr][nc] == '-') continue;
                dinic.addEdge(out, id(nr, nc, 0), INF);
            }

            if (r == 0 || r == N - 1 || c == 0 || c == M - 1) {
                dinic.addEdge(S, in, INF);
            }
        }
    }

    ll result = dinic.maxFlow(S, T);
    cout << (result % K) << "\n";
    return 0;
}