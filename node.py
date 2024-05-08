class CityNode:

    def __init__(self, state, parent, action, path_cost) -> None:
        self._state = state
        self._parent = parent
        self._action = action
        self._path_cost = path_cost

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def get_action(self):
        return self._action

    def set_action(self, action):
        self._action = action

    def get_path_cost(self):
        return self._path_cost

    def set_path_cost(self, path_cost):
        self._path_cost = path_cost

    def increment_path_cost(self, path_cost_increase):
        self._path_cost += path_cost_increase

    def __lt__(self, other):
        return self._path_cost < other.get_path_cost()
    
class CityNodeAStar(CityNode):
    
    def __init__(self, state, parent, action, path_cost, h_score, f_score=0) -> None:
        super().__init__(state, parent, action, path_cost)
        self.f_score = f_score
        self.h_score = h_score

    def get_h_score(self):
        return self.h_score
    
    def get_f_score(self):
        return self.f_score
    
    def __lt__(self, other):
        return self.f_score < other.f_score