## PNG 파일 참고

##################################################################################################################

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def makeingTree(arr, root, i):
    if(i < len(arr)) :
        root = Node(arr[i])
        root.left = makeingTree(arr, root.left, 2*i + 1)
        root.right = makeingTree(arr, root.right, 2*i + 2)
    return root

root = None

tree = makeingTree(arr, root ,0)

print(tree.data)

##################################################################################################################

# dic_tree = {}

# degree = 0

# while(2 ** degree < len(arr)):
#     degree += 1
# degree += 1

# for i in range(degree):
#     dic_tree[i] = []

# degree = 0
# for i, item in enumerate(arr):
#     index = i + 1
    
#     if index % 2 == 0 :
#         degree += 1

#     dic_tree[degree].append(item)

# print(dic_tree)

##################################################################################################################

 
# for i in range(degree):
#     num = 2 ** i
#     index = 2 ** i
#     dic_tree[i] = [arr[x + index] for x in range(num)]


##################################################################################################################
    
# temp = list(arr)

# temp.append(1)
# print(temp)
# print(arr)

# while(True):
#     i = 0
    


     