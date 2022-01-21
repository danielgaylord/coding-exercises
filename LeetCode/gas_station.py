class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        stations = len(gas)
        if sum(cost) > sum(gas):
            return -1
        
        total_gas, cur_gas = 0, 0
        station = 0
        
        for start_index in range(stations):
            cur_gas += gas[start_index] - cost[start_index]
            total_gas += gas[start_index] - cost[start_index]
            if cur_gas < 0:
                station = start_index + 1
                cur_gas = 0
        
        return station
            