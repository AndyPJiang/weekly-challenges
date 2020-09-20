class MatchParentheses:
    '''
    Given a base string of parentheses and a target string of parentheses, 
    find the minimum number of single character insertions such that the target 
    string is a substring of the base string.

    '''

    def __init__(self, base: str, target: str):
        self.base = base
        self.target = target

    def match(self) -> int:
        if not self.base:
            return len(self.target)
        min_insertions = float('inf')

        for i in range(len(self.base)):
            # count number of insertions needed if substring starts at position i
            insertions = 0

            for j in range(len(self.target)):
                # reached end of base string, must insert new paranthesis to match
                if i+j+insertions >= len(self.base):
                    insertions+=1
                # need to inesrt paranthesis if they don't match
                elif self.target[j] != self.base[i+j-insertions]:
                    insertions+=1

            min_insertions = min(min_insertions, insertions)
        return min_insertions




# f = MatchParentheses
# print(f.match('((()())()()))','(((())))'))
