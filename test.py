# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.


# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

# "abccccdd"
# a: 1 b :1 c: 4 d :2

# 'abbb'


def maxLengthPali(s):
    
    letterToCount = {}
    hasSingle = False
    
    for letter in s:
        
        num = letterToCount.get(letter, 0)
        letterToCount[letter] = num + 1
        
# letterToCount -> . a: 1 b :1 c: 4 d :2
    
    totalCount = 0
    
    for k,v in letterToCount:
        
        if v % 2 == 1:
            hasSingle = True
        else:
            if v % 2 == 0:
                totalCount = totalCount + v
            else:
                totalCount = totalCount + v - 1          
    if hasSingle:
        return totalCount + 1
    else:
        return totalCount

public int longestPalindrome(String s) {
    if(s==null || s.length()==0) return 0;
    HashSet<Character> hs = new HashSet<Character>();
    int count = 0;
    for(int i=0; i<s.length(); i++){
        if(hs.contains(s.charAt(i))){
            hs.remove(s.charAt(i));
            count++;
        }else{
            hs.add(s.charAt(i));
        }
    }
    if(!hs.isEmpty()) return count*2+1;
    return count*2;
}




# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [ 
#    [5,4,11,2],
#    [5,8,4,5]
# ]




# sum = 5
# path:5,8,4,
# res:[[5,4,11,2],[5,8,4,5]]


def findPath(root, sum):
    if not root:
        return None
    
    path = []
    res =[]
    
    dfs(root, path, res, sum)
    
    return res
        
    
def dfs(node, path, res, sum):
    if not node.left and not node.right:
        if node.val == sum:
            newPath = path.copy()
            newPath.append(node.val)
            res.append(newPath)
        
        return
    
    if sum - node.val >= 0: 
        if node.left: 
            path.append(node.val)
            dfs(node.left, path, res, sum - node.val)
            path.pop()

        if node.right:
            path.append(node.val)
            dfs(node.right, path, res, sum - node.val)
            path.pop()
        
        
# 1.root = none
# 2.root = one node
# 3.non balance tree, balance tree -》 只有一条线的时候，timecomplexity很奇怪
# 4.tree has alot of node ->测试memory能不能吼得住

# 考虑负的值
        
    
    
        
    
    
