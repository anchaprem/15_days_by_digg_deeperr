class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def hasCycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
            
    return False

# Example usage (create nodes manually to test)
# node1 = ListNode(3)
# node2 = ListNode(2)
# node3 = ListNode(0)
# node4 = ListNode(-4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2  # Cycle here
# print(hasCycle(node1))  # Output: True
