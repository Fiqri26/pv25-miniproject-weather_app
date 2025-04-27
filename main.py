import sys
import requests
from datetime import datetime
from PyQt5 import QtWidgets, QtGui
from weather_app import Ui_Form

class WeatherApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.update_date()
        self.ui.comboBox_suhu.setCurrentIndex(-1)
        self.hide_weather_info()

        self.ui.btn_search.clicked.connect(self.search_weather)
        self.ui.btn_exit.clicked.connect(self.exit_app)
        self.ui.checkBox_info.stateChanged.connect(self.handle_checkbox)

    def hide_weather_info(self):
        self.ui.label_humidity.setVisible(False)
        self.ui.label_wind.setVisible(False)
        self.ui.label_pressure.setVisible(False)
        self.ui.label_cloudiness.setVisible(False)

        self.ui.label_kosong3.setVisible(False)
        self.ui.label_kosong4.setVisible(False)
        self.ui.label_kosong5.setVisible(False)
        self.ui.label_kosong6.setVisible(False)

    def show_weather_info(self):
        self.ui.label_humidity.setVisible(True)
        self.ui.label_wind.setVisible(True)
        self.ui.label_pressure.setVisible(True)
        self.ui.label_cloudiness.setVisible(True)

        self.ui.label_kosong3.setVisible(True)
        self.ui.label_kosong4.setVisible(True)
        self.ui.label_kosong5.setVisible(True)
        self.ui.label_kosong6.setVisible(True)

    def handle_checkbox(self):
        if self.ui.checkBox_info.isChecked():
            location = self.ui.search.text().strip()
            temperature_unit = self.ui.comboBox_suhu.currentText().strip()

            if not location or not temperature_unit:
                QtWidgets.QMessageBox.warning(self, "Warning",
                    "Please fill in the location and select a temperature unit first!")
                self.ui.checkBox_info.setChecked(False)
                return

            self.show_weather_info()
        else:
            self.hide_weather_info()

    def search_weather(self):
        location = self.ui.search.text().strip()
        temperature_unit = self.ui.comboBox_suhu.currentText().strip()

        if not location:
            QtWidgets.QMessageBox.warning(self, "Warning", "Location cannot be empty, please type a location!")
            return

        if not temperature_unit:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a temperature unit (Celsius or Fahrenheit).")
            return

        try:
            API_KEY = "2a7b91cdb2e4fbdeabccc07ec0a15dcd"

            if temperature_unit == "Celsius":
                units = "metric"
                satuan_suhu = "°C"
            elif temperature_unit == "Fahrenheit":
                units = "imperial"
                satuan_suhu = "°F"
            else:
                units = "metric"
                satuan_suhu = "°C"

            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units={units}"
            response = requests.get(url)
            data = response.json()

            if str(data.get("cod")) != "200":
                raise Exception("Oops! We couldn't find that location, please try again.")

            weather = data["weather"][0]["main"]
            icon_code = data["weather"][0]["icon"]
            temp = data["main"]["temp"]  #
            min_temp = data["main"]["temp_min"]
            max_temp = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            pressure = data["main"]["pressure"]
            cloudiness = data["clouds"]["all"]

            self.ui.label_cuaca.setText(weather)
            self.update_weather_icon(icon_code)

            self.ui.label_kosong1.setText(f"{min_temp} {satuan_suhu}")
            self.ui.label_kosong2.setText(f"{max_temp} {satuan_suhu}")
            self.ui.label_kosong3.setText(f"{humidity} %")
            self.ui.label_kosong4.setText(f"{wind_speed} m/s")
            self.ui.label_kosong5.setText(f"{pressure} hPa")
            self.ui.label_kosong6.setText(f"{cloudiness} %")

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def update_weather_icon(self, icon_code):
        url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        image = QtGui.QImage()
        image.loadFromData(requests.get(url).content)
        pixmap = QtGui.QPixmap(image)

        self.ui.logo2.setPixmap(pixmap)
        self.ui.logo2.setScaledContents(True)

    def update_date(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%A, %d %B %Y")
        self.ui.label_date.setText(formatted_date)

    def exit_app(self):
        reply = QtWidgets.QMessageBox.question(self, 'Exit',
            "Are you sure you want to exit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)

        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.qApp.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
