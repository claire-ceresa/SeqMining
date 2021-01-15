import string
import random
import bcrypt as b
#from passlib.hash import bcrypt
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from functions.graphics_function import *


class Gestion_Users(QWidget):

    def __init__(self, parent=None, connexion=None, widget=None):
        super(Gestion_Users, self).__init__(parent)
        self.current = None
        self.connexion = connexion
        self.widget = widget

    # CLASS METHODS

    def list_users_clicked(self, line):
        all_users = self.connexion.get_all_users()
        print(all_users)
        if line < len(all_users):
            self.current = all_users[line]
            self.fill_in()
        else:
            self.current = None
            self.clear()

    def button_add_clicked(self):
        item = QListWidgetItem("")
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        item.setSelected(True)
        self.widget.u_list_users.addItem(item)
        self.widget.u_list_users.setCurrentItem(item)

    def button_save_clicked(self):
        if len(self.widget.u_edit_username.text()) == 0:
            create_messageBox("Attention !", "Nom d'utilisateur obligatoire !")
        else:
            if self.current is not None:
                action = self.save_modified_user()
            else:
                action = self.save_new_user()

    def button_delete_clicked(self):
        message = QtWidgets.QMessageBox.question(self, "Supprimer ?", "Etes vous sur ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if message == QtWidgets.QMessageBox.Yes:
            query = self.connexion.create_query_delete("users", {"username": '"' + self.current['username'] + '"'})
            query_to_send = [{'query': query}]
            self.connexion.run_on_php(query_to_send)
            self.init()

    def button_pwd_clicked(self):
        pwd = self.create_pwd()
        self.widget.u_edit_pwd.setText(pwd)
        self.widget.u_edit_crypt.clear()
        self.widget.u_button_crypt.setEnabled(True)
        self.widget.u_button_pwd_save.setEnabled(False)
        self.widget.u_button_verif.setEnabled(False)

    def button_crypt_clicked(self):
        pwd = self.widget.u_edit_crypt.text()
        hash = self.hash_pwd(pwd)
        self.widget.u_edit_crypt.setText(hash)
        if self.current is not None:
            self.widget.u_button_pwd_save.setEnabled(True)
            self.widget.u_button_verif.setEnabled(True)

    def button_pwd_save_clicked(self):
        query = self.connexion.create_query_update(table='users', values={'pwd_new': '"' + self.widget.u_edit_crypt.text() + '"'},
                                               where= {'username': '"' + self.current['username'] + '"'})
        query_to_send = [{'query': query}]
        action = self.connexion.run_on_php(query_to_send)
        if action["sent"]:
            create_messageBox("Succes !", "Mot de passe modifié !")
        else:
            create_messageBox("Erreur !",
                          "Une erreur est survenue.\n" + str(action['error']))


    def button_verif_clicked(self):
        proposed_pwd = bytes(self.widget.u_edit_pwd.text(), encoding='utf-8')
        saved_pwd = bytes(self.current['pwd_new'], encoding='utf-8')
        if b.checkpw(proposed_pwd, saved_pwd):

        # proposed_pwd = self.widget.u_edit_pwd.text()
        # saved_pwd = self.current['pwd_new']
        # if bcrypt.verify(proposed_pwd, saved_pwd):

            create_messageBox('Succes', 'Le mot de passe est correct')
        else:
            create_messageBox('Erreur', 'Le mot de passe est incorrect !')

    # GRAPHIC METHODS

    def init(self):
        self.connexion.load_datas()
        self.widget.u_list_users.clear()
        all_users = self.connexion.get_all_users()
        for user in all_users:
            self.widget.u_list_users.addItem(user['username'])
        self.current = all_users[0]
        self.widget.u_list_users.setCurrentRow(0)
        self.widget.u_checkbox_activated.setTristate(False)

    def fill_in(self):
        self.widget.u_edit_username.setText(self.current['username'])
        self.widget.u_edit_firstname.setText(self.current['firstname'])
        self.widget.u_edit_surname.setText(self.current['surname'])
        self.widget.u_edit_society.setText(self.current['society'])
        self.widget.u_edit_email.setText(self.current['email'])
        self.widget.u_edit_phone.setText(self.current['phone'])
        self.widget.u_edit_address.setText(self.current['address'])
        self.widget.u_label_nb_count.setText(self.current['count'])

        if self.current['activated'] == '1':
            self.widget.u_checkbox_activated.setChecked(True)
            set_label_bold(self.widget.u_checkbox_activated, True)
        else:
            self.widget.u_checkbox_activated.setChecked(False)
            set_label_bold(self.widget.u_checkbox_activated, False)

        if self.current['CGU_accepted'] is not None:
            self.widget.u_checkbox_cgu.setChecked(True)
            self.widget.u_checkbox_cgu.setEnabled(False)
            self.widget.u_label_cgu.setText('CGU acceptés le ' + str(self.current['CGU_accepted']))
            set_label_bold(self.widget.u_label_cgu, True)
        else:
            self.widget.u_checkbox_cgu.setChecked(False)
            self.widget.u_label_cgu.setText('CGU acceptés ')
            set_label_bold(self.widget.u_label_cgu, False)

        if self.current['pwd_new'] is not None:
            self.widget.u_checkbox_first_pwd.setChecked(True)
            self.widget.u_checkbox_first_pwd.setEnabled(False)
            set_label_bold(self.widget.u_label_first_pwd, True)
        else:
            self.widget.u_checkbox_first_pwd.setChecked(False)
            set_label_bold(self.widget.u_label_first_pwd, False)

    def clear(self):
        self.widget.u_edit_username.clear()
        self.widget.u_edit_firstname.clear()
        self.widget.u_edit_surname.clear()
        self.widget.u_edit_society.clear()
        self.widget.u_edit_email.clear()
        self.widget.u_edit_phone.clear()
        self.widget.u_edit_address.clear()
        self.widget.u_label_nb_count.setText('0')
        self.widget.u_checkbox_activated.setChecked(False)
        set_label_bold(self.widget.u_checkbox_activated, False)
        self.widget.u_checkbox_cgu.setChecked(False)
        self.widget.u_label_cgu.setText('CGU acceptés')
        set_label_bold(self.widget.u_label_cgu, False)
        self.widget.u_checkbox_first_pwd.setChecked(False)
        set_label_bold(self.widget.u_label_first_pwd, False)
        self.widget.u_edit_pwd.clear()
        self.widget.u_edit_crypt.clear()

    # OTHER METHODS

    def create_pwd(self):
        possibles_list = []
        possibles_list.append(string.ascii_letters)
        possibles_list.append(string.digits)
        possibles = "".join(possibles_list)
        character_list = [random.choice(possibles) for i in range(10)]
        pwd = "".join(character_list)
        return pwd

    def hash_pwd(self, pwd):
        salt = b.gensalt()
        hashed = b.hashpw(bytes(pwd, encoding='utf-8'), salt)
        #hashed = bcrypt.using(ident="2y").hash(pwd)
        return hashed


    def save_new_user(self):
        print("new")

    def save_modified_user(self):
        print("modified")