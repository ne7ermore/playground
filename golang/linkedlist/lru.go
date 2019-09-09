package linkedlist

import "sync"

var (
	cache     *lruCache
	cacheOnce sync.Once
)

type lruNode struct {
	key        string
	val        interface{}
	prev, next *lruNode
}

type lruCache struct {
	cap        int
	mappings   map[string]*lruNode
	head, tail *lruNode
}

func GetCache() *lruCache {
	cacheOnce.Do(func() {
		cache = new(lruCache)
		cache.cap = 1000
		cache.head = new(lruNode)
		cache.tail = new(lruNode)
		cache.head.next = cache.tail
		cache.tail.prev = cache.head
		cache.mappings = make(map[string]*lruNode)
	})
	return cache
}

func (lc *lruCache) add(node *lruNode) {
	nextNode := lc.head.next
	lc.head.next = node
	node.prev = lc.head
	nextNode.prev = node
	node.next = nextNode
}

func (lc *lruCache) del(node *lruNode) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (lc *lruCache) Get(key string) interface{} {
	if v, ok := lc.mappings[key]; ok {
		lc.del(v)
		lc.add(v)
		return v.val
	}
	return nil
}

func (lc *lruCache) Add(key string, val interface{}) {
	if v, ok := lc.mappings[key]; ok {
		lc.mappings[key].val = val
		lc.del(v)
		lc.add(v)
	} else {
		node := new(lruNode)
		node.val = val
		node.key = key
		lc.add(node)
		lc.mappings[key] = node
		if lc.cap == 0 {
			delete(lc.mappings, lc.tail.prev.key)
			lc.del(lc.tail.prev)
		} else {
			lc.cap--
		}
	}
}
