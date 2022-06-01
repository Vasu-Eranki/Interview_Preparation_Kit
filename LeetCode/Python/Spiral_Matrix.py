class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n_cols = len(matrix[0])
        n_rows = len(matrix)
        matrix = recursive_solution(0,0,n_rows,n_cols,[],matrix)
        return matrix

def recursive_solution(starting_rows,starting_cols,ending_rows,ending_cols,spiral_matrix,matrix):
        if(starting_cols<ending_cols) and (starting_rows<ending_rows):
            for i in range(starting_cols,ending_cols):
                spiral_matrix.append(matrix[starting_rows][i])
            for j in range(starting_rows+1,ending_rows):
                spiral_matrix.append(matrix[j][ending_cols-1])
            if((ending_rows-1)!=starting_rows):
                for i in range(ending_cols-2,starting_cols-1,-1):
                    spiral_matrix.append(matrix[ending_rows-1][i])
            if((ending_cols-1)!=starting_cols):
                for j in range(ending_rows-2,starting_rows,-1):
                    spiral_matrix.append(matrix[j][starting_cols])
            spiral_matrix=recursive_solution(starting_rows+1,starting_cols+1,ending_rows-     1,ending_cols-1,spiral_matrix,matrix)  
        else:
            return spiral_matrix
        return spiral_matrix
