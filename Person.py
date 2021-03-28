class Person:
    def __init__(self, start_node, end_node, name):
        self.name = name
        self.start = start_node
        self.end = end_node
        self.current_pos = 0
        self.nodes_visited = set()
        self.nodes_visited.add(start_node)
        self.path = [self.start]
        self.next_node = 1
        self.already_reached = False
        self.age = 0
        self.limbo = 0

    def set_path(self, ls):
        self.path = ls
        self.next_node = self.path[0]

    def get_next_node(self):
        return self.path.pop(0) if self.path else ""

    def reached(self):
        return self.path[self.current_pos] == self.end

    def reset(self):
        self.age = 0
        self.limbo = 0
        self.current_pos = 0
        self.next_node = 1
        self.already_reached = False

    def move(self, pos):
        '''
        This method will change current position
        of the person and will also append this
        new position to self.route_taken
        '''
        self.current_pos = pos
        pass
