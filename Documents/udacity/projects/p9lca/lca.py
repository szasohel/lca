head = None

class Node(object):
  def __init__(self,root):
    self.root = root
    self.right = None
    self.left = None

# Function to insert a new node at the beginning
def push_right(node, new_data):
    new_node = Node(new_data)
    node.right = new_node
    return new_node

# Function to insert a new node at the beginning
def push_left(node, new_data):
    new_node = Node(new_data)
    node.left = new_node
    return new_node

# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(head, n1, n2):
    # Base Case
    if head is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(head.root > n1 and head.root > n2):
        return lca(head.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(head.root < n1 and head.root < n2):
        return lca(head.right, n1, n2)

    return head.root


def question4(T, r, n1, n2):

    if len(T) == 0:
        return "Error! No tree input to work with"
    
    # Implementing Binary Search Tree
    head = Node(r)
    head.left, head.right = None, None
    node_value = 0
    node_list = []
    for elem in T[r]:
        if elem:
            if(node_value>r):
                node_list.append(push_right(head, node_value))
            else:
                node_list.append(push_left(head, node_value))
        node_value += 1

    tmp_node = node_list.pop(0)

    while tmp_node != None:
        node_value = 0
        for elem in T[tmp_node.root]:
            if elem:
                if(node_value>tmp_node.root):
                    node_list.append(push_right(tmp_node, node_value))
                else:
                    node_list.append(push_left(tmp_node, node_value))
            node_value += 1
        if node_list == []:
            break
        else:
            tmp_node = node_list.pop(0)

    return lca(head, n1, n2)

def test4():
    print ("Test 1")
    print(question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4))

    print ("test 2")
    print(question4([],
              3,
              1,
              4))

test4()
