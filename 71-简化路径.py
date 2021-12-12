class Solution:
    def simplifyPath(self, path: str) -> str:
        files = path.split("/")
        stack = []
        res = ""
        for file in files:
            if file != "":
                if file == "..":
                    if stack != []:
                        stack.pop()
                elif file != ".":
                    stack.append(file)
        if stack == []:
            return "/"
        for i in stack:
            res += "/" + i
        return res
