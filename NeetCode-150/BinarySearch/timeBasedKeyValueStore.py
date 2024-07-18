class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append([value, timestamp])
        else: 
            self.dic[key] = [[value,timestamp]]

        
        

    def get(self, key: str, timestamp: int) -> str:
        s = None
        if key in self.dic: 
            s = self.dic[key]
        else:
            return ""
        left = 0
        right = len(s) - 1
        while left <= right:
            mid = left + (right - left) //2 
            if s[mid][1] > timestamp:
                right = mid - 1
                continue
            if s[mid][1] < timestamp:
                left = mid + 1
                continue
            if s[mid][1] == timestamp:
                return s[mid][0]
        if s[right][1] <= timestamp:
            return s[right][0]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == "__main__":
    s = TimeMap()
    s.set("foo", "bar", 2)
    print(s.get("foo", 1)) #""
    print(s.get("foo", 3)) #"bar"
    s.set("foo", "bar2", 4) 
    print(s.get("foo", 6)) #bar2
