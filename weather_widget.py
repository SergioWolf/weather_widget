import sys

import weather_widget_gui
from PyQt5 import QtWidgets
import owm_request

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = weather_widget_gui.Ui_MainWindow()
ui.setupUi(window)

data = owm_request.request_forecast(owm_request.city_id)


ui.lineEditCity.setText(data['city']['name'] + ' ' + data['city']['country'])
ui.lineEditDateTime.setText(data['list'][0]['dt_txt'])
ui.lineEditDegree.setText(str('{0:+3.0f}'.format(data['list'][0]['main']['temp'])) + ' ' + '\xb0' + 'C')
ui.lineEditSky.setText(data['list'][0]['weather'][0]['description'])
wind = owm_request.get_wind_direction(data['list'][0]['wind']['deg'])
ui.lineEditWind.setText(str(wind + '{0:2.0f}'.format(data['list'][0]['wind']['speed']) + " м/с"))
ui.lineEditHumidity.setText(str(data['list'][0]['main']['humidity']) + '%')
pressure = '{0:4.0f}'.format(data['list'][0]['main']['pressure'] * 0.75006375541921)
ui.lineEditPressure.setText(str(pressure + ' мм рт ст'))


window.show()
sys.exit(app.exec_())