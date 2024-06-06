from design import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6 import QtGui
from image_grabber import imageDownloader
import controller
import random
import shutil


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Add button and other triggers here

        self.pushButton_next.clicked.connect(self.get_new_image)
        self.pushButton_save.clicked.connect(self.print_test)
      



    # Add functions for this window here
    
    def print_test(self):
        file_dialogue_id = QFileDialog()
        file_name = "doggy file"+str(random.randrange(0,99999999, 1)) + ".jpg"
        response = file_dialogue_id.getSaveFileName(parent = self, caption = "Select a folder", directory=file_name)
        if (response[0] == ''):
            print("Download cancelled")
            return
        
        # get original image
        source_file = open('image.jpg', 'rb')

        # get file location
        save_path = open(response[0], 'wb')

        # move image to new location
        shutil.copyfileobj(source_file, save_path)
        source_file.close()



    def set_image(self):
        self.label_image.setPixmap(QtGui.QPixmap("image.jpg"))
    def get_new_image(self):
        dog_breed = self.comboBox.currentText()
        image_link = controller.get_doggy_image(dog_breed)
        imageDownloader.downladImageUrl(self, "image.jpg", image_link)
        self.set_image()
    def load_random_dog(self):
        image_link = controller.get_random_dog()
        imageDownloader.downladImageUrl(self, "image.jpg", image_link)
        self.set_image()

app = QApplication([])
window = Window()


window.show()
app.exec()
