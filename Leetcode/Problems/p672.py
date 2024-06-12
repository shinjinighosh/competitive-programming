class Solution:
    # def flipLights(self, n: int, presses: int) -> int:

    #     if not presses:
    #         return 1

    #     start = [1] * n
    #     visited = set()

    #     def bfs(start, visited, presses_left, final_states):

    #         agenda = deque([(tuple(start), presses_left)])

    #         while agenda:

    #             current_state, pl = agenda.popleft()

    #             if pl == 0:
    #                 continue
                
    #             current_state = list(current_state)

    #             cand_1 = [1 - x for x in current_state]
    #             cand_2 = current_state[:]
    #             for i in range(1, n, 2):
    #                 cand_2[i] = 1 - cand_2[i]
    #             cand_3 = current_state[:]
    #             for i in range(0, n, 2):
    #                 cand_3[i] = 1 - cand_3[i]
    #             cand_4 = current_state[:]
    #             for i in range(0, n, 3):
    #                 cand_4[i] = 1 - cand_4[i]

    #             # print(f"Candidates are {cand_1}, {cand_2}, {cand_3}, {cand_4}")
                
    #             for cand in [cand_1, cand_2, cand_3, cand_4]:
    #                 if tuple(cand) not in visited:
    #                     visited.add(tuple(cand))
    #                     agenda.append((tuple(cand), pl - 1))
    #                     final_states.add(tuple(cand))
                
    #             # print(f"Visited is {visited} after {current_state}")
            
    #         # print(f"Final states are {final_states}")
    #         return len(final_states)

    #     return bfs(start, visited, presses, set())

    # def flipLights(self, n: int, presses: int) -> int:
    #     if not presses:
    #         return 1

    #     start = [1] * n
    #     visited = set()

    #     def bfs(start, visited, presses_left, final_states):
    #         agenda = deque([(tuple(start), presses_left)])

    #         while agenda:
    #             current_state, pl = agenda.popleft()
    #             if pl == 0:
    #                 continue

    #             current_state = list(current_state)  # Convert tuple back to list to manipulate

    #             # Prepare candidate states for each button press
    #             cand_1 = [1 - x for x in current_state]  # Button 1 flips all bulbs

    #             cand_2 = current_state[:]
    #             for i in range(1, n, 2):  # Button 2 flips bulbs with even labels (1-based)
    #                 cand_2[i] = 1 - cand_2[i]

    #             cand_3 = current_state[:]
    #             for i in range(0, n, 2):  # Button 3 flips bulbs with odd labels (1-based)
    #                 cand_3[i] = 1 - cand_3[i]

    #             cand_4 = current_state[:]
    #             for i in range(0, n, 3):  # Button 4 flips bulbs at 1, 4, 7, ... (1-based)
    #                 cand_4[i] = 1 - cand_4[i]

    #             # Process candidates
    #             for cand in [cand_1, cand_2, cand_3, cand_4]:
    #                 cand_tuple = tuple(cand)
    #                 if cand_tuple not in visited:
    #                     visited.add(cand_tuple)
    #                     agenda.append((cand_tuple, pl - 1))
    #                     final_states.add(cand_tuple)

    #         return len(final_states)

    #     return bfs(start, visited, presses, set())


    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        return 8
