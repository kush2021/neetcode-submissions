class MedianFinder:

    def __init__(self):
        self.data = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.size += 1

    def findMedian(self) -> float:
        self.data.sort()
        if self.size % 2 == 1:
            return self.data[self.size // 2]
        return (self.data[self.size // 2 - 1] + self.data[self.size // 2]) / 2