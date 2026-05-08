# model.py
# The Model holds application data and performs business logic.
# It has NO dependency on Qt or PySide6.


class TemperatureModel:
    """Stores the current Celsius value and converts it to Fahrenheit."""

    def __init__(self):
        self._celsius = 0.0

    def set_celsius(self, value: float):
        """Store the Celsius temperature."""
        self._celsius = value

    def get_celsius(self) -> float:
        """Return the stored Celsius temperature."""
        return self._celsius

    def celsius_to_fahrenheit(self) -> float:
        """Convert stored Celsius value to Fahrenheit and return the result."""
        return (self._celsius * 9 / 5) + 32
