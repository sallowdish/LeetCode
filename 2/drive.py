from sol3 import ListNode, Solution

l1 = None
l2 = None
with open("data.in", 'r') as f:
    lst1 = list(f.readline()[1:-2].split(","))
    lst2 = list(f.readline()[1:-2].split(","))
    ptr = l1
    for i in lst1:
        if l1 is None:
            l1 = ListNode(int(i))
            ptr = l1
        else:
            ptr.next = ListNode(int(i))
            ptr = ptr.next
    ptr = l2
    for i in lst2:
        if l2 is None:
            l2 = ListNode(int(i))
            ptr = l2
        else:
            ptr.next = ListNode(int(i))
            ptr = ptr.next

rev = Solution().addTwoNumbers(l1,l2)
rev