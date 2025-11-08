import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Recursive function to generate Huffman Codes
def get_codes(node, code=""):
    if node is None:
        return
    # If it's a leaf node, print the code
    if not node.left and not node.right:
        print(f"{node.char} -> {code}")
    # Traverse left and right
    get_codes(node.left, code + "0")
    get_codes(node.right, code + "1")

# Main program
print("----- Simple Huffman Coding -----")

n = int(input("Enter number of characters: "))
chars = []
freqs = []

for i in range(n):
    ch = input(f"Enter character {i+1}: ")
    f = int(input(f"Enter frequency of '{ch}': "))
    chars.append(ch)
    freqs.append(f)

# Create heap of nodes
heap = [Node(chars[i], freqs[i]) for i in range(n)]
heapq.heapify(heap)

# Build Huffman Tree
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    new_node = Node(left.char + right.char, left.freq + right.freq)
    new_node.left = left
    new_node.right = right
    heapq.heappush(heap, new_node)

# Print Huffman Codes
print("\nHuffman Codes for each character:")
print("--------------------------------")
get_codes(heap[0])
