import sys

import requests
import json
import random

from PyQt5.QtWidgets import QMainWindow, QApplication

import locations
import pokedata
import menu


class MenuW(QMainWindow, menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.checkBox_2.clicked.connect(self.togglepoints)
        self.checkBox_2.setEnabled(False)
        self.pushButton_3.clicked.connect(self.random_pkm_amount)
        self.pushButton_2.clicked.connect(self.roll)
        self.pushButton.clicked.connect(self.save)

        self.spinBox_2.setEnabled(False)

    def togglepoints(self):
        self.label_6.setEnabled(not self.label_6.isEnabled())
        self.spinBox_3.setEnabled(not self.spinBox_3.isEnabled())

    def random_pkm_amount(self):
        self.spinBox.setValue(random.randint(1, 10))

    def roll(self):
        self.locationsstr = []
        self.pushButton_2.setText('Reroll')
        self.pushButton.setEnabled(True)
        self.label_9.clear()
        for area in range(8):
            if self.verticalLayout_2.itemAt(area).widget().isChecked():
                self.locationsstr.append(self.verticalLayout_2.itemAt(area).widget().text())
        self.pkmsavailable = []
        if self.locationsstr:
            for loc in self.locationsstr:
                self.pkmsavailable += locations.locations[loc]
        else:
            self.pkmsavailable += locations.locations[random.choice(['Pleasant Forest', 'Windswept Sky',
                                                                     'Sparkling Sea', 'Spooky Manor', 'Rugged Mountain',
                                                                     'Icy Cave', 'Dream Park', 'Cafe Forest'])]
        self.pkm_count = self.spinBox.value()

        self.encounters = []
        self.ver = 'BW' if self.comboBox.currentText() == 'Black/White' else 'B2W2'
        for i in range(self.pkm_count):
            pkm = random.choice(self.pkmsavailable)
            if pkm['ver'] != 'none':
                while pkm['ver'] != self.ver:
                    pkm = random.choice(self.pkmsavailable)
            pkm_d = pokedata.pkms[pkm['name']]
            pkm_id = pkm_d['id']
            move = random.choice(pkm['move'])
            move_id = pokedata.moves[move]
            form = random.choice(pkm_d['forms']) if pkm['name'] \
                                                    not in ['Deoxys', 'Rotom', 'Giratina', 'Shaymin', 'Arceus',
                                                            'Tornadus', 'Thundurus', 'Landorus', 'Kyurem', 'Keldeo',
                                                            'Meloetta', 'Genesect'] else 0
            animation = random.choice(["SPIN_RIGHT", "SPIN_LEFT"]) if pkm_id in [597, 11, 14, 327] else \
                random.choice(["LOOK_AROUND", "WALK_AROUND", "WALK_LOOK_AROUND", "WALK_VERTICALLY",
                               "WALK_HORIZONTALLY", "WALK_LOOK_HORIZONTALLY", "SPIN_RIGHT", "SPIN_LEFT"])
            self.encounters.append(
                {'species': pkm_id, 'move': move_id, 'form': form, 'gender': pkm_d['gender'], 'animation': animation})
            self.label_9.setText(f'{self.label_9.text()}{pkm["name"]}: {move}, ')

    def save(self):
        g = requests.Session()
        print(g.post('http://127.0.0.1/dashboard/login', data={
            'gsid': self.lineEdit.text()}))
        print(g.post('http://127.0.0.1/dashboard/profile', data=json.dumps({'encounters': self.encounters,
                                                                            'items': [],
                                                                            'avenueVisitors': [],
                                                                            'cgearSkin': 'none',
                                                                            'dexSkin': 'none',
                                                                            'musical': 'none',
                                                                            'gainedLevels': 0})))
        g.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MenuW()
    ex.show()
    sys.exit(app.exec_())
