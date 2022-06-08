class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_dict = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'}
        alphabets = [number_dict[i] for i in digits]
        results = recursive_solution(alphabets)
        return results
        
def recursive_solution(alphabets):
    if(not alphabets):
        return
    results = []
    for i in alphabets[0]:
            combos = recursive_solution(alphabets[1:])
            if(combos):
                for j in combos:
                    results.append(i+j)
            else:
                results.append(i)
    return results
        
