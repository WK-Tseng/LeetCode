class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.defaultdict(list)
        self.key_value = {}
        

    def get(self, key: int) -> int:
        if key in self.key_value:
            # print(f'key: {key}--------')
            # print(self.key_value)
            # print(self.cache)

            times = self.key_value[key][1]
            self.cache[times].remove(key)
            if len(self.cache[times]) == 0:
                self.cache.pop(times)

            times += 1
            self.cache[times].append(key)
            self.key_value[key][1] = times

            # print(self.key_value)
            # print(self.cache)
            # print('-----------------------')

            return self.key_value[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print('put ++++++++++++', key, value)
        # print(self.key_value)
        # print(self.cache)

        if self.capacity == 0:
            pass
        else:
            if key in self.key_value:
                times = self.key_value[key][1]
                self.cache[times].remove(key)
                if len(self.cache[times]) == 0:
                    self.cache.pop(times)

                times += 1
                self.key_value[key] = [value, times]
                self.cache[times].append(key)
            else:
                if len(self.key_value) == self.capacity:
                    times = min(self.cache.keys())
                    # print(f'times: {times}')
                    remove_key = self.cache[times].pop(0)
                    if len(self.cache[times]) == 0:
                        self.cache.pop(times)
                    
                    self.key_value.pop(remove_key)

                self.key_value[key] = [value, 1]
                self.cache[1].append(key)

        # print(self.key_value)
        # print(self.cache)
        # print('++++++++++++++++')


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)