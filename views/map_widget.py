from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPainter, QColor, QMouseEvent
from PySide6.QtCore import Qt, QPoint

class MapWidget(QLabel):
    def __init__(self, viewmodel):
        super().__init__()
        self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.setMinimumSize(600, 400)
        self.viewmodel = viewmodel
        self.pixmap_img = None

        # Bind ViewModel signals
        self.viewmodel.map_loaded.connect(self.set_map_image)
        self.viewmodel.points_updated.connect(self.update)

    def set_map_image(self, pixmap):
        self.pixmap_img = pixmap
        self.setPixmap(pixmap)
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.viewmodel.add_point(event.position().toPoint())
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.pixmap_img:
            painter = QPainter(self)
            painter.setPen(Qt.red)
            painter.setBrush(QColor(255, 0, 0, 180))
            for point in self.viewmodel.get_points():
                painter.drawEllipse(point, 5, 5)
            painter.end()
