from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import pyqtSignal, QFileInfo, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSoundEffect
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QSlider, QGridLayout, QPushButton)
from PyQt5.QtGui import QPixmap
import os
import sys


class Button(QPushButton):
    entered = pyqtSignal()
    leaved = pyqtSignal()

    def enterEvent(self, event):
        super().enterEvent(event)
        self.entered.emit()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.leaved.emit()




class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"jesus25.ui", self)
        self.first()
        
        
        self.hl = QSoundEffect()
        self.hl.setSource(QUrl.fromLocalFile("sounds/hl.wav"))

        self.mocha_sound = QSoundEffect()
        self.mocha_sound.setSource(QUrl.fromLocalFile("sounds/moch.wav"))
        
        self.player = QMediaPlayer()
        self.slid.valueChanged[int].connect(self.change_volume)
        self.slid.setValue(100)
        self.volume = self.slid.value()

        self.music1.toggled.connect(self.muzic)
        self.music2.toggled.connect(self.r)
        self.music3.toggled.connect(self.t)
        self.music4.toggled.connect(self.y)
        self.stop.toggled.connect(self.pop)
        self.player.setVolume(self.volume)

        self.ton = Button(self)
        self.ton.setGeometry(470, 470, 121, 71)
        self.ton.setText("ХЛЭБ")

        self.utton = Button(self)
        self.utton.setGeometry(130, 470, 121, 71)
        self.utton.setText('МОЧА')

        self.ton.entered.connect(self.hle)
        self.ton.entered.connect(self.hl.play)
        self.ton.leaved.connect(self.first)

        self.utton.entered.connect(self.moch)
        self.utton.entered.connect(self.mocha_sound.play)
        self.utton.leaved.connect(self.first)

    def change_volume(self, value):
        self.player.setVolume(value)

    def muzic(self, selected):
        if selected:
            self.player.setMedia(
                QMediaContent(QUrl.fromLocalFile(
                    r"sounds/KHava_nagila.mp3")))
            self.player.play()

    def r(self, selected):
        if selected:
            self.player.setMedia(
                QMediaContent(QUrl.fromLocalFile(
                    r"sounds/Evreiskaya_narodnaya.mp3")))
            self.player.play()

    def t(self, selected):
        if selected:
            self.player.setMedia(
                QMediaContent(QUrl.fromLocalFile(
                    r"sounds/SHalom-Alejjkhem.mp3")))
            self.player.play()

    def y(self, selected):
        if selected:
            self.player.setMedia(
                QMediaContent(QUrl.fromLocalFile(
                    r"sounds/Tum-balalajjka.mp3")))
            self.player.play()

    def pop(self, selected):
        if selected:
            self.player.stop()



    def hle(self):
        self.jhleb.show()
        self.jhleb.raise_()
        self.jmoch.hide()
        self.jnormal.hide()
        self.hleb.raise_()
        self.mocha.raise_()
        self.slid.raise_()

    def moch(self):
        self.jmoch.show()
        self.jnormal.hide()
        self.jhleb.hide()
        self.hleb.raise_()
        self.mocha.raise_()
        self.slid.raise_()

    def first(self):
        self.jmoch.hide()
        self.jnormal.show()
        self.jhleb.hide()
        self.hleb.raise_()
        self.mocha.raise_()
        self.slid.raise_()


if __name__ == "__main__":
    tt = QApplication([])
    app = QApplication(sys.argv)
    rt = App()
    rt.show()
    sys.exit(app.exec())