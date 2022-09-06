#Problema y codigo recuperados de: https://www.techiedelight.com/invert-alternate-levels-perfect-binary-tree/
 #a. Invertir niveles alternos de un arbol binario
 #b. Elegi el problema porque en el semestre pasado una de las cosas mas dificiles para mi fue el invertir una linked list y me dio curiosidad que tan dificil seria hacerlo
 #   con un arbol binario.

from collections import deque


# Clase
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


# Nivel
def levelOrderTraversal(root):

	if root is None:
		return

	# Creamos una queue con el nodo raiz
	queue = deque()
	queue.append(root)

	# hacemos un ciclo hasta que la lista este vacia
	while queue:

		# hacemos que para cada nodo en cola se pongan en la cola sus nodos derecho e izquierdo no vacios
		curr = queue.popleft()
		print(curr.data, end=' ')

		if curr.left:
			queue.append(curr.left)

		if curr.right:
			queue.append(curr.right)


# Funcion recursiva para invertir los niveles del arbol
# Usamos preorden
def invertBinaryTree(first, second, level):

	# Retornamos si esta vacio
	if first is None or second is None:
		return

	# cambiamos los datos si es par
	if level:
		temp = first.data
		first.data = second.data
		second.data = temp

	# llamamos la funcion con el hijo izquierdo del primero y el hijo deerecho del segundo
	invertBinaryTree(first.left, second.right, not level)

	# Hacemos lo mismo al reves
	invertBinaryTree(first.right, second.left, not level)


def invertBT(root):

	# funcion para llamar la reversion
	if not root:
		return

	invertBinaryTree(root.left, root.right, True)


if __name__ == '__main__':

	root = None

	''' Construct the following tree
				  1
			   /     \
			 /         \
		   2             3
		 /   \         /   \
		4     5       6     7
	  /  \    / \    / \    / \
	 8    9  10 11 12  13  14 15

	'''

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	root.left.left.left = Node(8)
	root.left.left.right = Node(9)
	root.left.right.left = Node(10)
	root.left.right.right = Node(11)
	root.right.left.left = Node(12)
	root.right.left.right = Node(13)
	root.right.right.left = Node(14)
	root.right.right.right = Node(15)

	invertBT(root)
	levelOrderTraversal(root)
