#include <string>
#include <unordered_map>
#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
#include <algorithm>

namespace BkTree {
    struct node {
        node() : item() {};
        node(std::string str) : item(str) {};
        std::string item;
        std::pair<std::string, std::unordered_map<int, node *>> children;
    };

    class tree {
        public:
            tree() : root() {};
            int edit_distance(std::string, std::string);
            node* get_root(); 
            void add(std::string);
            std::vector<std::pair<int, std::string>> search(std::string, int);
        private:
            struct node *root;
    };

    int tree::edit_distance(std::string str1, std::string str2) {
        int n = str1.size(), m = str2.size();
        int dp[n + 1][m + 1];
        for (int i = 0; i <= n; i++) dp[i][0] = i;
        for (int i = 0; i <= m; i++) dp[0][i] = i;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                if (str1[i - 1] == str2[j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                else
                {
                    int tmp = std::min(dp[i - 1][j], dp[i - 1][j - 1]);
                    dp[i][j] = std::min(tmp, dp[i][j - 1]) + 1;
                }
            }
        }
        return dp[n][m];        
    }

    node* tree::get_root() {
        return root;
    }

    void tree::add(std::string str) {
        node *n = root;
        if (n->item.size() == 0) {
            n->item = str;
            return;
        }
        while (1) {
            int d = edit_distance(n->item, str);
            auto search = n->children.second.find(d);
            if (search != n->children.second.end()) {
                n = search->second;
            } else {
                n->children.second[d] = new node(str);
                return;
            }
        }
    }

    std::vector<std::pair<int, std::string>> tree::search(std::string item, int value) {
        std::vector<std::pair<int, std::string>> res;
        if (root->item.size() == 0) {
            return res;
        }

        std::queue<node *> q;
        q.push(root);
        while (q.size()) {
            node *n = q.front();
            q.pop();

            int d = edit_distance(n->item, item);
            if (d <= value) res.push_back(make_pair(d, n->item));
            for (auto c: n->children.second) if (c.first >= d-value and c.first <= d+value) q.push(c.second);
        }

        sort(res.begin(), res.end());
        return res;        
    }    
}

int main() {
    using namespace BkTree;
    BkTree::tree t;
    t.add("asdasd");
    return 0;
}