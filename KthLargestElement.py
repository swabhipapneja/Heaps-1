# Time Complexity : O(nlogk) where k is the given no and n is the no of element sin the list
# - every insertion in heap takes O(log k) time and we are doing it k times
# Space Complexity : O(k), because we are taking k as the size of the min heap
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# using min heap because we have to find kth LARGEST element
# by default heapq in python is set to minheap
# in min heap - every parent should be less than both its children, it's a complete binary tree (all levels are full exxcept the last level) and the children are more to the left
# at every iteration, we put an element in the minheap, it should be a valid minheap at all times
# if the size of heap > k => then we have to extract the smallest element => heap.pop()
# we repeat this for all the elements in nums
# after all iterations, we have removed n-k small elements and the next is the kth largest element



import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None:
            return 0
        
        n = len(nums)
        
        pq = [] 
        heapq.heapify(pq) # priority queue storing the list of elements in the heap

        # iterating over all the elements of nums
        for i in range(n):
            num = nums[i]
            # adding the element num to the pq
            heapq.heappush(pq, num)
            # if the size of the pq is greater than k, we have to remove the smallest element in the pq
            # which is present at the head/root - heappop operation
            if len(pq) > k:
                # remove the top element
                heapq.heappop(pq)
        
        # returning the head of the min heap
        return heapq.heappop(pq) # the head of the heap is the kth largest element
            





        