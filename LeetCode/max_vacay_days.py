class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(city, week):
            if week == len(days[0]):
                return 0
            max_vacay = 0
            for dest, avail in enumerate(flights[city]):
                if avail == 1 or dest == city:
                    vacay = days[dest][week] + dfs(dest, week + 1)
                    max_vacay = max(max_vacay, vacay)
            return max_vacay
            
        return dfs(0, 0)