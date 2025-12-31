import sys
from PyQt5 import QtWidgets, QtGui
import cv2

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ders 3 - Buton Oluşturma")

    
    # etiket = QtWidgets.QLabel(pencere)
    image="/home/huawei/Documents/internship/Tasks/ocr/1.jpg"
    # etiket2.setPixmap(QtGui.QPixmap(image))
    # etiket2.move(30, 100)
    # etiket.setText("Yazı Alanı")
    # etiket.move(400, 50)

    button = QtWidgets.QPushButton(pencere)
    button.setText("Resmi Göster")

 


    button.move(350, 400)
    pencere.setGeometry(100, 100, 800, 500)

    pencere.show()
    

    sys.exit(app.exec_())

Pencere()    