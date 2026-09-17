# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        heap = []
        i = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, i, l))
                i += 1

        dummy = ListNode()
        cur = dummy
        while len(heap) != 0:
            v, _, l = heapq.heappop(heap)
            cur.next = l
            cur = cur.next

            if l.next:
                heapq.heappush(heap, (l.next.val, i, l.next))
                i += 1

        return dummy.next
