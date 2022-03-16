class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_index = 0
        new_stack = []
        
        for item in pushed:
            new_stack.append(item)
            while new_stack and new_stack[-1] == popped[pop_index]:
                new_stack.pop()
                pop_index += 1
        
        return pop_index == len(popped)