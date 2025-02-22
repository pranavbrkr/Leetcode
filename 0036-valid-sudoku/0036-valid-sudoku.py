class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            h_set = set()
            v_set = set()

            for j in range(9):
                if board[i][j] in h_set:
                    return False
                if board[i][j] != '.':
                    h_set.add(board[i][j])
                
                if board[j][i] in v_set:
                    return False
                if board[j][i] != '.':
                    v_set.add(board[j][i])
        
        box_dict = {}
        for i in range(9):
            a = i // 3
            for j in range(9):
                b = j // 3

                if (a, b) not in box_dict:
                    box_dict[(a, b)] = set()
                
                if board[i][j] in box_dict[(a, b)]:
                    return False
                if board[i][j] != '.':
                    box_dict[(a, b)].add(board[i][j])

        return True