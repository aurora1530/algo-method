#include <iostream>
#include <vector>
#include <string>
#include <cmath>

const int B = 30;
const int M = 1000003;

struct Node {
    std::string val;
    Node* nex;
    Node(std::string x = "") : val(x), nex(nullptr) {}
};

std::vector<Node*> table(M, new Node());

int charToNumber(char c) {
    return c - 'a' + 1;
}

int rolling_hash(std::string word) {
    int result = 0;
    int word_l = word.length();
    for (int i = 0; i < word_l; i++) {
        result += charToNumber(word[word_l - 1 - i]) * pow(B, i);
    }
    return result % M;
}

int main() {
    int Q;
    std::cin >> Q;
    std::cin.ignore();

    for (int i = 0; i < M; i++) {
        Node* nil = new Node();
        nil->nex = nil;
        table[i] = nil;
    }

    for (int i = 0; i < Q; i++) {
        std::string line;
        std::getline(std::cin, line);
        std::string query = line.substr(0, 1);
        std::string T = line.substr(2);

        if (query == "0") {
            int hx = rolling_hash(T);
            Node* insert_node = new Node(T);
            Node* current_table_node = table[hx];
            insert_node->nex = current_table_node->nex;
            current_table_node->nex = insert_node;
        } else if (query == "1") {
            int hx = rolling_hash(T);
            Node* now_node = table[hx];
            while (true) {
                if (now_node->nex->val == T) {
                    Node* target_node = now_node->nex;
                    now_node->nex = target_node->nex;
                    break;
                } else {
                    now_node = now_node->nex;
                }
                if (now_node->nex == now_node) {
                    break;
                }
            }
        } else {
            int hx = rolling_hash(T);
            Node* now_node = table[hx];
            while (true) {
                if (now_node->nex->val == T) {
                    std::cout << "Yes" << std::endl;
                    break;
                } else {
                    now_node = now_node->nex;
                }
                if (now_node->nex->val == "") {
                    std::cout << "No" << std::endl;
                    break;
                }
            }
        }
    }

    return 0;
}