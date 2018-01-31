class Stage:
    # layout is expected to be a 2D array
    def __init__(self, layout=None):
        self.layout = layout
        self.width = len(layout)
        self.height = len(layout[0])
