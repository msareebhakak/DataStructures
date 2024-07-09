#
# Author: Sareeb Hakak
# Purpose: Learn Hashtable
# Date: 24 Feb 24
# Python uses dictionary, C++ has std::map
#
# ord function takes a char and gives the ASCII representation
print(ord('A'))  # Output: 65
print(ord('a'))  # Output: 97
# chr takes ASCII unicode and returns a char
print(chr(65))  # Output: 'A'
print(chr(97))  # Output: 'a'


def get_hash(key):
    """
    simple hash function
    """
    h = 0
    for char in key:
        h += ord(char)
    return h % 100


class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def add(self, key, value):
        h_key = self.get_hash(key)
        self.arr[h_key] = value

    def __setitem__(self, key, value):
        h_key = self.get_hash(key)
        self.arr[h_key] = value

    def get(self, key):
        h_key = self.get_hash(key)
        return self.arr[h_key]

    def __getitem__(self, key):
        h_key = self.get_hash(key)
        return self.arr[h_key]

    def delete(self, key):
        h_key = self.get_hash(key)
        self.arr[h_key] = None

    def __delitem__(self, key):
        h_key = self.get_hash(key)
        self.arr[h_key] = None


class ChainedHashTable(HashTable):
    def __init__(self):
        """
        Modify the original implementation to use chaining
        Replace value in self.arr with a list. This list stores a (key, value) pair
        """
        super().__init__()
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def add(self, key, value):
        h_key = self.get_hash(key)

        found = False
        for count, ele in enumerate(self.arr[h_key]):
            # val will be the (key, element) tuple
            if len(ele) == 2 and ele[0] == value:
                self.arr[h_key][count] = (key, value)
                found = True
                break
        if not found:
            # append if key doesn't exist
            self.arr[h_key].append((key, value))

    def get(self, key):
        h_key = self.get_hash(key)

        for count, ele in enumerate(self.arr[h_key]):
            if len(ele) == 2 and ele[0] == key:
                return self.arr[h_key][count][1]

    def __setitem__(self, key, value):
        h_key = self.get_hash(key)

        found = False
        for count, ele in enumerate(self.arr[h_key]):
            # val will be the (key, element) tuple
            if len(ele) == 2 and ele[0] == key:
                self.arr[h_key][count] = (key, value)
                found = True
                break
        if not found:
            # append if key doesn't exist
            self.arr[h_key].append((key, value))

    def __getitem__(self, key):
        h_key = self.get_hash(key)

        for count, ele in enumerate(self.arr[h_key]):
            if len(ele) == 2 and ele[0] == key:
                return self.arr[h_key][count][1]

    def delete(self, key):
        h_key = self.get_hash(key)
        for count, ele in enumerate(self.arr[h_key]):
            if len(ele) == 2 and ele[0] == key:
                del self.arr[h_key][count]

    def __delitem__(self, key):
        h_key = self.get_hash(key)
        for count, ele in enumerate(self.arr[h_key]):
            if len(ele) == 2 and ele[0] == key:
                del self.arr[h_key][count]


if __name__ == '__main__':
    print(get_hash('m'))

    hmap = HashTable()
    print(hmap.get_hash('march9'))

    hmap.add('humu', 28)
    hmap.add('sar', 29)

    print(hmap.get('humu'))
    print(hmap.get('sar'))

    hmap['humu'] = 28
    hmap['sar'] = 29

    print(hmap['humu'])
    print(hmap['sar'])

    t = ChainedHashTable()
    print(t.get_hash('march6') == t.get_hash('march17'))
    t['march6'] = 120
    t['march6'] = 86  # should replace 120
    t['march17'] = 130
    print(t.arr)
    print(t['march6'])
    print(t['march17'])
    del t['march6']
    print(t['march6'])
