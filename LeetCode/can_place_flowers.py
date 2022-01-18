class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if (len(flowerbed) == 1 and flowerbed[0] == 0) or n == 0:
            return True
        
        plants = [0] + list(flowerbed) + [0]
        remaining = n
        
        for index in range(1, len(plants) - 1):
            if plants[index - 1] == plants[index] == plants[index + 1] == 0:
                plants[index] = 1
                remaining -= 1
            if remaining == 0:
                return True

        return False