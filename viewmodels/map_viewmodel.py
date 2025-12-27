from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QPixmap
from models.map_data import MapData

class MapViewModel(QObject):
    map_loaded = Signal(QPixmap)
    points_updated = Signal()

    def __init__(self):
        super().__init__()
        self.model = MapData()
        self.pixmap = None

    def load_map(self, path):
        self.pixmap = QPixmap(path)
        if self.pixmap.isNull():
            return
        self.model.load_image(path)
        self.map_loaded.emit(self.pixmap)
        self.points_updated.emit()

    def add_point(self, point):
        self.model.add_point(point)
        self.points_updated.emit()

    def get_points(self):
        return self.model.get_points()
