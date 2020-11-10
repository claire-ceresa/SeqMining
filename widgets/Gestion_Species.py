from PyQt5.QtWidgets import QWidget, QListWidgetItem
from functions.graphics_function import *


class Gestion_Species(QWidget):

    def __init__(self, parent=None, connexion=None, widget=None):
        super(Gestion_Species, self).__init__(parent)
        self.current = None
        self.connexion = connexion
        self.widget = widget

    # METHODS OF THE BUTTONS

    def list_species_clicked(self, line):
        all_species = self.connexion.get_all_species()
        if line < len(all_species):
            self.current = all_species[line]
            self.fill_in()
        else:
            self.current = None
            self.clear()

    def button_save_clicked(self):
        if len(self.widget.s_edit_name.text()) == 0:
            create_messageBox("Attention !", "Nom d'espece obligatoire !")
        else:
            if self.current is not None:
                action = self.save_modified_species()
            else:
                action = self.save_new_species()
            if action['sent']:
                create_messageBox("Enregistré !", "Modifications enregistrées !")
                self.init()
                self.list_species_clicked(self.widget.s_list_species.currentRow())
            else:
                create_messageBox("Erreur !",
                                  "Une erreur est survenue.\n" + str(action['error']))

    def button_delete_clicked(self):
        message = QtWidgets.QMessageBox.question(self, "Supprimer", "Etes vous sur ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No )
        if message == QtWidgets.QMessageBox.Yes:
            query = self.connexion.create_query_delete("species", {'name': '"' + self.current['name'] + '"'})
            query_to_send = [{'query': query}]
            self.connexion.run_on_php(query_to_send)
            self.init()

    def button_add_species_clicked(self):
        item = QListWidgetItem("")
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        item.setSelected(True)
        self.widget.s_list_species.addItem(item)
        self.widget.s_list_species.setCurrentItem(item)

    # GRAPHIC METHODS

    def init(self):
        self.connexion.load_datas()
        self.widget.s_list_species.clear()
        all_species = self.connexion.get_all_species()
        for species in all_species:
            self.widget.s_list_species.addItem(species['name'])
        self.current = all_species[0]
        self.widget.s_list_species.setCurrentRow(0)

    def fill_in(self):
        self.widget.s_edit_name.setText(self.current['name'])
        self.widget.s_edit_by.setText(self.current['discovered_by'])
        self.widget.s_edit_in.setText(self.current['discovered_in'])
        self.widget.s_edit_famille.setText(self.current['family'])
        self.widget.s_edit_ordre.setText(self.current['ordo'])
        self.widget.s_edit_classe.setText(self.current['classe'])
        self.widget.s_edit_emb.setText(self.current['phylum'])
        self.widget.s_edit_regne.setText(self.current['kingdom'])
        self.widget.s_edit_morpho.setText(self.current['morpho'])
        self.widget.s_edit_caract.setText(self.current['caracteristics'])
        self.widget.s_edit_behav.setText(self.current['behavior'])
        self.widget.s_edit_ecosocio.setText(self.current['eco_socio'])
        self.widget.s_edit_ecology.setText(self.current['ecology'])
        self.widget.s_edit_threat.setText(self.current['threats'])

        if self.current['symbiosis'] == 'oui':
            self.widget.s_checkbox_symbiose.setChecked(True)
            set_label_bold(self.widget.s_checkbox_symbiose, True)
        else:
            self.widget.s_checkbox_symbiose.setChecked(False)
            set_label_bold(self.widget.s_checkbox_symbiose, False)

        if self.current['UICN_short'] is not None:
            self.widget.s_groupbox_uicn.setChecked(True)
            self.widget.s_edit_uicn_short.setText(self.current['UICN_short'])
            self.widget.s_edit_uicn_fr.setText(self.current['UICN_fr'])
            self.widget.s_edit_uicn_long.setText(self.current['UICN_long'])
        else:
            self.widget.s_groupbox_uicn.setChecked(False)
            self.widget.s_edit_uicn_short.clear()
            self.widget.s_edit_uicn_fr.clear()
            self.widget.s_edit_uicn_long.clear()

        if self.current['synonym'] is not None:
            self.widget.s_checkbox_synonym.setChecked(True)
            self.widget.s_edit_synonym.setText(self.current['synonym'])
        else:
            self.widget.s_checkbox_synonym.setChecked(False)
            self.widget.s_edit_synonym.clear()

        if self.current['CITES'] is not None:
            self.widget.s_checkbox_cites.setChecked(True)
            self.widget.s_edit_cites.setText(self.current['CITES'])
        else:
            self.widget.s_checkbox_cites.setChecked(False)
            self.widget.s_edit_cites.clear()

    def clear(self):
        self.widget.s_edit_name.clear()
        self.widget.s_edit_by.clear()
        self.widget.s_edit_in.clear()
        self.widget.s_edit_famille.clear()
        self.widget.s_edit_ordre.clear()
        self.widget.s_edit_classe.clear()
        self.widget.s_edit_emb.clear()
        self.widget.s_edit_regne.clear()
        self.widget.s_edit_morpho.clear()
        self.widget.s_edit_caract.clear()
        self.widget.s_edit_behav.clear()
        self.widget.s_edit_ecosocio.clear()
        self.widget.s_edit_ecology.clear()
        self.widget.s_edit_threat.clear()
        self.widget.s_checkbox_symbiose.setChecked(False)
        set_label_bold(self.widget.s_checkbox_symbiose, False)
        self.widget.s_groupbox_uicn.setChecked(False)
        self.widget.s_edit_uicn_short.clear()
        self.widget.s_edit_uicn_fr.clear()
        self.widget.s_edit_uicn_long.clear()
        self.widget.s_checkbox_synonym.setChecked(False)
        self.widget.s_edit_synonym.clear()
        self.widget.s_checkbox_cites.setChecked(False)
        self.widget.s_edit_cites.clear()

    # GETTERS

    def get_new_species(self):
        new_species = {
            'name': self.widget.s_edit_name.text(),
            'synonym': self.widget.s_edit_synonym.text(),
            'family': self.widget.s_edit_famille.text(),
            'ordo': self.widget.s_edit_ordre.text(),
            'classe': self.widget.s_edit_classe.text(),
            'phylum': self.widget.s_edit_emb.text(),
            'kingdom': self.widget.s_edit_regne.text(),
            'discovered_by': self.widget.s_edit_by.text(),
            'discovered_in': self.widget.s_edit_in.text(),
            'symbiosis': None,
            'UICN_short': self.widget.s_edit_uicn_short.text(),
            'UICN_long': self.widget.s_edit_uicn_long.text(),
            'UICN_fr': self.widget.s_edit_uicn_fr.text(),
            'threats': self.widget.s_edit_threat.toPlainText(),
            'CITES': self.widget.s_edit_cites.text(),
            'morpho': self.widget.s_edit_morpho.toPlainText(),
            'caracteristics': self.widget.s_edit_caract.toPlainText(),
            'behavior': self.widget.s_edit_behav.toPlainText(),
            'ecology': self.widget.s_edit_ecology.toPlainText(),
            'eco_socio': self.widget.s_edit_ecosocio.toPlainText()
        }

        if self.widget.s_checkbox_symbiose.checkState() == 2:
            new_species['symbiosis'] = 'oui'
        else:
            new_species['symbiosis'] = 'non'

        return new_species

    def get_new_values(self, new_species):
        saved = {}
        for key, value in new_species.items():
            if value == '':
                continue
            else:
                saved[key] = '"' + str(value) + '"'
        return saved

    def get_modified_values(self, new_species):
        modified = {}
        for key, value in new_species.items():
            if value == '':
                value = None
            if self.current[key] != value:
                if value is None:
                    modified[key] = 'NULL'
                else:
                    modified[key] = '"' + str(value) + '"'
        return modified

    # SAVING METHODS

    def save_new_species(self):
        query_to_send = []
        new_species = self.get_new_species()
        self.current = new_species
        values_to_save = self.get_new_values(new_species)
        query = self.connexion.create_query_insert(table="species", values=values_to_save)
        if query is not None:
            query_to_send.append({'query':query})
        run = self.connexion.run_on_php(query_to_send)
        return run

    def save_modified_species(self):
        query_to_send = []
        new_species = self.get_new_species()
        values_to_save = self.get_modified_values(new_species)
        query = self.connexion.create_query_update(table="species", values=values_to_save,
                                                   where={'name':  '"' + self.current['name'] + '"'})
        if query is not None:
            query_to_send.append({'query': query})
        run = self.connexion.run_on_php(query_to_send)
        return run