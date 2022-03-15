class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def man_dist(work, bike):
            return abs(work[0] - bike[0]) + abs(work[1] - bike[1])
        
        trips = []
        
        for work, w_loc in enumerate(workers):
            for bike, b_loc in enumerate(bikes):
                trips.append((man_dist(w_loc, b_loc), work, bike))
        
        trips.sort()
        
        bike_stat = [False for _ in range(len(bikes))]
        work_stat = [-1 for _ in range(len(workers))]
        pair_ct = 0
        
        for dist, work, bike in trips:
            if work_stat[work] == -1 and not bike_stat[bike]:
                bike_stat[bike] = True
                work_stat[work] = bike
                pair_ct += 1
                
                if pair_ct == len(workers):
                    return work_stat
        
        return work_stat