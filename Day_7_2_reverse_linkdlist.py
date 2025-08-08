class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left == right:
        return head
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    curr = prev.next
    for _ in range(right - left):
        tmp = curr.next
        curr.next = tmp.next
        tmp.next = prev.next
        prev.next = tmp
    return dummy.next

def toList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

head = ListNode(1)
curr = head
for i in range(2, 6):
    curr.next = ListNode(i)
    curr = curr.next
new_head = reverseBetween(head, 2, 4)
print(toList(new_head))  # [1, 4, 3, 2, 5]
