class Node:
    def __init__(self, freq, data, left=None, right=None, huff=None):
        self.freq = freq
        self.data = data
        self.left = left
        self.right = right


def calculate_frequency(input_string):
    frequency = {}

    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    sorted_frequency = sorted(frequency.items(), key=lambda item: (-item[1], -ord(item[0])))
    nodes = [Node(freq, data) for data, freq in sorted_frequency]
    return nodes

def build_huffman_tree(nodes):
    while len(nodes) > 1:
        left = nodes.pop()
        right = nodes.pop()
        freq = left.freq + right.freq
        nodes.append(Node(freq, None, left, right))
        nodes.sort(key=lambda node: node.freq, reverse=True)
    
    return nodes[0]

def generate_huffman_codes(node, bin_string='',huffman_codes={}):
    if node.data is not None:
        huffman_codes[node.data] = bin_string
    if node.left:
        generate_huffman_codes(node.left, bin_string + '0', huffman_codes)
    if node.right:
        generate_huffman_codes(node.right, bin_string + '1', huffman_codes)
    return huffman_codes

if __name__ == "__main__":
    user_input = input("Enter Input: ")
    nodes = calculate_frequency(user_input)
    root = build_huffman_tree(nodes)
    huffman_codes = generate_huffman_codes(root)

    print(huffman_codes)