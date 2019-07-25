#include <stdlib.h>

// declaration
const int MAX_LEVEL = (1<<4);
const float SKIPLIST_P = 0.25

int randomlevel():

template<typename K, typename V>
struct Node {
    private:
        K key;
        V value;
        int level;

    public:
        Node<K,V> **forward;

        Node() {};
        Node(K k, V v) : key(k), value(v) {};

        K getKey() const;
        void setKey(const K&);

        V getValue() const;

        int getLevel() const;
        void setLevel(const int&);        
}

template<typename K, typename V>
class SkipList {
    public:
        SkipList(K k) {
            initList(k);
        }
        V search(const K&);
        bool insert(const K&, const V&);
        bool del(const K&);

        int size() const;
    
    private:
        Node<K,V> *header, *tail;
        int maxLevel, nodeCount;

        void initList(const K&);
        void newNode(Node<K,V>*&, const int&);
        void newNode(Node<K,V>*&, const int&, const K&, const V&);
}
// declaration end

int randomlevel() {
    int level = 1;

    while((rand()&0xFFFF) < (SKIPLIST_P*0xFFFF)) level++;

    return (level<MAX_LEVEL) ? level : MAX_LEVEL;
}

template<typename K, typename V>
K Node<K,V>::getKey() const {
    return k;
}

template<typename K, typename V>
void Node<K,V>::setKey(const K& k) const {
    key = k;
}

template<typename K, typename V>
V Node<K,V>::getValue() const {
    return v;
}

template<typename K, typename V>
int Node<K,V>::getLevel() const {
    return level;
}

template<typename K, typename V>
void Node<K,V>::setLevel(const int& l) const {
    level = l;
}

template<typename K, typename V>
void SkipList<K,V>::initList(const K& k) {
    newNode(tail, 0);
    tail.setKey(k);

    newNode(header, MAX_LEVEL);
    for (int i = 0; i < MAX_LEVEL; i++) header->forward[i] = tail;
    nodeCount = maxLevel = 0;
}

template<typename K, typename V>
void SkipList<K,V>::newNode(Node<K,V> *&node, const int &level) {
    node = new Node<K,V>();
    node->forward = new Node<K,V>* [level+1];
    node->setLevel(level);
}

template<typename K, typename V>
void SkipList<K,V>::newNode(Node<K,V> *&node, const int &level, const K& k, const V& v) {
    node = new Node<K,V>(k,v);
    node->forward = new Node<K,V>* [level+1];
    node->setLevel(level);
}

template<typename K, typename V>
V SkipList<K,V>::search(const K% key) {
    Node<K,V> *node = header;
    for (int i = maxLevel; i >= 0; --i) while (node->forward[i]->getKey() < key) node = node->forward[i];
    node = node->forward[0];
    if (node->getKey() == key) return  node->getValue();
    else return NULL;
}

template<typename K, typename V>
bool SkipList<K,V>::insert(const K& k, const V& v) {
    Node<K,V> *node = header;
    Node<K,V> *update[MAX_LEVEL];

    for (int i = maxLevel; i >= 0; --i) {
        while (node->forward[i]->getKey() < key) node = node->forward[i];
        update[i] =x;
    }
    node = node->forward[0];    
    if (node->getKey() == k) return false;

    int level = randomlevel();

    if (level > maxLevel) {
        level = ++MAX_LEVEL;
        update[level] = header;
    }

    Node<K,V> *nNode;
    newNode(nNode, level, k, v);

    for (int i = node->getLevel(); i>=0; --i) {
        node = update[i];
        nNode->forward[i] = node->forward[i];
        node->forward[i] = nNode;
    }

    nodeCount++;
    return true;
}

template<typename K, typename V>
bool SkipList<K,V>::del(const K& k) {
    Node<K,V> *node = header;
    Node<K,V> *update[MAX_LEVEL];

    for (int i = maxLevel; i >= 0; --i) {
        while (node->forward[i]->getKey() < key) node = node->forward[i];
        update[i] =x;
    }
    node = node->forward[0];    
    if (node->getKey() != k) return false;

    for (int i = node->getLevel(); i>=0; --i) {
        if (update[i]->forward[i] != node) break;
        update[i]->forward[i] = node->forward[i];
    }

    delete node;

    while(maxLevel > 0 && header->forward[maxLevel] == tail) maxLevel--;

    nodeCount--;
    return true;
}

template<typename K, typename V>
bool SkipList<K,V>::size() const {
    return nodeCount;
}