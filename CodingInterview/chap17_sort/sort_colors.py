from typing import List

def sort_colors(nums:List[int])->None:
    red,white,blue =0,0,len(nums)

    while white<blue:
        if nums[white]<1:
            nums[red],nums[white]=nums[white],nums[red]
            white+=1
            red+=1
        elif nums[white]>1:
            blue-=1
            nums[blue],nums[white] =nums[white],nums[blue]
        else:
            white+=1
        