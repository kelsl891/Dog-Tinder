# Form implementation generated from reading ui file 'Dog_Tinder_2.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 1100)
        MainWindow.setMinimumSize(QtCore.QSize(900, 1100))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, -1, 901, 1055))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_image = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_image.setMaximumSize(QtCore.QSize(900, 600))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("../../../Downloads/faaba8fb-a33a-431d-870c-7d49957652d3.jpg"))
        self.label_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 1, 0, 1, 3)
        self.pushButton_save = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 2, 0, 1, 1)
        self.pushButton_next = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout.addWidget(self.pushButton_next, 2, 2, 1, 1)
        self.label_title = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 3)
        self.comboBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dog Tinder"))
        self.pushButton_save.setText(_translate("MainWindow", "Save Image"))
        self.pushButton_next.setText(_translate("MainWindow", "Next Image"))
        self.label_title.setText(_translate("MainWindow", "Dog Tinder"))
        self.comboBox.setItemText(0, _translate("MainWindow", "affenpinscher"))
        self.comboBox.setItemText(1, _translate("MainWindow", "african"))
        self.comboBox.setItemText(2, _translate("MainWindow", "airedale"))
        self.comboBox.setItemText(3, _translate("MainWindow", "akita"))
        self.comboBox.setItemText(4, _translate("MainWindow", "appenzeller"))
        self.comboBox.setItemText(5, _translate("MainWindow", "australian"))
        self.comboBox.setItemText(6, _translate("MainWindow", "basenji"))
        self.comboBox.setItemText(7, _translate("MainWindow", "beagle"))
        self.comboBox.setItemText(8, _translate("MainWindow", "bluetick"))
        self.comboBox.setItemText(9, _translate("MainWindow", "borzoi"))
        self.comboBox.setItemText(10, _translate("MainWindow", "bouvier"))
        self.comboBox.setItemText(11, _translate("MainWindow", "boxer"))
        self.comboBox.setItemText(12, _translate("MainWindow", "brabancon"))
        self.comboBox.setItemText(13, _translate("MainWindow", "briard"))
        self.comboBox.setItemText(14, _translate("MainWindow", "buhund"))
        self.comboBox.setItemText(15, _translate("MainWindow", "bulldog"))
        self.comboBox.setItemText(16, _translate("MainWindow", "bullterrier"))
        self.comboBox.setItemText(17, _translate("MainWindow", "cattledog"))
        self.comboBox.setItemText(18, _translate("MainWindow", "chihuahua"))
        self.comboBox.setItemText(19, _translate("MainWindow", "chow"))
        self.comboBox.setItemText(20, _translate("MainWindow", "clumber"))
        self.comboBox.setItemText(21, _translate("MainWindow", "cockapoo"))
        self.comboBox.setItemText(22, _translate("MainWindow", "collie"))
        self.comboBox.setItemText(23, _translate("MainWindow", "coonhound"))
        self.comboBox.setItemText(24, _translate("MainWindow", "corgi"))
        self.comboBox.setItemText(25, _translate("MainWindow", "cotondetulear"))
        self.comboBox.setItemText(26, _translate("MainWindow", "dashshund"))
        self.comboBox.setItemText(27, _translate("MainWindow", "dalmation"))
        self.comboBox.setItemText(28, _translate("MainWindow", "dane"))
        self.comboBox.setItemText(29, _translate("MainWindow", "deerhound"))
        self.comboBox.setItemText(30, _translate("MainWindow", "dhole"))
        self.comboBox.setItemText(31, _translate("MainWindow", "dingo"))
        self.comboBox.setItemText(32, _translate("MainWindow", "doberman"))
        self.comboBox.setItemText(33, _translate("MainWindow", "elkhound"))
        self.comboBox.setItemText(34, _translate("MainWindow", "eskimo"))
        self.comboBox.setItemText(35, _translate("MainWindow", "finnish"))
        self.comboBox.setItemText(36, _translate("MainWindow", "frise"))
        self.comboBox.setItemText(37, _translate("MainWindow", "germanshepherd"))
        self.comboBox.setItemText(38, _translate("MainWindow", "greyhound"))
        self.comboBox.setItemText(39, _translate("MainWindow", "groenedael"))
        self.comboBox.setItemText(40, _translate("MainWindow", "havanese"))
        self.comboBox.setItemText(41, _translate("MainWindow", "hound"))
        self.comboBox.setItemText(42, _translate("MainWindow", "husky"))
        self.comboBox.setItemText(43, _translate("MainWindow", "keeshond"))
        self.comboBox.setItemText(44, _translate("MainWindow", "kelpie"))
        self.comboBox.setItemText(45, _translate("MainWindow", "komondor"))
        self.comboBox.setItemText(46, _translate("MainWindow", "kuvasz"))
        self.comboBox.setItemText(47, _translate("MainWindow", "labradoodle"))
        self.comboBox.setItemText(48, _translate("MainWindow", "labrador"))
        self.comboBox.setItemText(49, _translate("MainWindow", "leonberg"))
        self.comboBox.setItemText(50, _translate("MainWindow", "lhasa"))
        self.comboBox.setItemText(51, _translate("MainWindow", "malamute"))
        self.comboBox.setItemText(52, _translate("MainWindow", "malinois"))
        self.comboBox.setItemText(53, _translate("MainWindow", "maltese"))
        self.comboBox.setItemText(54, _translate("MainWindow", "mastiff"))
        self.comboBox.setItemText(55, _translate("MainWindow", "mexicanhairless"))
        self.comboBox.setItemText(56, _translate("MainWindow", "mix"))
        self.comboBox.setItemText(57, _translate("MainWindow", "mountain"))
        self.comboBox.setItemText(58, _translate("MainWindow", "newfoundland"))
        self.comboBox.setItemText(59, _translate("MainWindow", "otterhound"))
        self.comboBox.setItemText(60, _translate("MainWindow", "ovcharka"))
        self.comboBox.setItemText(61, _translate("MainWindow", "papillon"))
        self.comboBox.setItemText(62, _translate("MainWindow", "pekinese"))
        self.comboBox.setItemText(63, _translate("MainWindow", "pembroke"))
        self.comboBox.setItemText(64, _translate("MainWindow", "pinscher"))
        self.comboBox.setItemText(65, _translate("MainWindow", "pitbull"))
        self.comboBox.setItemText(66, _translate("MainWindow", "pointer"))
        self.comboBox.setItemText(67, _translate("MainWindow", "pomeranian"))
        self.comboBox.setItemText(68, _translate("MainWindow", "poodle"))
        self.comboBox.setItemText(69, _translate("MainWindow", "pug"))
        self.comboBox.setItemText(70, _translate("MainWindow", "puggle"))
        self.comboBox.setItemText(71, _translate("MainWindow", "pyrenees"))
        self.comboBox.setItemText(72, _translate("MainWindow", "redbone"))
        self.comboBox.setItemText(73, _translate("MainWindow", "retriever"))
        self.comboBox.setItemText(74, _translate("MainWindow", "ridgeback"))
        self.comboBox.setItemText(75, _translate("MainWindow", "rottweiler"))
        self.comboBox.setItemText(76, _translate("MainWindow", "saluki"))
        self.comboBox.setItemText(77, _translate("MainWindow", "samoyed"))
        self.comboBox.setItemText(78, _translate("MainWindow", "schipperke"))
        self.comboBox.setItemText(79, _translate("MainWindow", "schnauzer"))
        self.comboBox.setItemText(80, _translate("MainWindow", "segugio"))
        self.comboBox.setItemText(81, _translate("MainWindow", "setter"))
        self.comboBox.setItemText(82, _translate("MainWindow", "sharpei"))
        self.comboBox.setItemText(83, _translate("MainWindow", "sheepdog"))
        self.comboBox.setItemText(84, _translate("MainWindow", "shiba"))
        self.comboBox.setItemText(85, _translate("MainWindow", "shihtzu"))
        self.comboBox.setItemText(86, _translate("MainWindow", "spaniel"))
        self.comboBox.setItemText(87, _translate("MainWindow", "spitz"))
        self.comboBox.setItemText(88, _translate("MainWindow", "springer"))
        self.comboBox.setItemText(89, _translate("MainWindow", "stbernard"))
        self.comboBox.setItemText(90, _translate("MainWindow", "terrier"))
        self.comboBox.setItemText(91, _translate("MainWindow", "tervuren"))
        self.comboBox.setItemText(92, _translate("MainWindow", "vizsla"))
        self.comboBox.setItemText(93, _translate("MainWindow", "waterdog"))
        self.comboBox.setItemText(94, _translate("MainWindow", "weimaraner"))
        self.comboBox.setItemText(95, _translate("MainWindow", "whippet"))
        self.comboBox.setItemText(96, _translate("MainWindow", "wolfhound"))