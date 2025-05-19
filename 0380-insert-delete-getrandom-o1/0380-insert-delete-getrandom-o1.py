class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.num_list = []
        self.n = 0

    def insert(self, val: int) -> bool:
        res = val not in self.num_map
        if res:
            self.num_map[val] = self.n
            self.num_list.append(val)
            self.n += 1
        
        return res

    def remove(self, val: int) -> bool:
        res = val in self.num_map

        if res:
            curr_pos = self.num_map[val]
            last_ele = self.num_list[-1]
            self.num_list[curr_pos] = last_ele
            self.num_list.pop()
            self.n -= 1
            self.num_map[last_ele] = curr_pos
            del self.num_map[val]
        
        return res


        

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()