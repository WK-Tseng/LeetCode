class TweetCounts:

    def __init__(self):
        self.record = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        heapq.heappush(self.record[tweetName], time)
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = 60
        if freq == 'hour':
            delta = 3600
        elif freq == 'day':
            delta = 86400
        
        result = [0] * ((endTime - startTime) // delta +  1)
        for time in self.record[tweetName]:
            if startTime <= time <= endTime:
                result[(time-startTime) // delta] += 1

        return result


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)