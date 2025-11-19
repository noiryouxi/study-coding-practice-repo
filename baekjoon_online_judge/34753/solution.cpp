#include <bits/stdc++.h>
using namespace std;

static long long A[1501][1501];
static long long remain_cost[3005];
static bool done[3005];

int N;

struct Node {
    long long cost;
    int type;
    int num;
    int id;
    bool operator<(Node const& other) const {
        if (cost != other.cost) return cost > other.cost;  // min-heap
        if (type != other.type) return type > other.type;
        return num > other.num;
    }
};

pair<int,int> lineOrder(int lid, int N){
    if (lid < N) return {0, lid};           // row
    else if (lid < 2*N) return {1, lid-N};  // col
    else if (lid == 2*N) return {2, 0};     // diag
    else return {3, 0};                     // anti
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> A[i][j];
        }
    }

    int ROW = 0;
    int COL = N;
    int DIA = 2*N;
    int ADI = 2*N+1;
    int total_lines = 2*N + 2;

    // 초기 남은 비용 계산
    for(int i=0;i<N;i++){
        long long s=0;
        for(int j=0;j<N;j++) s += A[i][j];
        remain_cost[ROW+i] = s;
    }
    for(int j=0;j<N;j++){
        long long s=0;
        for(int i=0;i<N;i++) s += A[i][j];
        remain_cost[COL+j] = s;
    }
    long long s=0;
    for(int i=0;i<N;i++) s += A[i][i];
    remain_cost[DIA] = s;
    s=0;
    for(int i=0;i<N;i++) s += A[i][N-1-i];
    remain_cost[ADI] = s;

    priority_queue<Node> pq;
    for(int lid=0; lid<total_lines; lid++){
        auto o = lineOrder(lid, N);
        pq.push({remain_cost[lid], o.first, o.second, lid});
    }

    vector<long long> ans(total_lines+1);
    long long cur_time = 0;
    int bingo = 0;

    while (bingo < total_lines){
        Node nd;
        do {
            nd = pq.top(); pq.pop();
        } while(done[nd.id] || nd.cost != remain_cost[nd.id]);

        int lid = nd.id;
        done[lid] = true;

        cur_time += remain_cost[lid];
        bingo++;
        ans[bingo] = cur_time;

        // 해당 줄 완성 → 포함된 모든 칸의 값만큼 다른 줄 감소
        if (lid < COL){ // row
            int i = lid;
            for(int j=0;j<N;j++){
                long long val = A[i][j];
                if(val == 0) continue;
                A[i][j] = 0;
                // row
                if(!done[ROW+i]){
                    remain_cost[ROW+i] -= val;
                    auto o = lineOrder(ROW+i,N);
                    pq.push({remain_cost[ROW+i], o.first, o.second, ROW+i});
                }
                // col
                if(!done[COL+j]){
                    remain_cost[COL+j] -= val;
                    auto o = lineOrder(COL+j,N);
                    pq.push({remain_cost[COL+j], o.first, o.second, COL+j});
                }
                // diag
                if(i == j){
                    if(!done[DIA]){
                        remain_cost[DIA] -= val;
                        auto o = lineOrder(DIA,N);
                        pq.push({remain_cost[DIA], o.first, o.second, DIA});
                    }
                }
                // anti
                if(i + j == N-1){
                    if(!done[ADI]){
                        remain_cost[ADI] -= val;
                        auto o = lineOrder(ADI,N);
                        pq.push({remain_cost[ADI], o.first, o.second, ADI});
                    }
                }
            }
        }
        else if (lid < DIA){ // col
            int j = lid - COL;
            for(int i=0;i<N;i++){
                long long val = A[i][j];
                if(val == 0) continue;
                A[i][j] = 0;
                if(!done[ROW+i]){
                    remain_cost[ROW+i] -= val;
                    auto o = lineOrder(ROW+i,N);
                    pq.push({remain_cost[ROW+i], o.first, o.second, ROW+i});
                }
                if(!done[COL+j]){
                    remain_cost[COL+j] -= val;
                    auto o = lineOrder(COL+j,N);
                    pq.push({remain_cost[COL+j], o.first, o.second, COL+j});
                }
                if(i == j){
                    if(!done[DIA]){
                        remain_cost[DIA] -= val;
                        auto o = lineOrder(DIA,N);
                        pq.push({remain_cost[DIA], o.first, o.second, DIA});
                    }
                }
                if(i + j == N-1){
                    if(!done[ADI]){
                        remain_cost[ADI] -= val;
                        auto o = lineOrder(ADI,N);
                        pq.push({remain_cost[ADI], o.first, o.second, ADI});
                    }
                }
            }
        }
        else if (lid == DIA){
            for(int i=0;i<N;i++){
                int j=i;
                long long val = A[i][j];
                if(val == 0) continue;
                A[i][j] = 0;
                if(!done[ROW+i]){
                    remain_cost[ROW+i] -= val;
                    auto o = lineOrder(ROW+i,N);
                    pq.push({remain_cost[ROW+i], o.first, o.second, ROW+i});
                }
                if(!done[COL+j]){
                    remain_cost[COL+j] -= val;
                    auto o = lineOrder(COL+j,N);
                    pq.push({remain_cost[COL+j], o.first, o.second, COL+j});
                }
                if(!done[DIA]){
                    remain_cost[DIA] -= val;
                    auto o = lineOrder(DIA,N);
                    pq.push({remain_cost[DIA], o.first, o.second, DIA});
                }
                if(i + j == N-1){
                    if(!done[ADI]){
                        remain_cost[ADI] -= val;
                        auto o = lineOrder(ADI,N);
                        pq.push({remain_cost[ADI], o.first, o.second, ADI});
                    }
                }
            }
        }
        else { // ADI
            for(int i=0;i<N;i++){
                int j = N-1-i;
                long long val = A[i][j];
                if(val == 0) continue;
                A[i][j] = 0;
                if(!done[ROW+i]){
                    remain_cost[ROW+i] -= val;
                    auto o = lineOrder(ROW+i,N);
                    pq.push({remain_cost[ROW+i], o.first, o.second, ROW+i});
                }
                if(!done[COL+j]){
                    remain_cost[COL+j] -= val;
                    auto o = lineOrder(COL+j,N);
                    pq.push({remain_cost[COL+j], o.first, o.second, COL+j});
                }
                if(i == j){
                    if(!done[DIA]){
                        remain_cost[DIA] -= val;
                        auto o = lineOrder(DIA,N);
                        pq.push({remain_cost[DIA], o.first, o.second, DIA});
                    }
                }
                if(!done[ADI]){
                    remain_cost[ADI] -= val;
                    auto o = lineOrder(ADI,N);
                    pq.push({remain_cost[ADI], o.first, o.second, ADI});
                }
            }
        }
    }

    for(int i=1;i<=total_lines;i++){
        cout << ans[i] << "\n";
    }
}