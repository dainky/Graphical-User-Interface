# controller.py
# The Controller connects signals from the View to logic in the Model,
# and updates the View when the Model changes.

from PySide6.QtWidgets import QMainWindow

from model import TemperatureModel
from view import Ui_MainWindow


class TemperatureController(QMainWindow):
    """Acts as the glue between the View (Ui_MainWindow) and the Model."""

    def __init__(self):
        super().__init__()

        # Set up the UI (View)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # Create the Model
        self._model = TemperatureModel()

        # Connect signals to slots
        self._ui.convertButton.clicked.connect(self._on_convert)
        self._ui.inputLineEdit.returnPressed.connect(self._on_convert)

    # ------------------------------------------------------------------
    # Slots
    # ------------------------------------------------------------------

    def _on_convert(self):
        """Read input, update Model, then refresh the View."""
        raw_input = self._ui.inputLineEdit.text().strip()

        # Validate input at the boundary
        try:
            celsius_value = float(raw_input)
        except ValueError:
            self._ui.errorLabel.setText("Please enter a valid number.")
            self._ui.resultLabel.setText("Result will appear here")
            return

        # Clear any previous error
        self._ui.errorLabel.setText("")

        # Update Model
        self._model.set_celsius(celsius_value)

        # Retrieve result from Model and update View
        fahrenheit = self._model.celsius_to_fahrenheit()
        self._ui.resultLabel.setText(
            f"{celsius_value:.2f} °C  =  {fahrenheit:.2f} °F"
        )
