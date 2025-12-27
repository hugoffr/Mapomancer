from PySide6.QtCore import QPoint

class MapData:
    def __init__(self):
        self.image_path = None
        self.points = []

    def load_image(self, path):
        self.image_path = path
        self.points = []

    def add_point(self, point: QPoint):
        self.points.append(point)

    def get_points(self):
        return self.points
