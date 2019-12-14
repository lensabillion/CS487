def sortColors(nums):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if nums[i]<nums[j]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
  
