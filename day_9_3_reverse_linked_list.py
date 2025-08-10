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
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    
    return dummy.next

# Example
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = reverseBetween(head, 2, 4)
while result:
    print(result.val, end=" ")  # Output: 1 4 3 2 5
    result = result.next
