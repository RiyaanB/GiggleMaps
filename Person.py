class Person:
    def __init__(self, start_node, end_node):
        self.start = start_node
        self.end = end_node
        self.current_pos = start_node
        self.nodes_visited = set()
        self.nodes_visited.add(start_node)
        self.prev_node = start_node
        self.path = []
        self.next_node = ""

    def set_path(self, ls):
        self.path = ls
        self.next_node = self.path[0]

    def get_next_node(self):
        return self.path.pop(0) if self.path else ""

    def reached(self):
        return self.current_pos == self.end

    def move(self, pos):
        '''
        This method will change current position
        of the person and will also append this
        new position to self.route_taken
        '''
