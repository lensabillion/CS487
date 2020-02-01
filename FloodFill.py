class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows,cols = len(image),len(image[0])
        startcolor = image[sr][sc]
        
        if startcolor == newColor:
            return image
        stack = [(sr,sc)]
       
        while stack:
            r,c = stack.pop()
            if r < 0 or r >= rows  or c < 0 or c >= cols:
                continue
            if image[r][c] != startcolor:
                continue
            image[r][c] = newColor
            for dr ,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                stack.append((r+dr,c+dc))
            
        return image
           
