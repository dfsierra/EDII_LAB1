class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.height = 0
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.__root = None

    def insert(self, data):     #insertar un nodo
        # caso base
        if not self.__root:
            self.__root = Node(data)   # si el nodo no tiene raiz, el primero se convertira en esta
        # si la raiz del nodo existe
        else:
            self.__insert_data(data, self.__root)

    def remove(self, data):     #Eliminar un nodo
        try:
            if not self.__root:
                print("vacio")
            else:
                self.__remove_data(data, self.__root)
        except TypeError:
            print("error")

    def __insert_data(self, data, node):
        if data < node.data:
            if node.left:
                self.__insert_data(data, node.left)     #Insertar informacion en el nodo
            else:
                node.left = Node(data, node)
                self.__violation_handler(node.left)
        if data > node.data:
            if node.right:
                self.__insert_data(data, node.right)
            else:
                node.right = Node(data, node)
                self.__violation_handler(node.right)

    def __remove_data(self, data, node):          #Eliminar informacion del nodo
        # localizar la informacion del nodo a eliminar
        if data < node.data:
            if node.left:
                self.__remove_data(data, node.left)
        elif data > node.data:
            if node.right:
                self.__remove_data(data, node.right)
        elif data == node.data:
            # Si el nodo no tiene hijos, queda como hoja
          
            if not node.left and not node.right:
                parent_node = node.parent
                if parent_node:
                    if parent_node.left == node:
                        parent_node.left = None
                    elif parent_node.right == node:
                        parent_node.right = None
                # si el nodo es la raiz
                else:
                    self.__root = None
                del node
                self.__violation_handler(parent_node)

            #cuando tiene un hijo izquierdo
            elif node.left and not node.right:
                parent_node = node.parent
               
                if parent_node:
                    if parent_node.left == node:  # nodo a eliminar
                        parent_node.left = node.left
                    elif parent_node.right == node:
                        parent_node.right = node.left
                else:
                    self.__root = node.left
               
                node.left.parent = parent_node
                del node
                self.__violation_handler(parent_node)

            #cuando existe el hijo derecho
            elif node.right and not node.left:
                parent_node = node.parent
               
                if parent_node:
                    if parent_node.left == node:  #nodo a eliminar
                        parent_node.left = node.right
                    elif parent_node.right == node:
                        parent_node.right = node.right
                else:
                    self.__root = node.right
              
                node.right.parent = parent_node
                del node
                self.__violation_handler(parent_node)

            # cuando el nodo tiene 2 hijos
            elif node.left and node.right:
               
                successor_node = self.__find_successor(node.right)
                successor_node.data, node.data = node.data, successor_node.data
                self.__remove_data(successor_node.data, node.right)

    def __find_successor(self, node):
        if node.left:
            return self.__find_successor(node.left)
        return node

    def __violation_handler(self, node):
        while node: 
            node.height = max(self.__calculate_height(node.left), self.__calculate_height(node.right)) + 1
            self.__violation_fix(node)
            node = node.parent  #recorrido desde la raiz

    def __calculate_height(self, node):
       #calcular la altura
        if not node:
            return -1
        return node.height
        print(node.height)

    def __violation_fix(self, node):    #Correcion del nodo para rotarlo luego de una operacion
        
        if self.__balance_factor(node) > 1:
           
            if self.__balance_factor(node.left) < 0: 
                self.__rotate_left(node.left)
            self.__rotate_right(node)
     
        if self.__balance_factor(node) < -1:
          
            if self.__balance_factor(node.right) > 0: 
                self.__rotate_right(node.right)
            self.__rotate_left(node)

    def __balance_factor(self, node): #factor de balance
     
        if not node:
            return 0
        return self.__calculate_height(node.left) - self.__calculate_height(node.right)

    def __rotate_left(self, node):
        temp_right_node = node.right
        t = node.right.left

       
        temp_right_node.left = node
        node.right = t

       #se intercambian las conexiones entre nodos
        temp_parent = node.parent
        temp_right_node.parent = temp_parent
        node.parent = temp_right_node
        if t:
            t.parent = node

         #se intercambian las conexiones entre nodos
        if temp_right_node.parent:   
            if temp_right_node.parent.left == node:
                temp_right_node.parent.left = temp_right_node
            elif temp_right_node.parent.right == node:
                temp_right_node.parent.right = temp_right_node
        #caso raiz
        else:
            self.__root = temp_right_node

        # actualizacion de altura de los nodos
        node.height = max(self.__calculate_height(node.left), self.__calculate_height(node.right)) + 1
        temp_right_node.height = max(self.__calculate_height(temp_right_node.left),
                                     self.__calculate_height(temp_right_node.right)) + 1

        print(f"rotacion a la izquierda sobre el nodo {node.data}...")

    def __rotate_right(self, node):
        temp_left_node = node.left
        t = node.left.right

       #se intercambian las conexiones entre nodos
        temp_left_node.right = node
        node.left = t

        
        temp_parent = node.parent
        temp_left_node.parent = temp_parent
        node.parent = temp_left_node
        if t:
            t.parent = node

          #se intercambian las conexiones entre nodos
        if temp_left_node.parent:
            if temp_left_node.parent.left == node:
                temp_left_node.parent.left = temp_left_node
            elif temp_left_node.parent.right == node:
                temp_left_node.parent.right = temp_left_node
        else:
            self.__root = temp_left_node

     
        node.height = max(self.__calculate_height(node.left), self.__calculate_height(node.right)) + 1
        temp_left_node.height = max(self.__calculate_height(temp_left_node.left),
                                    self.__calculate_height(temp_left_node.right)) + 1

        print(f"rotacion a la derecha sobre el nodo {node.data}...")

    def recorrido(self):
        if self.__root:
            self.__in_order(self.__root)

    def __in_order(self, node):
        """izquierda -> raiz -> derecha"""
        if node.left:
            self.__in_order(node.left)

        print(node.data)

        if node.right:
            self.__in_order(node.right)

    def find(self, data):
        if self.__root:
            return self.__find_data(data, self.__root)
           

    def __find_data(self, data, node):
        try:
            
            if data < node.data:
                if node.left:
                    return self.__find_data(data, node.left)
            elif data > node.data:
                if node.right:
                    return self.__find_data(data, node.right)
            elif data == node.data:
                return True
            return False
        except TypeError:
            return "error"


if __name__ == "__main__":
    tree = AVLTree()

    tree.insert(12)
    tree.insert(24)
    tree.insert(10)
    tree.insert(0)
    tree.insert(-2)
    tree.insert(20)
    tree.insert(21)
    tree.insert(19)
    tree.insert(-6)
    tree.insert(-3)
    tree.insert(-10)
    tree.remove(12)
   
    print(tree.find(-3))
    tree.recorrido()
    