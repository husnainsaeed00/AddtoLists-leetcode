# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10

            current.next = ListNode(digit)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next


# Create linked lists
# l1 = [2, 4, 3]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# l2 = [5, 6, 4]
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Create an instance of the Solution class
solution = Solution()

# Add the two numbers
result = solution.addTwoNumbers(l1, l2)

# Create a list to store the result digits
result_digits = []

# Traverse the result linked list and collect the digits
while result:
    result_digits.append(str(result.val))
    result = result.next

# Reverse the list of digits and join them into a single string
result_str = " ".join(result_digits[::-1])

# Print the result
print(result_str)
