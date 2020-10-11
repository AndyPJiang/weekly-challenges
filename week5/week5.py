class TrieNode:
    def __init__(self):
        # one extra character for the apostrophe
        self.links = [0] * 27
        self.isEnd = False

class Dictionary:
    def __init__(self):
        self.trie = TrieNode()
        f = open("words2.txt", "r")
        for word in f.readlines():
            self._insertWord(word.lower().strip())

    def _insertWord(self,word):
        node = self.trie
        for char in word:
            if char == "'":
                ind = 26
            else:
                ind = ord(char)-ord('a')
            if not node.links[ind]:
                node.links[ind] = TrieNode()
            node = node.links[ind]

        node.isEnd = True
    
    def _traverseTrie(self,word):
        """
        Helper function to traverse a trie given a word/prefix
        """
        node = self.trie
        for char in word:
            if char == "'":
                ind = 26
            else:
                ind = ord(char)-ord('a')
            if not node.links[ind]:
                return None
            node = node.links[ind]
        return node

    def isWord(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self._traverseTrie(word.lower())
        if node:
            return node.isEnd
        return False

    def isPrefix(self, prefix):
        """
        Returns if there is any word in the trie that starts with a given prefix.
        """
        node = self._traverseTrie(prefix.lower())
        if node:
            return True
        return False

class LongestWordInGrid:
    def __init__(self, grid):
        self.grid = grid
        self.trie = Dictionary()


    def longestWord(self):
        grid = self.grid
        if not grid:
            return ""
        n = len(grid)
        m = len(grid[0])
        resWord = ''
        resLength = 0
        for i in range(n):
            for j in range(m):
                longestWordLength, longestWord = self._searchWord(i,j,grid[i][j], set((i,j)))
                if longestWordLength > resLength:
                    resLength = longestWordLength
                    resWord = longestWord
        return resWord


    # DFS to search for longest word given a starting index
    def _searchWord(self,i,j, prefix, seen):
        longestWord = ''
        longestWordLength = 0

        adjacentCells = [
                        (i+1,j),
                        (i-1,j),
                        (i,j+1),
                        (i,j-1),
                        (i+1,j+1),
                        (i-1,j-1),
                        (i+1,j-1),
                        (i-1,j+1)
                    ]

        for x,y in adjacentCells:
            if x >= 0 and x < len(self.grid) and y >= 0 and y < len(self.grid[0]) and (x,y) not in seen:
                word = prefix + self.grid[x][y]
                if self.trie.isPrefix(word):
                    seen.add((x,y))
                    longestL, longestW= self._searchWord(x,y, word, seen)
                    # letter will be part of the next word we look at, so remove it
                    seen.remove((x,y))
                    if longestWordLength < longestL:
                        longestWordLength = longestL
                        longestWord = longestW

                if self.trie.isWord(word):
                    if longestWordLength < len(word):
                        longestWordLength = len(word)
                        longestWord = word

        return (longestWordLength, longestWord)