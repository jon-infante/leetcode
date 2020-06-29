# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. 
# A . means it can represent any one letter.

class WordNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()
        
    def addWord(self, word):
        node = self.root
        for let in word:
            if let in node.children:
                node = node.children[let]
            else:
                node.children[let] = WordNode()
                node = node.children[let]
        node.isEnd = True
                
    def search(self, word):
        stack = [(self.root,word)]
        while stack:
            node, let = stack.pop()
            if not let:
                if node.isEnd:
                    return True
            elif let[0]=='.':
                for val in node.children.values():
                    stack.append((val, let[1:]))
            else:
                if let[0] in node.children:
                    val = node.children[let[0]]
                    stack.append((val, let[1:]))
        return False
                        
        
if __name__ == '__main__':
    word = 'bad'
    obj = WordDictionary()
    obj.addWord(word)
    print(obj.search("b.."))