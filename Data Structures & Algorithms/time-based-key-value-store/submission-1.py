class TimeMap:

    def __init__(self):
        self.store = {} # key : [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:        
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store:
            return res
        left = 0
        right = len(self.store[key]) - 1
        value_list = self.store[key]
        while left <= right:
            mid = (left + right)
            if value_list[mid][1] <= timestamp:
                res = value_list[mid][0]
                left = mid + 1
            else:
                right = mid - 1            

        return res
        
