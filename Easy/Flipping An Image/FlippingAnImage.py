class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for row in image:
            flipped_row = row[::-1]
            inverted_row = [1-bit for bit in flipped_row]
            res.append(inverted_row)
        return res
    
#QED
#Problem 832 (Easy Of Flipping An Image) - Jason Balayev (python)