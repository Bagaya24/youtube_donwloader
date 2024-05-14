from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QFileDialog

from Ui.Fenetre import Fenetre
from pytube import YouTube


from functools import partial


class FenetrePrincaple(QtWidgets.QWidget, Fenetre):
    def __init__(self):
        super(FenetrePrincaple, self).__init__()
        self.setup_ui(self)

        self.setup_connection()

    def setup_connection(self):
        self.btn_quitter.clicked.connect(self.close)
        self.btn_telecharger.clicked.connect(self.setup_telecharger)
        self.btn_verification.clicked.connect(self.setup_recherche)
        QtWidgets.QShortcut(QtGui.QKeySequence("Esc"), self, self.close)
        #QtWidgets.QShortcut(QtGui.QKeySequence(""), self, self.setup_recherche)

    def setup_recherche(self):
        if self.le_telechargement.text() == "":
            avertissement = QtWidgets.QMessageBox(self)
            avertissement.warning(self, "Erreur", "Veuillez saisir un lien a telechargement")
        else:
            url = self.le_telechargement.text()
            self.video_a_telecharger = YouTube(url, use_oauth=True, allow_oauth_cache=True)
            self.le_titre.setText(self.video_a_telecharger.title)

    def setup_telecharger(self):
        try:
            if self.le_telechargement.text() == "":
                avertissement = QtWidgets.QMessageBox(self)
                avertissement.warning(self, "Erreur", "Veuillez chercher la video d'abord")
            else:
                chemin_du_telechargement = QFileDialog.getExistingDirectory(self, 'Select Folder', '.')
                if self.chk_haute_resolution.checkState():
                    self.video_a_telecharger = self.video_a_telecharger.streams.get_highest_resolution()
                    self.video_a_telecharger.download(chemin_du_telechargement)
                    self.reset()
                elif self.chk_basse_resolution.checkState():
                    self.video_a_telecharger = self.video_a_telecharger.streams.get_lowest_resolution()
                    self.video_a_telecharger.download(chemin_du_telechargement)
                    self.reset()
                elif self.chk_audio.checkState():
                    self.video_a_telecharger = self.video_a_telecharger.streams.get_audio_only()
                    self.video_a_telecharger.download(chemin_du_telechargement)
                    self.reset()
                else:
                    critical = QtWidgets.QMessageBox(self)
                    critical.critical(self, "Erreur", "Veillez cocher une case")

        except Exception as es:
            critical = QtWidgets.QMessageBox(self)
            critical.critical(self, "Erreur", f"{es} \n veillez reessayer ou changer de lien")
            self.le_titre.clear()
            self.le_telechargement.clear()

    def reset(self):
        QtWidgets.QMessageBox.information(self, "Reussi", f"Le telechargement de "
                                                          f"{self.le_titre.text()} est termine")
        self.le_titre.clear()
        self.le_telechargement.clear()


app = QtWidgets.QApplication([])

fenetre = FenetrePrincaple()
fenetre.show()

app.exec_()