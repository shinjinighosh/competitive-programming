class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def bfs(agenda): 

            # distance holds distance to target from current
            # returns -1 if cannot reach

            visited = set(deadends)

            while agenda:

                current, distance = agenda.popleft()
                if current == target:
                    return distance

                if current in visited:
                    continue
                visited.add(current)

                for idx, num in enumerate(current):
                    if num == "0":
                        option_1 = current[:idx] + "9" + current[idx+1:]
                        option_2 = current[:idx] + str(int(num) + 1) + current[idx+1:]
                    elif num == "9":
                        option_2 = current[:idx] + "0" + current[idx+1:]
                        option_1 = current[:idx] + str(int(num) - 1) + current[idx+1:]
                    else: 
                        option_1 = current[:idx] + str(int(num) - 1) + current[idx+1:]
                        option_2 = current[:idx] + str(int(num) + 1) + current[idx+1:]

                    if option_1 not in visited:
                            agenda.append((option_1, distance + 1))
                    if option_2 not in visited:
                            agenda.append((option_2, distance + 1))

            return -1 # finished agenda and could not get to target
                

        agenda = deque([("0000", 0)]) # starts at the root
        return bfs(agenda) # since it is bfs, it should find the minimum distance route first

