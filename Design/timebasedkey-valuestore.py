"""Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. 
  If there are no values, it returns "".
"""

class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((timestamp, value))
        else:
            self.timemap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap:
            left = 0
            right = len(self.timemap[key]) - 1
            closest = None
            while left <= right:
                mid = (left + right) // 2
                val = self.timemap[key][mid][0]
                if val == timestamp:
                    return self.timemap[key][mid][1]
                elif val < timestamp:
                    closest = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return self.timemap[key][closest][1] if closest is not None else ""
        else:
            return ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)