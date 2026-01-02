#include <iostream>
#include <algorithm>
#include <vector>
static const auto fastio = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
using namespace std;
typedef struct Tree {
    int y, x, v, n;
} tree;
bool cmp1 (tree a, tree b) {
    if (b.v < a.v) return true;
    else return false;
}
bool cmp2 (tree a, tree b) {
    if (a.y < b.y) return true;
    else return false;
}
bool cmp3 (tree a, tree b) {
    if (a.x < b.x) return true;
    else return false;
}
int n, res = 100000;
vector<tree> fence, yfence, xfence;
vector<bool> repeated;
int main() { 
    cin >> n;
    fence = vector<tree>(n);
    xfence = vector<tree>(n);
    yfence = vector<tree>(n);
    for (int i = 0; i < n; i++) cin >> fence[i].y >> fence[i].x >> fence[i].v;
    sort(fence.begin(), fence.end(), cmp1);
    for (int i = 0; i < n; i++) fence[i].n = i;
    for (int i = 0; i < n; i++) yfence[i] = xfence[i] = fence[i];
    sort(yfence.begin(), yfence.end(), cmp2);
    sort(xfence.begin(), xfence.end(), cmp3);
    for (int right = n - 1; right >= 0; right--) {
        for (int left = 0; left <= right; left++) {
            for (int high = n - 1; high >= 0; high--) {
                for (int low = 0; low <= high; low++) {
                    
                    int length = 0, cnt = 0;
                    repeated = vector<bool>(n);
                    for (int i = right + 1; i < n; i++) repeated[yfence[i].n] = true;
                    for (int i = left - 1; i >= 0; i--) repeated[yfence[i].n] = true;
                    for (int i = high + 1; i < n; i++) repeated[xfence[i].n] = true;
                    for (int i = low - 1; i >= 0; i--) repeated[xfence[i].n] = true;
                    
                    for (int i = 0; i < n; i++) {
                        if (repeated[i]) {
                            length += fence[i].v;
                            cnt++;
                        }
                    }
                    int fenceLength = ((yfence[right].y - yfence[left].y) + (xfence[high].x - xfence[low].x)) * 2;
                    for (int i = 0; i < n; i++) {
                        if (fenceLength <= length) break;
                        if (repeated[i]) continue;
                        length += fence[i].v;
                        cnt++;
                    }
                    if (fenceLength <= length) res = min(res, cnt);
                }
            }
        }
    }
    cout << res;
    return 0;
}