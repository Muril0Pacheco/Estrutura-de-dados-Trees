# Murilo Pacheco Xavier da Silva - 213390 - C.Computação 4º semestre

from graphviz import Digraph
import random

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

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

    def search(self, valor):
        return self._search(self.root, valor)

    def _search(self, current, valor):
        if current is None:
            return False
        if valor == current.valor:
            return True
        elif valor < current.valor:
            return self._search(current.left, valor)
        else:
            return self._search(current.right, valor)

    def delete(self, valor):
        self.root = self._delete(self.root, valor)

    def _delete(self, current, valor):
        if current is None:
            return current

        if valor < current.valor:
            current.left = self._delete(current.left, valor)
        elif valor > current.valor:
            current.right = self._delete(current.right, valor)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            temp = self._min_value_node(current.right)
            current.valor = temp.valor
            current.right = self._delete(current.right, temp.valor)

        return current

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def depth(self, valor):
        return self._depth(self.root, valor, 0)

    def _depth(self, current, valor, nivel):
        if current is None:
            return -1
        if current.valor == valor:
            return nivel
        elif valor < current.valor:
            return self._depth(current.left, valor, nivel + 1)
        else:
            return self._depth(current.right, valor, nivel + 1)

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
    # árvore com valores fixos
    bst = BinarySearchTree()
    valores_fixos = [55, 30, 80, 20, 45, 70, 90]
    for v in valores_fixos:
        bst.insert(v)

    bst.visualize("arvore_fixa")

    print("busca pelo valor 45:", bst.search(45))

    bst.delete(30)
    bst.visualize("arvore_fixa_delete")

    bst.insert(60)
    bst.visualize("arvore_fixa_insert")

    print("altura da árvore fixa:", bst.height())
    print("profundidade do nó 45:", bst.depth(45))

    # árvore com valores aleatórios
    bst_random = BinarySearchTree()
    valores_random = random.sample(range(1, 200), 15)
    for v in valores_random:
        bst_random.insert(v)

    bst_random.visualize("arvore_random")
    print("altura da árvore aleatória:", bst_random.height())
