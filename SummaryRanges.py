class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
       
        flist = []
        
        if len(nums) == 0:
            return flist
        if len(nums) == 1:
            flist.append(str(nums[0]))
            return flist
        
        head = nums[0]
        trailer = head
        tail = nums[1]
        
        for i in range(1, len(nums)): 
            if tail == (trailer + 1):
                trailer = tail
                if (i + 1) >= len(nums):
                    flist.append(str(head) + "->" + str(tail))
                else:
                    tail = nums[i+1]
                continue
            elif tail != (trailer + 1):
                if trailer == head:
                    flist.append(str(head))
                    head = tail
                    trailer = head
                    if (i + 1) >= len(nums):
                        flist.append(str(tail))
                    else:
                        tail = nums[i+1]
                else:
                    flist.append(str(head) + "->" + str(trailer))
                    head = tail
                    trailer = head
                    if (i + 1) >= len(nums):
                        flist.append(str(tail))
                    else:
                        tail = nums[i+1]
        return flist        
