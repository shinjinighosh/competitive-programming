class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        curr_num = 0 # to build the repetition number
        curr_str = ""

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == "[":  # starting a new repeating sequence
                count_stack.append(curr_num)
                string_stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif char == "]": # finished a repeating sequence
                repeat_count = count_stack.pop()
                top_str = string_stack.pop()
                curr_str = top_str + curr_str * repeat_count
            else:
                curr_str += char
            # print(f"{char}: count_stack is {count_stack}, str_stack is {string_stack}, curr_num {curr_num}, curr_str {curr_str}")
        
        return curr_str
