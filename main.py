import sys
from PySide6.QtWidgets import QApplication
from viewmodels.map_viewmodel import MapViewModel
from views.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    viewmodel = MapViewModel()
    window = MainWindow(viewmodel)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
