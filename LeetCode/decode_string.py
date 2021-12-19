class Solution:
    def decodeString(self, s: str) -> str:
        time_s = []
        code_s = []
        decoded = ""     
        time = 0
        code = ""
        for char in s:
            if char.isnumeric():
                time *= 10
                time += int(char)
            if char.isalpha():
                code += char
            if char == "[":
                time_s.append(time)
                code_s.append(code)
                code = ""
                time = 0
            if char == "]":
                decoded = code_s.pop()
                for _ in range(time_s.pop()):
                    decoded += code
                code = decoded
        return code