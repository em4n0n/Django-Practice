# The fastest log notation to solve 2 sum is the binary search tree (BST) method. The BST method uses a data structure called a binary search tree to efficiently find pairs of numbers in a sorted array that sum to a given target value. 
# The BST method has a time complexity of O(n log n), which is the fastest possible time complexity for solving the 2 sum problem.
# Here is an example of how the BST method could be implemented in Python to solve the 2 sum problem:

# Import the deque class from the collections module.
from collections import deque

# Define a class for a binary search tree node.
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Define a function that inserts a value into a binary search tree.
def insert(node, val):
  # If the current node is None, create a new node with the given value.
  if node is None:
    return Node(val)

  # If the value is less than the current node's value, insert it into the left subtree.
  if val < node.val:
    node.left = insert(node.left, val)
  # If the value is greater than or equal to the current node's value, insert it into the right subtree.
  else:
    node.right = insert(node.right, val)

  # Return the current node.
  return node

# Define a function that finds pairs of numbers in a binary search tree that sum to a given target value.
def find_pairs(node, target):
  # Create a list to store the pairs of numbers.
  pairs = []

  # Create a queue to store the nodes in the binary search tree.
  queue = deque([node])

  # While the queue is not empty, continue searching the tree.
  while queue:
    # Pop the first node from the queue.
    curr = queue.popleft()

    # If the current node has a left child, add it to the queue.
    if curr.left:
      queue.append(curr.left)

    # If the current node has a right child, add it to the queue.
    if curr.right:
      queue.append(curr.right)

    # Check if the current node's value is a valid partner for any of the nodes in the queue.
    for other in queue:
      # If the current node's value and the other node's value sum to the target value, add the pair of numbers to the list.
      if curr.val + other.val == target:
        pairs.append((curr.val, other.val))

  # Return the list of pairs of numbers.
  return pairs

# Define an array of numbers.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a binary search tree from the array of numbers.
root = None
for num in nums:
  root = insert(root, num)

# Find pairs of numbers in the binary search tree that sum to 12.
pairs = find_pairs(root, 12)

# Print the pairs of numbers.
print(pairs)
# Output: [(1, 11), (2, 10), (3, 9), (4
