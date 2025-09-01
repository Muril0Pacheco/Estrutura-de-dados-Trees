# Murilo Pacheco Xavier da Silva - 213390 - C.Computação 4º semestre

from graphviz import Digraph
import random

# classe nó da árvore
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

# classe árvore binária
class BinaryTree:
    def __init__(self):
        self.root = None

    # inserção em BST para manter árvore ordenada
    def insert(self, valor):
        if self.root is None:
            self.root = Node(valor)
        else:
            self._insert(self.root, valor)

    def _insert(self, current, valor):
        if valor < current.valor:
            if current.left is None:
                current.left = Node(valor)
            else:
                self._insert(current.left, valor)
        elif valor > current.valor:
            if current.right is None:
                current.right = Node(valor)
            else:
                self._insert(current.right, valor)

    # travessia in-order: esquerda -> raiz -> direita
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.valor)
            self._inorder(node.right, result)

    # travessia pre-order: raiz -> esquerda -> direita
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.valor)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    # travessia post-order: esquerda -> direita -> raiz
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.valor)

    # graphviz
    def visualize(self, filename="tree"):
        dot = Digraph()
        self._add_nodes(dot, self.root)
        dot.render(filename, format="png", cleanup=True)

    def _add_nodes(self, dot, node):
        if node:
            dot.node(str(node.valor))
            if node.left:
                dot.edge(str(node.valor), str(node.left.valor))
                self._add_nodes(dot, node.left)
            if node.right:
                dot.edge(str(node.valor), str(node.right.valor))
                self._add_nodes(dot, node.right)

if __name__ == "__main__":
    # árvore fixa
    tree_fixed = BinaryTree()
    valores_fixos = [55, 30, 80, 20, 45, 70, 90]
    for v in valores_fixos:
        tree_fixed.insert(v)

    tree_fixed.visualize("tree_fixed")

    print("Árvore fixa:")
    print("in-order:", tree_fixed.inorder())
    print("pre-order:", tree_fixed.preorder())
    print("post-order:", tree_fixed.postorder())
    print()

    # árvore randômica
    tree_random = BinaryTree()
    valores_random = random.sample(range(1, 200), 10)
    for v in valores_random:
        tree_random.insert(v)

    tree_random.visualize("tree_random")

    print("Árvore randômica (valores inseridos):", valores_random)
    print("in-order:", tree_random.inorder())
    print("pre-order:", tree_random.preorder())
    print("post-order:", tree_random.postorder())
