#Time complexity : O(N), Space complexity : O(1)
class Solution(object):
    def trap(self, height):
        # Solution : 가장 높은 Wall을 찾음. 양끝에서 시작해서, 가장 높은 wall에 다다를때까지 계산.
        # 지금까지 마주친 가장 높은 블록을 Wall로 설정하여, 새로운 블록을 마주칠때마다 차이값을 계산하여 더함.
        # 현재 Wall과 같은 높이거나 더 높은 블록을 마주칠때마다 Wall을 업데이트.
        
        if not height:
            return 0
        
        #Find index of maximum value
        highest_wall = height.index(max(height))
 
        total_water = 0
        #left-to-right
        wall_height = 0
        for i in range(highest_wall):
            wall_height = max(wall_height, height[i])
            total_water += (wall_height - height[i])
    
        #right-to-left
        wall_height = 0
        for i in reversed(range(highest_wall, len(height))):
            wall_height = max(wall_height, height[i])
            total_water += (wall_height - height[i])
        
        return total_water