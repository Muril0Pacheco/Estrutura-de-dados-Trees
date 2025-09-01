# Murilo Pacheco Xavier da Silva - 213390 - C.Computação 4º semestre


from graphviz import Digraph
import random

# nó da árvore
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value   # operador (+, -, *, /) ou número
        self.left = left     # nó filho da esquerda
        self.right = right   # nó filho da direita

# árvore fixa
# expressão: ((7 + 3) * (5 - 2)) / (10 * 20)

def build_fixed_tree():
    # folhas
    n7 = Node("7")
    n3 = Node("3")
    n5 = Node("5")
    n2 = Node("2")
    n10 = Node("10")
    n20 = Node("20")

    # operadores internos
    plus = Node("+", n7, n3)
    minus = Node("-", n5, n2)
    mult_left = Node("*", plus, minus)
    mult_right = Node("*", n10, n20)

    # raiz (divisão)
    root = Node("/", mult_left, mult_right)
    return root

# árvore randômica
# gera expressão aleatória com 2 operadores e 3 operandos

def build_random_tree():
    # operandos possíveis 
    operands = [str(random.randint(1, 20)) for _ in range(3)]
    # operadores possíveis
    operators = random.sample(["+", "-", "*", "/"], 2)

    # montando árvore aleatória simples
    left = Node(operators[0], Node(operands[0]), Node(operands[1]))
    root = Node(operators[1], left, Node(operands[2]))
    return root



# Graphviz
def visualize_tree(root, filename="tree"):

    dot = Digraph()

    def add_nodes_edges(node):
        if node is None:
            return
        # cria nó com ID único baseado no endereço de memória
        dot.node(str(id(node)), node.value)
        if node.left:
            dot.edge(str(id(node)), str(id(node.left)))
            add_nodes_edges(node.left)
        if node.right:
            dot.edge(str(id(node)), str(id(node.right)))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render(filename, format="png", cleanup=True)

if __name__ == "__main__":
    # árvore fixa
    fixed_tree = build_fixed_tree()
    visualize_tree(fixed_tree, "fixed_tree")

    # árvore randômica
    random_tree = build_random_tree()
    visualize_tree(random_tree, "random_tree")
