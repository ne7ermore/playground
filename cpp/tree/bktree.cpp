#include <string>
#include <unordered_map>
#include <iostream>
#include <vector>
#include <cstring>
#include <queue>

namespace BkTree {
    struct node {
        node() : item() {};
        node(std::string str) : item(str) {};
        std::string item;
        std::pair<std::string, std::unordered_map<int, node *>> children;
    };

    class tree {
        public:
            int edit_distance(std::string, std::string);
            node* get_root(); 
            void add(std::string);
            vector<pair<std::string, int>> search(std::string, int);
        private:
            struct node *root;
    }

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
                    int tmp = min(dp[i - 1][j], dp[i - 1][j - 1]);
                    dp[i][j] = min(tmp, dp[i][j - 1]) + 1;
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
            node->item = str;
            return;
        }
        while (1) {
            int d = edit_distance(node->item, str);
            auto search = node->children.find(d);
            if (search != node->children.end()) {
                n = search->second;
            } else {
                node->children[d] = new node(str);
                return;
            }
        }
    }

    vector<pair<std::string, int>> search(std::string item, int n) {
        vector<pair<std::string, int>> res;
        if (root->item.size() == 0) {
            return res;
        }

        std::queue<node *> q;
        q.push(root);
        while (q.size()) {
            node *n = q.front();
            q.pop();

            int d = edit_distance(n->item, item);
            if (d <= n) res.push(pair<std::string, int>(n->item, d));
            for (auto c: n->children) if (c->first >= d-n and c->first <= d+n) q.push(n->second);
            sort
        }
    }    


    template<typename T>;

    bool compare(const T &t1, const T &t2) {
        return t1.second < t2.second;
    }
}

int main() {
    using namespace BkTree;
    BkTree::node n("asd");
    std::cout << n.item.size();
    return 0;
}