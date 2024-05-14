from PySide2 import QtWidgets, QtGui


class Fenetre(object):
    def setup_ui(self, fenetre):
        fenetre.setWindowTitle("YoutubeDownload")
        self.layout_principale = QtWidgets.QVBoxLayout(fenetre)
        self.h_layout = QtWidgets.QHBoxLayout()
        self.layout_horizontal = QtWidgets.QHBoxLayout()
        self.layout_horizontal_titre = QtWidgets.QHBoxLayout()
        chemin_image = R"image\youtube-logo-png-31792.png"
        self.label = QtWidgets.QLabel()
        self.image = QtGui.QPixmap(chemin_image)
        self.image.setDevicePixelRatio(5)
        self.label.setPixmap(self.image)

        self.le_telechargement = QtWidgets.QLineEdit()
        self.le_telechargement.setFrame(False)
        self.le_telechargement.setPlaceholderText("Entrer le lien exemple:www.youtube.com")
        self.le_telechargement.clearFocus()
        self.le_titre = QtWidgets.QLineEdit()
        self.le_titre.setFrame(False)
        self.le_titre.setPlaceholderText("Titre de la video")




        self.btn_verification = QtWidgets.QPushButton("Recherches")

        self.chk_haute_resolution = QtWidgets.QCheckBox("Haute resolution")
        self.chk_basse_resolution = QtWidgets.QCheckBox("Basse resolution")
        self.chk_audio = QtWidgets.QCheckBox("Audio")

        self.btn_telecharger = QtWidgets.QPushButton("Telecharger")
        self.btn_quitter = QtWidgets.QPushButton("Quitter")
        self.btn_quitter.setFlat(True)
        self.btn_telecharger.setFlat(True)
        self.btn_telecharger.setStyleSheet("QPushButton:hover {color:#8B1874};}")
        self.btn_quitter.setStyleSheet("QPushButton:hover {color:#8B1874;}")

        self.layout_principale.addWidget(self.label)
        self.layout_principale.addWidget(self.le_telechargement)
        self.layout_principale.addLayout(self.layout_horizontal_titre)
        self.layout_horizontal_titre.addWidget(self.le_titre)

        self.layout_principale.addWidget(self.btn_verification)

        self.layout_horizontal.addWidget(self.chk_haute_resolution)
        self.layout_horizontal.addWidget(self.chk_basse_resolution)
        self.layout_horizontal.addWidget(self.chk_audio)

        self.layout_principale.addLayout(self.layout_horizontal)

        self.h_layout.addWidget(self.btn_telecharger)
        self.h_layout.addWidget(self.btn_quitter)

        self.layout_principale.addLayout(self.h_layout)