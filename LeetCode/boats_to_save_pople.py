class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = list(sorted(people))
        front = 0
        back = len(people) - 1
        boats = 0
        
        while front <= back:
            if people[front] + people[back] <= limit:
                front += 1
            boats += 1
            back -= 1
        
        return boats