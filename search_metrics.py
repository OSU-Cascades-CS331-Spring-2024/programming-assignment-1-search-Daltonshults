class SearchMetrics:

    def __init__(self):
        self.explored_cnt = 0
        self.expanded_cnt = 0
        self.maintained_cnt = 0

    def increment_explored(self):
        self.explored_cnt += 1

    def increment_expanded(self):
        self.expanded_cnt += 1

    def increment_maintained(self):
        self.maintained_cnt += 1

    def get_explored(self):
        return self.explored_cnt
    
    def get_expanded(self):
        return self.expanded_cnt
    
    def get_maintained(self):
        return self.maintained_cnt