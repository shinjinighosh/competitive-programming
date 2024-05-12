class Solution:
    def simplifyPath(self, path: str) -> str:

        elts = path.split("/")
        elts = [i for i in elts if i]
        print(elts)
        
        res = []
        for elt in elts:
            if elt == ".":
                continue
            elif elt == "..":
                if res:
                    res.pop()
            else:
                res.append(elt)
        return "/" + "/".join(res)
