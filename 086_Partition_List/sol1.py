from utils.ListNode import *


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        # build list
        lst = head.to_list()
        insert_before = None
        for i in range(len(lst)):
            if lst[i] >= x:
                if insert_before is not None:
                    continue
                insert_before = i
            else:
                if insert_before is None:
                    continue
                temp = lst[i]
                del lst[i]
                lst.insert(insert_before, temp)
                insert_before += 1

        return build_linked_list_from_pylist(lst)
