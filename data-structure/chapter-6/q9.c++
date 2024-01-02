#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

int charToNum(char c) {
    return c - 'a';
}

int main() {
    int N;
    std::cin >> N;
    std::vector<std::string> S(N);
    for (int i = 0; i < N; i++) {
        std::cin >> S[i];
    }

    std::unordered_map<std::string, int> counter;

    for (const auto& word : S) {
        std::vector<int> used_char_count(26, 0);
        for (const auto& c : word) {
            int char_num = charToNum(c);
            used_char_count[char_num]++;
        }
        std::string key;
        for (const auto& count : used_char_count) {
            key += std::to_string(count);
        }
        counter[key]++;
    }

    double bottom = static_cast<double>(N) * (N - 1);
    double top = 0;
    for (const auto& pair : counter) {
        top += static_cast<double>(pair.second) * (pair.second - 1);
    }
    std::cout << top / bottom << std::endl;

    return 0;
}