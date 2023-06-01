class FrequencyTracker:

    def __init__(self):
        self.counter = Counter()
        self.frequencySet = collections.defaultdict(set)

    def add(self, number: int) -> None:
        self.counter[number] += 1
        
        frequency = self.counter[number]
        self.frequencySet[frequency].add(number)
        self.frequencySet[frequency-1].discard(number)

    def deleteOne(self, number: int) -> None:
        self.counter[number] -= 1

        frequency = self.counter[number]
        if frequency < 0:
            frequency = 0
            self.counter[number] = frequency
            
        self.frequencySet[frequency].add(number)
        self.frequencySet[frequency+1].discard(number)

    def hasFrequency(self, frequency: int) -> bool:
        return len(self.frequencySet[frequency]) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)