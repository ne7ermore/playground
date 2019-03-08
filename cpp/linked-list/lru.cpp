/**
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2);

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
 * **/

#include <unordered_map>

using namespace std;

struct LRUNode
{
    LRUNode(int key, int val) : k(key), val(val), next(0), prev(0) {}
    int k, val;
    LRUNode *next;
    LRUNode *prev;
};

class LRUCache
{
  public:
    LRUCache(int capacity)
    {
        cap = capacity;
        head->next = tail;
        tail->prev = head;
    }

    int get(int key)
    {
        if (mappings.count(key))
        {
            del(mappings[key]);
            add(mappings[key]);
            return mappings[key]->val;
        }
        else
            return -1;
    }

    void put(int key, int value)
    {
        if (mappings.count(key))
        {
            mappings[key]->val = value;
            del(mappings[key]);
            add(mappings[key]);
        }
        else
        {
            LRUNode *newNode = new LRUNode(key, value);
            add(newNode);
            mappings[key] = newNode;
            if (cap == 0)
            {
                mappings.erase(tail->prev->k);
                del(tail->prev);
            }
            else
            {
                cap--;
            }
        }
    }

  private:
    unordered_map<int, LRUNode *> mappings;
    LRUNode *head = new LRUNode(0, 0);
    LRUNode *tail = new LRUNode(0, 0);
    int cap;

    void add(LRUNode *node)
    {
        LRUNode *nxtNode = head->next;
        head->next = node;
        node->prev = head;
        nxtNode->prev = node;
        node->next = nxtNode;
    }
    void del(LRUNode *node)
    {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
};