import sys
import os
import weather_widget_gui
from PyQt5 import QtWidgets
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QLineEdit, QFormLayout, QFileDialog, QAction
import search_city_gui
import owm_request
import data_city

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = weather_widget_gui.Ui_MainWindow()
ui.setupUi(window)


def set_weather_icon(label, weather):
    image = Image.open(os.path.join('images', "%s.png" % weather[0]['icon']))
    w, h = image.size
    k = w / h
    height = 51
    width = int(height * k)
    image = image.resize((width, height), Image.ANTIALIAS)
    img_tmp = ImageQt(image.convert('RGBA'))
    pixmap = QPixmap.fromImage(img_tmp)
    label.setPixmap(pixmap)




def start():
    data = owm_request.request_forecast(owm_request.city_id)
    ui.lineEditCity.setText(data['city']['name'] + ' ' + data['city']['country'])
    ui.lineEditDateTime.setText(data['list'][1]['dt_txt'])
    ui.lineEditDegree.setText(str('{0:+3.0f}'.format(data['list'][0]['main']['temp'])) + ' ' + '°C')
    ui.lineEditSky.setText(data['list'][1]['weather'][0]['description'])
    wind = owm_request.get_wind_direction(data['list'][1]['wind']['deg'])
    ui.lineEditWind.setText(str(wind + '{0:2.0f}'.format(data['list'][1]['wind']['speed']) + 'м/с'))
    ui.lineEditHumidity.setText(str(data['list'][1]['main']['humidity']) + '%')
    pressure = '{0:4.0f}'.format(data['list'][1]['main']['pressure'] * 0.75006375541921)
    ui.lineEditPressure.setText(str(pressure + ' мм рт ст'))

    set_weather_icon(ui.labelPicture, data['list'][1]['weather'])

start()

def search_city():
    dialog = QtWidgets.QDialog()
    sc = search_city_gui.Ui_Dialog()
    sc.setupUi(dialog)

    lst_country = data_city.data_country

    def onActivatedId(text2):
        print(text2)
        country = sc.comboBoxCountry.currentText()
        city_id = 0
        for i in data_city.cities:
            if i.get_name() == text2 and i.get_country() == country:
                city_id = i.get_id()
                print (city_id)
        sc.lineEditCityID.setText(str(city_id))

    def onActivatedCity(text1):
        lst_city = sorted(set([val.get_name() for val in data_city.cities if val.get_country() == text1]))
        sc.comboBox.addItems(lst_city)
        return lst_city


    sc.comboBoxCountry.addItems(lst_country)

    sc.comboBoxCountry.activated[str].connect(onActivatedCity)
    sc.comboBox.activated[str].connect(onActivatedId)

    def other_city():
        city_id = sc.lineEditCityID.text()
        print(city_id)
        if city_id == None:
            dialog.accept()
        else:
            data = owm_request.request_forecast(city_id)
            ui.lineEditCity.setText(data['city']['name'] + ' ' + data['city']['country'])
            ui.lineEditDateTime.setText(data['list'][1]['dt_txt'])
            ui.lineEditDegree.setText(str('{0:+3.0f}'.format(data['list'][0]['main']['temp'])) + ' ' + '°C')
            ui.lineEditSky.setText(data['list'][1]['weather'][0]['description'])
            wind = owm_request.get_wind_direction(data['list'][1]['wind']['deg'])
            ui.lineEditWind.setText(str(wind + '{0:2.0f}'.format(data['list'][1]['wind']['speed']) + 'м/с'))
            ui.lineEditHumidity.setText(str(data['list'][1]['main']['humidity']) + '%')
            pressure = '{0:4.0f}'.format(data['list'][1]['main']['pressure'] * 0.75006375541921)
            ui.lineEditPressure.setText(str(pressure + ' мм рт ст'))

            set_weather_icon(ui.labelPicture, data['list'][1]['weather'])
            dialog.close()

    sc.pushButtonCancel.clicked.connect(dialog.reject)
    sc.pushButtonOk.clicked.connect(other_city)

    dialog.exec()



ui.pushButtonSearch.clicked.connect(search_city)

ui.pushButtonUpdate.clicked.connect(start)

window.show()
sys.exit(app.exec_())
