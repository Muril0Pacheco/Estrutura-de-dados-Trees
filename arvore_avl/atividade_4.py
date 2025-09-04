# Murilo Pacheco Xavier da Silva - 213390 - C.Computação 4º semestre

from graphviz import Digraph
import random

# nó da árvore AVL
class AVLNode:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None
        self.height = 1

# árvore AVL
class AVLTree:
    def __init__(self):
        self.root = None

    # inserção com balanceamento
    def insert(self, valor):
        self.root = self._insert(self.root, valor)

    def _insert(self, node, valor):
        if not node:
            return AVLNode(valor)

        if valor < node.valor:
            node.left = self._insert(node.left, valor)
        elif valor > node.valor:
            node.right = self._insert(node.right, valor)
        else:
            return node  # valores duplicados não são permitidos

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        balance = self._get_balance(node)

        # caso left-left
        if balance > 1 and valor < node.left.valor:
            print(f"Rotação simples à direita no nó {node.valor}")
            return self._right_rotate(node)
        # caso right-right
        if balance < -1 and valor > node.right.valor:
            print(f"Rotação simples à esquerda no nó {node.valor}")
            return self._left_rotate(node)
        # caso left-right
        if balance > 1 and valor > node.left.valor:
            print(f"Rotação dupla esquerda-direita no nó {node.valor}")
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # caso right-left
        if balance < -1 and valor < node.right.valor:
            print(f"Rotação dupla direita-esquerda no nó {node.valor}")
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # busca
    def search(self, valor):
        return self._search(self.root, valor)

    def _search(self, node, valor):
        if not node:
            return False
        if valor == node.valor:
            return True
        elif valor < node.valor:
            return self._search(node.left, valor)
        else:
            return self._search(node.right, valor)

    # remoção com balanceamento
    def delete(self, valor):
        self.root = self._delete(self.root, valor)

    def _delete(self, node, valor):
        if not node:
            return node

        if valor < node.valor:
            node.left = self._delete(node.left, valor)
        elif valor > node.valor:
            node.right = self._delete(node.right, valor)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.valor = temp.valor
            node.right = self._delete(node.right, temp.valor)

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        balance = self._get_balance(node)

        # balanceamento
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # rotação à direita
    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    # rotação à esquerda
    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    # graphviz
    def visualize(self, filename="avl_tree"):
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
    # Demonstração das rotações com valores fixos

    print("Inserção sequência [10, 20, 30] - deve forçar rotação simples à esquerda")
    avl_simple_left = AVLTree()
    for v in [10, 20, 30]:
        avl_simple_left.insert(v)
        avl_simple_left.visualize(f"avl_simple_left_{v}")

    print("\nInserção sequência [10, 30, 20] - deve forçar rotação dupla direita-esquerda")
    avl_double_right_left = AVLTree()
    for v in [10, 30, 20]:
        avl_double_right_left.insert(v)
        avl_double_right_left.visualize(f"avl_double_right_left_{v}")

    # Árvore com 20 valores aleatórios
    avl_random = AVLTree()
    valores_random = random.sample(range(1, 200), 20)
    for v in valores_random:
        avl_random.insert(v)
    avl_random.visualize("avl_random_20")
    print("\nValores aleatórios inseridos:", valores_random)
