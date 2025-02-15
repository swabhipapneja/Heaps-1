# Time Complexity : O(nk logk) where k is the given no of lists and n is the avg no of elements in the lists
# - every insertion in heap takes O(log k) time and we are doing it nk times
# Space Complexity : O(k), because we are taking k as the size of the min heap
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# using min heap because we have to find kth LARGEST element
# by default heapq in python is set to minheap
# in min heap - every parent should be less than both its children, it's a complete binary tree (all levels are full exxcept the last level) and the children are more to the left
# heapq cannot process listnode because they are not iteratable, so we store them as tuple
# but we have to store the node in heap, so that we can move to the next of this node

# every list is sorted in ascending order
# we take the first node from k lists and store it in a heap
# then we take the min value from the heap and store it in the final LL
# now which ever node is our min, we move curr to it's next
# and we keep on going until the heap becomes empty




import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if lists is None:
            return None
        
        # dummy node
        dummy = ListNode(-1)

        # priority queue to store the min heap, min heap by default
        # storing lisnodes in the pq
        pq = []

        # iterating over the given lists, to store the min of every list in the min heap
        for i,l in enumerate(lists):
            # adding the first node of every list in the pq/heap
            if l is not None:
                heapq.heappush(pq, (l.val, i, l))
        
        # current starts with a dummy node
        curr = dummy

        # while the heap is not empty
        while pq:
            # extract the min from the heap, which is at the head
            # and store it in min
            val, i, minn = heapq.heappop(pq)
            # now we add this node to the answer LL
            # since we are storing list nodes in heap, we do not need to create node here
            curr.next = minn
            # if there is a next element of min in the list
            # min is the node that came out of pq
            # add the next value in the pq
            if minn.next is not None:
                heapq.heappush(pq, (minn.next.val, i, minn.next))
            # and we move current to the next node
            curr = curr.next
        
        # returning the final LL
        return dummy.next






        