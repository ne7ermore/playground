//from word2vec

# include <vector>
#include <iostream>

using namespace std;

struct HMNode
{
    int count, codelen;
    int *point, *code; 
};

struct HMNode *tree;

const int MAX_CODE_LENGTH = 10;

void CreateTree(vector<int> cns) {
    int size = cns.size(), a;
    sort(cns.begin(), cns.end(), greater<int>());
    vector<int> counts(size*2-1, INT_MAX);
    int *parents = (int *)calloc((size*2-1), sizeof(int));
    int *binary = (int *)calloc((size*2-1), sizeof(int));
    for (a = 0; a < size; a++) counts[a] = cns[a];

    int min1i, min2i, pos1 = size-1, pos2 = size;

    for (a = 0; a < size; a++) {
        if (pos1 >= 0) {
            if (counts[pos1] < counts[pos2]) {
                min1i = pos1;
                pos1--;
            } else {
                min1i = pos2;
                pos2++;
            }
        } else {
            min1i = pos2;
            pos2++;
        }

        if (pos1 >= 0) {
            if (counts[pos1] < counts[pos2]) {
                min2i = pos1;
                pos1--;
            } else {
                min2i = pos2;
                pos2++;
            }
        } else {
            min2i = pos2;
            pos2++;
        }
        counts[size+a] = counts[min1i] + counts[min2i];
        parents[min1i] = size+a;
        parents[min2i] = size+a;
        binary[min2i] = 1;
    }

    tree = (HMNode *)realloc(tree, size*sizeof(struct HMNode));
    int b, i;
    int code[MAX_CODE_LENGTH], point[MAX_CODE_LENGTH];
    for (a = 0; a < size; a++) {
        tree[a].count = counts[a];
        b = a;
        i = 0;
        tree[a].point = (int *)calloc(MAX_CODE_LENGTH, sizeof(int));
        tree[a].code = (int *)calloc(MAX_CODE_LENGTH, sizeof(int));
        while(1) {
            code[i] = binary[b];
            point[i] = b;
            b = parents[b];
            i++;
            if (b == 2*size-1) break;
        }
        tree[a].point[0] = size-1;
        tree[a].codelen = i;
        for (b = 0; b < i; b++) {
            tree[a].code[i-b-1] = code[b];
            tree[a].point[i-b] = point[b]-size;
        }
    }
    free(parents);
    free(binary);
}

