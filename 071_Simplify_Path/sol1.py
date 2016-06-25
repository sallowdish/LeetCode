class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = ['']
        steps = path.split('/')
        for step in steps:
            if not step or step == ".":
                continue
            if step == "..":
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(step)
        return "/".join(stack) if len(stack) > 1 else "/"
