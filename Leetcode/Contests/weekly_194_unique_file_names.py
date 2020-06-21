# 5441. Making File Names Unique

'''
Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute, you will create a folder with the name names[i].

Since two files cannot have the same name, if you enter a folder name which is previously used, the system will have a suffix addition to its name in the form of (k), where, k is the smallest positive integer such that the obtained name remains unique.

Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder when you create it.
'''


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        dic = {}
        res = []
        for name in names:
            suffix = None
            just_name = name
            flag = False
            if '(' in name:  # might have a number
                try:
                    closing = name.index(')')
                    # print('got closing')
                    if closing:
                        opening = name.index('(')
                        suffix = int(name[opening + 1:closing])
                        just_name = just_name[:opening]
                        flag = True
                        # print('got here! just_name is', just_name)
                except:
                    pass
            if just_name not in dic:
                # print('first timer with', name)
                dic[just_name] = [suffix]
                res.append(name)
                # print('dic is', dic)
            else:
                taken = dic[just_name]
                if suffix not in taken:
                    dic[just_name].append(suffix)
                    res.append(name)
                    # print('suffix wasnt taken, dic is', dic)
                else:  # already taken, find least available
                    if not flag:
                        ini = 1
                        while ini in taken:
                            ini += 1
                        dic[just_name].append(ini)
                        res.append(just_name + '(' + str(ini) + ')')
                        # print('suffix was taken, dic is', dic)
                    else:  # suffix was taken also this should be appended
                        new_suffix = 1
                        while suffix + 0.1 * new_suffix in taken:
                            new_suffix += 1
                        dic[just_name].append(suffix + 0.1 * new_suffix)
                        res.append(name + '(' + str(new_suffix) + ')')
                        # print('suffix was taken and flag activated, dic is', dic)
        return res


# input ["b(4)(3)","d(1)","k","z(1)(4)","u","s(1)(2)","q(1)(4)","z(1)","r","b(3)(4)","x","e","r(1)","t","e","z(2)","d","n(1)","o","o","t(1)","l","p","a","w","j(3)","w","c(3)","q","v","u"]

# expected ["b(4)(3)","d(1)","k","z(1)(4)","u","s(1)(2)","q(1)(4)","z(1)","r","b(3)(4)","x","e","r(1)","t","e(1)","z(2)","d","n(1)","o","o(1)","t(1)","l","p","a","w","j(3)","w(1)","c(3)","q","v","u(1)"]
