#include <iostream>

// 재귀 함수를 사용하여 팩토리얼 계산
unsigned long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int n;

    std::cout << "양의 정수를 입력하세요: ";
    std::cin >> n;

    if (n < 0) {
        std::cout << "음수의 팩토리얼은 정의되지 않습니다." << std::endl;
    } else {
        unsigned long long result = factorial(n);
        std::cout << n << "의 팩토리얼은 " << result << " 입니다." << std::endl;
    }

    return 0;
}
