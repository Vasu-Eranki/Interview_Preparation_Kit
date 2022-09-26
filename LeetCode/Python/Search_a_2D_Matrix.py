class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = binary_2d_search(matrix,target)
        return index
    
def binary_2d_search(matrix,value):
    index = False
    while(len(matrix)!=0):
        mid_length = len(matrix)//2
        first_element = matrix[mid_length][0]
        last_element = matrix[mid_length][-1]
        if(value<=last_element) and (value>=first_element):
            index = binary_search(matrix[mid_length],value)
            return index
        elif(value<first_element):
            matrix =matrix[:mid_length]
        else:
            matrix = matrix[mid_length+1:] 
    return index 
    
def binary_search(matrix, value):
    index = False
    while(len(matrix)!=0):
        mid_length = len(matrix)//2
        if(matrix[mid_length]==value):
            return True
        elif(matrix[mid_length]<value):
            matrix = matrix[mid_length+1:]
        else:
            matrix = matrix[:mid_length]
    return index
