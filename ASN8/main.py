import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from asn8_ui import Ui_root


class MainWindow(QMainWindow, Ui_root):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect buttons to event handlers
        self.btnS.clicked.connect(self.submit)
        self.btnR.clicked.connect(self.reset)
        self.btnQ.clicked.connect(self.quit_app)

    def submit(self):
        first = self.entFirst.text().strip()
        last = self.entLast.text().strip()
        email = self.entEmail.text().strip()
        phone = self.entPhone.text().strip()

        # Validate required fields
        if not first or not last:
            QMessageBox.warning(self, "Validation Error",
                                "First Name and Last Name are required.")
            return

        # Display submitted data
        msg = (f"First Name: {first}\n"
               f"Last Name: {last}\n"
               f"Email: {email}\n"
               f"Phone: {phone}")
        QMessageBox.information(self, "Submitted Data", msg)

    def reset(self):
        self.entFirst.clear()
        self.entLast.clear()
        self.entEmail.clear()
        self.entPhone.clear()

    def quit_app(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
