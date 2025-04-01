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
        self.points_checkbox.clicked.connect(self.togglepoints)
        self.type_checkbox.clicked.connect(self.toggletypes)
        self.get_button.clicked.connect(self.get)
        self.pokegen_button.clicked.connect(self.random_pkm_amount)
        self.itemgen_button.clicked.connect(self.random_item_amount)
        self.roll_button.clicked.connect(self.roll)
        self.save_button.clicked.connect(self.save)
        self.IP = '127.0.0.1'
        self.types = []
        self.types_enabled = False
        self.ver = 'BW'
        self.level = 1

        self.gamesyncid_label_style = self.gamesyncid_label.styleSheet()
        self.get_button_style = self.get_button.styleSheet()
        self.points_label_style = self.points_label.styleSheet()
        self.points_checkbox_style = self.points_checkbox.styleSheet()
        self.points_spinbox_style = self.points_spinbox.styleSheet()

    def togglepoints(self):
        self.points_label.setEnabled(not self.points_label.isEnabled())
        self.points_spinbox.setEnabled(not self.points_spinbox.isEnabled())

    def toggletypes(self):
        self.types_enabled = not self.types_enabled
        self.types_label.setEnabled(self.types_enabled)

    def get(self):
        self.gamesyncid_label.setStyleSheet(self.gamesyncid_label_style)
        s = requests.Session()
        login_request = s.post(f'http://{self.IP}/dashboard/login', data={
            'gsid': self.gamesyncid_lineedit.text()})
        if 'error' in login_request.json() and login_request.json()['error']:
            self.gamesyncid_label.setStyleSheet('QLabel {color: red;}')
            return
        request = s.get(f'http://{self.IP}/dashboard/profile').json()
        s.close()
        if 'dreamerInfo' in request:
            self.types = pokedata.types[request['dreamerInfo']['species']]
            self.types_label.setText(', '.join(self.types if self.types[1] != '' else [self.types[0]]))
            self.level = request['dreamerInfo']['level']
        if 'gameVersion' in request:
            self.game_comboBox.setCurrentIndex(1 if "2" in request['gameVersion'] else 0)
            self.ver = 'B2W2' if "2" in request['gameVersion'] else 'BW'

    def random_pkm_amount(self):
        self.pokegen_spinbox.setValue(random.randint(1, 10))

    def random_item_amount(self):
        self.itemgen_spinbox.setValue(random.randint(1, 12))

    def roll(self):
        self.get_button.setStyleSheet(self.get_button_style)
        self.points_label.setStyleSheet(self.points_label_style)
        self.points_checkbox.setStyleSheet(self.points_checkbox_style)
        self.points_spinbox.setStyleSheet(self.points_spinbox_style)
        if not self.types:
            self.get_button.setStyleSheet('QPushButton {color: red;}')
            return
        self.roll_button.setText('Reroll')
        self.save_button.setEnabled(True)
        self.output_label.clear()

        areas = [self.areas_layout.itemAt(a).widget().text() for a in range(8)
                 if self.areas_layout.itemAt(a).widget().isChecked()]
        if not areas:
            areas = list(locations.locations.keys())
        if self.points_checkbox.isChecked():
            areas = [i for i in areas if locations.locations[i]['points'][self.ver] == 'Default' or
                     self.points_spinbox.value() >= locations.locations[i]['points'][self.ver]]
        if not areas:
            self.points_label.setStyleSheet('QLabel {color: red;}')
            self.points_checkbox.setStyleSheet('QCheckBox {color: red;}')
            self.points_spinbox.setStyleSheet('QSpinBox {color: red;}')
            return
        areas_weight = [
            1 + self.level / 100 if self.types_enabled and (self.types[0] in locations.locations[i]['types'] or
                                                            self.types[1] in locations.locations[i]['types'])
            else 1 for i in areas]
        random_location = random.choices(areas, weights=areas_weight)[0]
        possible_pokemon = locations.locations[random_location]['pkms']
        possible_items = locations.locations[random_location]['items']

        pokemon_count = self.pokegen_spinbox.value()
        item_count = self.itemgen_spinbox.value()

        self.encounters = []
        for i in range(pokemon_count):
            random_pokemon = random.choice(possible_pokemon)
            while not ((random_pokemon['ver'] == self.ver or random_pokemon['ver'] == 'none') and
                       ((random_pokemon['points'] == 'Default'
                         or self.points_spinbox.value() >= random_pokemon['points'])
                       if self.points_checkbox.isChecked() else True)):
                random_pokemon = random.choice(possible_pokemon)
            pokemon_dictionary = pokedata.pkms[random_pokemon['name']]
            pokemon_id = pokemon_dictionary['id']
            pokemon_move = random.choice(random_pokemon['move'])
            name = random_pokemon['name']
            pokemon_move_id = pokedata.moves[pokemon_move]
            form = random_pokemon['form'] if 'form' in random_pokemon else 0
            animation = random.choice(["SPIN_RIGHT", "SPIN_LEFT"]) if name in ['Metapod', 'Kakuna', 'Pineco',
                                                                                     'Silcoon', 'Cascoon', 'Spinda',
                                                                                     'Burmy', 'Ferroseed'] else \
                random.choice(["LOOK_AROUND", "WALK_AROUND", "WALK_LOOK_AROUND", "WALK_VERTICALLY",
                               "WALK_HORIZONTALLY", "WALK_LOOK_HORIZONTALLY", "SPIN_RIGHT", "SPIN_LEFT"])
            self.encounters.append(
                {'species': pokemon_id, 'move': pokemon_move_id, 'form': form,
                 'gender': pokemon_dictionary['gender'],
                 'animation': animation})
            self.output_label.setText(f'{self.output_label.text()}{random_pokemon["name"]}: {pokemon_move}, ')
        if self.encounters:
            self.output_label.setText(f'{self.output_label.text()[:-2]}\n\n')

        self.items = []
        for i in range(item_count):
            item = random.choice(possible_items)
            item_id = pokedata.items[item['item']]
            item_dict = {'id': item_id, 'quantity': 1}
            if item_dict in self.items:
                self.items[self.items.index(item_dict)]['quantity'] += 1
            else:
                self.items.append(item_dict)
            self.output_label.setText(f'{self.output_label.text()}{item["item"]}, ')
        if self.items:
            self.output_label.setText(self.output_label.text()[:-2])

    def save(self):
        g = requests.Session()
        g.post(f'http://{self.IP}/dashboard/login', data={
            'gsid': self.gamesyncid_lineedit.text()})
        g.post(f'http://{self.IP}/dashboard/profile', data=json.dumps({'encounters': self.encounters,
                                                                       'items': self.items,
                                                                       'avenueVisitors': [],
                                                                       'cgearSkin': 'none',
                                                                       'dexSkin': 'none',
                                                                       'musical': 'none',
                                                                       'gainedLevels': 0}))
        g.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MenuW()
    ex.show()
    sys.exit(app.exec_())
