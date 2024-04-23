class SearchInterface:
    def __init__(self, search_class):
        self.search_class = search_class

    def search(self, **kwargs):
        return self.search_class.search(**kwargs)