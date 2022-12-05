class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(seat - stu) for seat, stu in zip(sorted(seats), sorted(students)))