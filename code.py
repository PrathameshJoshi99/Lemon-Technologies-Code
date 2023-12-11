class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        def _remove_node(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            
            def _add_to_head(self, node):
                node.next = self.head.next
                node.prev = self.head
                self.head.next.prev = node
                self.head.next = node
                
                def get(self, key):
                    if key in self.cache:
                        node = self.cache[key]
                        self._remove_node(node)
                        self._add_to_head(node)
                        return node.value
                        
                        else:
                            return None
                            
                            def put(self, key, value):
                                if key in self.cache:
                                    node = self.cache[key]
                                    node.value = value
                                    self._remove_node(node)
                                    
                                    
                  else:
                        if len(self.cache) >= self.capacity:
                            del self.cache[self.tail.prev.key]
                            self._remove_node(self.tail.prev)
                            
                       
                       node = Node(key, value)
                       self.cache[key] = node
                       
                       self._add_to_head(node)
                       
                       
