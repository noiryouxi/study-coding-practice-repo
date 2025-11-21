#include <iostream>
using namespace std;

// 0과 1의 출현 횟수를 저장하는 구조체
struct Count {
    int zero;
    int one;
};

int main() {
    int T;
    cin >> T;

    // N은 최대 40이므로 DP 배열 크기를 41로 설정
    Count dp[41];

    // 초기값 설정
    dp[0] = {1, 0}; // fibonacci(0)은 0을 1번 출력, 1을 0번 출력
    dp[1] = {0, 1}; // fibonacci(1)은 0을 0번 출력, 1을 1번 출력

    // DP 계산
    for (int i = 2; i <= 40; i++) {
        // fibonacci(i)의 0 출력 횟수 = fibonacci(i-1)의 0 + fibonacci(i-2)의 0
        dp[i].zero = dp[i-1].zero + dp[i-2].zero;
        // fibonacci(i)의 1 출력 횟수 = fibonacci(i-1)의 1 + fibonacci(i-2)의 1
        dp[i].one = dp[i-1].one + dp[i-2].one;
    }

    // 각 테스트 케이스 처리
    while (T--) {
        int N;
        cin >> N;
        cout << dp[N].zero << " " << dp[N].one << "\n";
    }

    return 0;
}