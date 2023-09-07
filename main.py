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
        self.checkBox_2.clicked.connect(self.togglepoints)
        self.pushButton_3.clicked.connect(self.random_pkm_amount)
        self.pushButton_4.clicked.connect(self.random_item_amount)
        self.pushButton_2.clicked.connect(self.roll)
        self.pushButton.clicked.connect(self.save)

    def togglepoints(self):
        self.label_6.setEnabled(not self.label_6.isEnabled())
        self.spinBox_3.setEnabled(not self.spinBox_3.isEnabled())

    def random_pkm_amount(self):
        self.spinBox.setValue(random.randint(1, 10))

    def random_item_amount(self):
        self.spinBox_2.setValue(random.randint(1, 12))

    def roll(self):
        self.locationsstr = []
        self.pushButton_2.setText('Reroll')
        self.pushButton.setEnabled(True)
        self.label_9.clear()
        for area in range(8):
            if self.verticalLayout_2.itemAt(area).widget().isChecked():
                self.locationsstr.append(self.verticalLayout_2.itemAt(area).widget().text())
        self.pkmsavailable = []
        self.itemsavailable = []
        if self.locationsstr:
            for loc in self.locationsstr:
                self.pkmsavailable += locations.locations[loc]['pkms']
                self.itemsavailable += locations.locations[loc]['items']
        else:
            randloc = random.choice(['Pleasant Forest', 'Windswept Sky',
                                     'Sparkling Sea', 'Spooky Manor', 'Rugged Mountain',
                                     'Icy Cave', 'Dream Park', 'Cafe Forest'])
            self.pkmsavailable += locations.locations[randloc]['pkms']
            self.itemsavailable += locations.locations[randloc]['items']
        self.pkm_count = self.spinBox.value()
        self.item_count = self.spinBox_2.value()

        self.encounters = []
        self.ver = 'BW' if self.comboBox.currentText() == 'Black/White' else 'B2W2'
        for i in range(self.pkm_count):
            pkm = random.choice(self.pkmsavailable)
            while (pkm['ver'] != self.ver and pkm['ver'] != 'none') or \
                    (('Default' != pkm['points'] and self.spinBox_3.value() < pkm['points'])
                     if self.spinBox_3.isEnabled() else False):
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
        if self.encounters:
            self.label_9.setText(f'{self.label_9.text()[:-2]}\n\n')

        self.items = []
        for i in range(self.item_count):
            item = random.choice(self.itemsavailable)
            item_id = pokedata.items[item['item']]
            item_dict = {'id': item_id, 'quantity': 1}
            if item_dict in self.items:
                self.items[self.items.index(item_dict)]['quantity'] += 1
            else:
                self.items.append(item_dict)
            self.label_9.setText(f'{self.label_9.text()}{item["item"]}, ')
        if self.items:
            self.label_9.setText(self.label_9.text()[:-2])

    def save(self):
        g = requests.Session()
        print(g.post('http://127.0.0.1/dashboard/login', data={
            'gsid': self.lineEdit.text()}))
        print(g.post('http://127.0.0.1/dashboard/profile', data=json.dumps({'encounters': self.encounters,
                                                                            'items': self.items,
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
