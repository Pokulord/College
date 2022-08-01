from  main import *

class UIFunction(MainWindow):

    def toggleMenu(self,maxWidth,enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standart = 150

            if width == standart:
                widthExtended = maxExtend
            else:
                widthExtended = standart

            self.animation = QPropertyAnimation(self.ui.frame_left_menu,b"minimumWidth")
            self.animation.setDuration(200)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()