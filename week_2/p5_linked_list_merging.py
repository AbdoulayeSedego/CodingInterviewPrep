class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode(0) #create a dummy node
        current = result

        #while both list have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        #attaching remaining nodes if any
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return result.next



# Helper functions
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test
solution = Solution()
list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 4])
merged = solution.mergeTwoLists(list1, list2)
print(print_list(merged))  # [1, 1, 2, 3, 4, 4]
# ```

# **Problem:** Merge two sorted linked lists into one sorted list.

# **Example:**
# ```
# List1: 1 → 2 → 4
# List2: 1 → 3 → 4

# Merged: 1 → 1 → 2 → 3 → 4 → 4