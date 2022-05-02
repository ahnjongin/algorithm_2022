class LRUCache:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.dic = {}


    def get(self, key: int) -> int:
        if key in self.dic:
            value = self.dic.pop(key)
            self.dic[key] = value
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        elif len(self.dic) == self.max_size:
            del self.dic[next(iter(self.dic))]
        self.dic[key] = value

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        num = list(map(int,input().split()))
        lst = list(map(int,input().split()))
        LRUCache1 = LRUCache(num[0])
        count = 0
        for i in range(num[1]):
            if lst[count] == 0:
                LRUCache1.put(lst[count+1], lst[count+2])
                count += 3
            elif lst[count] == 1:
                print(LRUCache1.get(lst[count+1]))
                count += 2