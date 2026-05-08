# main.py
# Application entry point.
# Initializes QApplication, creates the Controller (which owns the View),
# shows the main window, and starts the Qt event loop.

import sys

from PySide6.QtWidgets import QApplication

from controller import TemperatureController


def main():
    app = QApplication(sys.argv)
    window = TemperatureController()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
