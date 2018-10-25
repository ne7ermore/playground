import mmh3
from bitarray import bitarray


class BloomFilter(object):

    def __init__(self, bit_size=5000000, seeds=[11, 12, 13, 14, 15]):
        bit_array = bitarray(bit_size)
        bit_array.setall(0)

        self.bit_array = bit_array
        self.seeds = seeds
        self.bit_size = bit_size

    def add(self, url):
        for b in self.get_slots(url):
            self.bit_array[b] = 1

    def contains(self, url):
        slots = self.get_slots(url)
        return all([self.bit_array[b] for b in slots])

    def hash(self, args):
        return mmh3.hash(args[0], args[1]) % self.bit_size

    def get_slots(self, url):
        return map(self.hash, zip([url] * len(self.seeds), self.seeds))


if __name__ == "__main__":
    b = BloomFilter()

    url = "https://ne7ermore.github.io/"
    print(b.contains(url))
    b.add(url)
    print(b.contains(url))
