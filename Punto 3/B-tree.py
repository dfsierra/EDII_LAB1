# Realizar un algoritmo que le permita hacer operaciones basicas como Buscar e insertar en un arbol B.


# Crear el nodo
class BTreeNode:
  def __init__(self, leaf=False):
    self.leaf = leaf
    self.keys = []
    self.child = []

class BTree:
  def __init__(self, t): #Constructor
    self.root = BTreeNode(True)
    self.t = t

    # Insertar
  def insertar(self, k):
    root = self.root
    if len(root.keys) == (2 * self.t) - 1:
      temp = BTreeNode()
      self.root = temp
      temp.child.insert(0, root)
      self.dividir(temp, 0)
      self.insertar_nonfull(temp, k)
    else:
      self.insertar_nonfull(root, k)

    # Insertar nonfull
  def insertar_nonfull(self, x, k):
    i = len(x.keys) - 1
    if x.leaf:
      x.keys.append((None, None))
      while i >= 0 and k[0] < x.keys[i][0]:
        x.keys[i + 1] = x.keys[i]
        i -= 1
      x.keys[i + 1] = k
    else:
      while i >= 0 and k[0] < x.keys[i][0]:
        i -= 1
      i += 1
      if len(x.child[i].keys) == (2 * self.t) - 1:
        self.dividir(x, i)
        if k[0] > x.keys[i][0]:
          i += 1
      self.insertar_nonfull(x.child[i], k)

    # Dividir
  def dividir(self, x, i):
    t = self.t
    y = x.child[i]
    z = BTreeNode(y.leaf)
    x.child.insert(i + 1, z)
    x.keys.insert(i, y.keys[t - 1])
    z.keys = y.keys[t: (2 * t) - 1]
    y.keys = y.keys[0: t - 1]
    if not y.leaf:
      z.child = y.child[t: 2 * t]
      y.child = y.child[0: t - 1]

  # Mostrar el arbol
  def print_tree(self, x, l=0):
    print("Level ", l, " ", len(x.keys), end=":")
    for i in x.keys:
      print(i, end=" ")
    print()
    l += 1
    if len(x.child) > 0:
      for i in x.child:
        self.print_tree(i, l)

  # Buscar
  def search_key(self, k, x=None):
    if x is not None:
      i = 0
      while i < len(x.keys) and k > x.keys[i][0]:
        i += 1
      if i < len(x.keys) and k == x.keys[i][0]:
        return (x, i)
      elif x.leaf:
        return None
      else:
        return self.search_key(k, x.child[i])
      
    else:
      return self.search_key(k, self.root)


def main():
  B = BTree(3)

  for i in range(10):
    B.insertar((i, 2 * i))

  B.print_tree(B.root)
  print("------------------------------------------")
  B.insertar((20, 15))
  B.insertar((120, 3))
  B.insertar((45, 9))
  B.insertar((110, 99))
  B.print_tree(B.root)


  if B.search_key(8) is not None:
    print("\Encontrado")
  else:
    print("\nNo existe")


if __name__ == '__main__':
  main()