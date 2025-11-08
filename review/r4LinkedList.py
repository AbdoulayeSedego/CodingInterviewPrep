class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val    # The data
        self.next = next  # Pointer to next node

        # Create: 1 → 2 → 3 → None
node3 = ListNode(3, None)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = node1  # Head points to first node

# Traverse:
current = head
while current:
    print(current.val)  # 1, 2, 3
    current = current.next