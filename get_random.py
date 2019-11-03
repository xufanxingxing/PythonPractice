import random


class key_val_store:
    
    def __init__(self):
        
        self.key_val = {}
        self.idx_to_key = []
    
    def get(self, key):
        if key in self.key_val.keys():
            return self.key_val.get(key)[0]
        return None
        
    def set_pair(self, key, val):
        if key in self.key_val.keys():
            self.key_val[key][0] = val
        else:
            new_pair = [val, len(self.idx_to_key)]
            self.key_val[key] = new_pair
            self.idx_to_key.append(key)
        
    def delete(self, key):
        if key in self.key_val.keys():
            curr_idx = self.key_val[key][1]
            curr_last_key = self.idx_to_key[-1]

            self.idx_to_key[curr_idx] = curr_last_key        
            self.key_val[curr_last_key][1] = curr_idx
            self.key_val.pop(key)
            self.idx_to_key.pop()

        return key
          
    def get_random(self):
        if len(self.idx_to_key) == 0:
            return None
        random_idx = random.randint(0, len(self.idx_to_key) - 1)
        print("random_idx = ",random_idx)
        print("idx_to_key",self.idx_to_key)
        random_key = self.idx_to_key[random_idx]
        return self.key_val[random_key][0]
        
        
    
a = key_val_store()
a.set_pair(1,1)
a.set_pair(3,3)
a.set_pair(4,4)
a.set_pair(6,6)
a.set_pair(8,12)

print(a.get(1))
print(a.get(3))
print(a.get(2))

a.set_pair(3,5)
print(a.get(3))

print("random",a.get_random())

print("delete",a.delete(1))
print("delete",a.delete(3))
print("delete",a.delete(4))
print("delete",a.delete(1))
