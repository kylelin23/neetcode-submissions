class TimeMap:

    def __init__(self):
        self.l = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.l: 
            self.l[key] = []
        self.l[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.l: 
            return ""
        arr = self.l[key]
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