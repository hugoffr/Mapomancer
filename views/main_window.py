from PySide6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from .map_widget import MapWidget

class MainWindow(QMainWindow):
    def __init__(self, viewmodel):
        super().__init__()
        self.viewmodel = viewmodel
        self._load_ui()
        self._connect_signals()

    def _load_ui(self):
        ui_file = QFile("resources/main_window.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print("Failed to load UI file.")
            return
        
        loader = QUiLoader()
        loaded_ui = loader.load(ui_file, self)
        if not loaded_ui:
            print("Failed to load UI with QUiLoader.")
            return

        ui_file.close()

        self.setCentralWidget(loaded_ui)
        self.ui = loaded_ui

        self.map_widget = MapWidget(self.viewmodel)
        layout = QVBoxLayout()
        layout.addWidget(self.map_widget)
        self.ui.mapContainer.setLayout(layout)

    def _connect_signals(self):
        self.ui.loadButton.clicked.connect(self._load_map)

    def _load_map(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Map", "", "Images (*.png *.jpg *.bmp)")
        if path:
            self.viewmodel.load_map(path)
