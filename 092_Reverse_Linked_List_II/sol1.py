from utils.ListNode import *


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        if m == n:
            # no need to reverse
            return head
        step_count = 1
        reverse_entry_point = reverse_start_point = None
        prev = None
        curr = head
        while curr:
            if step_count < m or step_count > n:
                prev = curr
                curr = curr.next
            elif step_count == m:
                # enter reverse section
                reverse_entry_point = prev if m > 1 else curr
                reverse_start_point = curr
                prev = curr
                curr = curr.next
            elif step_count == n:
                # leave reverse section
                if m > 1:
                    reverse_entry_point.next = curr
                else:
                    head = curr
                reverse_start_point.next = curr.next
                curr.next = prev
                prev = reverse_start_point
                curr = reverse_start_point.next
            else:
                # within reverse section
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            step_count += 1
        if m == 0:
            return reverse_entry_point
        else:
            return head
