def reconstructQueue(people):
    # first pick out all the 0's
    current_k = 0
    current_agenda = []
    result = []
    for h, k in people:
        if k == 0:
            current_agenda.append([h, k])
    # sort in decreasing order of height
    current_agenda.sort(key=lambda x: x[0])
    result += current_agenda
    current_agenda = []
    current_k += 1
    while len(result) != len(people):
        for h, k in people:
            if k == current_k:
                current_agenda.append([h, k])
        # sort in decreasing order of height
        current_agenda.sort(reverse=True, key=lambda x: x[0])
        # print("current agenda is", current_agenda)
        current_k += 1
        while current_agenda:
            new_height, new_k = current_agenda.pop(0)
            # could have also removed reverse = True, and let pop remove from the end
            count = 0
            for index, (h, k) in enumerate(result):
                if h >= new_height:
                    count += 1
                if count == new_k:  # already found k people >= in height, so insert here
                    result.insert(index + 1, [new_height, new_k])
                    break
            else:
                # should not come here? it means we have gone through the list without inserting
                result.append([new_height, new_k])
            # print(result)

    return result


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(reconstructQueue(people))
