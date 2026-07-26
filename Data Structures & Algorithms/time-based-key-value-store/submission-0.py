class TimeMap:

    def __init__(self):
        self.t = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t: 
            self.t[key] = []
        self.t[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        print(self.t)
        if key not in self.t: 
            return ""
        
        arr = self.t[key]
        l = 0
        r = len(arr) - 1
        result = ""
        while l <= r: 
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp: 
                result = arr[mid][1]
                l = mid + 1
            else: 
                r = mid - 1
            
        return result