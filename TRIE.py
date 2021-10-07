# TRIE

class TrieNode:
    def __init__(self):
        self.children={ }
        self.endofString=False
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insertString(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endofString=True
        print("Succefully Inserted")   

    def SearchString(self,word):
        currentNode=self.root
        for i in word:
            node=currentNode.children.get(i)
            if node==None:
                return False
            currentNode=node
        if currentNode.endofString==True:
            return True
        else:
            return False

def deleteString(root,word,index):
    ch=word[index]
    currentNode=root.children.get(ch)
    CanThisNodeBeDeleted=False

    if len(currentNode.children)>1:
        deleteString(currentNode,word,index+1)
        return False 

    if index == len(word) - 1:
        if len(currentNode.children)>=1:
            currentNode.endofString=False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentNode.endofString==True:
        deleteString(currentNode,word,index+1)
        return False
    CanThisNodeBeDeleted= deleteString(currentNode,word,index+1)
    if CanThisNodeBeDeleted==True:
        root.children.pop()
        return True
    else:
        return False        
            
newTrie=Trie()   
newTrie.insertString("APP") 
newTrie.insertString("APPL")  
deleteString(newTrie.root,"APP",0)
print(newTrie.SearchString("APPL"))      