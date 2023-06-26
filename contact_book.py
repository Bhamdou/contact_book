import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add(self, name, phone, email):
        for contact in self.contacts:
            if contact.name == name:
                return False
        self.contacts.append(Contact(name, phone, email))
        return True

    def delete(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def update(self, name, phone, email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = phone
                contact.email = email
                return True
        return False

    def search(self, name):
        return [contact for contact in self.contacts if name.lower() in contact.name.lower()]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)

        self.addContactButton = QtWidgets.QPushButton(self.centralwidget)
        self.addContactButton.setObjectName("addContactButton")
        self.gridLayout.addWidget(self.addContactButton, 2, 0, 1, 1)

        self.deleteContactButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteContactButton.setObjectName("deleteContactButton")
        self.gridLayout.addWidget(self.deleteContactButton, 2, 1, 1, 1)

        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.gridLayout.addWidget(self.emailLineEdit, 1, 3, 1, 1)

        self.phoneLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.gridLayout.addWidget(self.phoneLineEdit, 0, 3, 1, 1)

        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.phoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.phoneLabel.setObjectName("phoneLabel")
        self.gridLayout.addWidget(self.phoneLabel, 0, 2, 1, 1)

        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setObjectName("emailLabel")
        self.gridLayout.addWidget(self.emailLabel, 1, 2, 1, 1)

        self.updateContactButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateContactButton.setObjectName("updateContactButton")
        self.gridLayout.addWidget(self.updateContactButton, 2, 2, 1, 1)

        self.contactsTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.contactsTableWidget.setObjectName("contactsTableWidget")
        self.contactsTableWidget.setColumnCount(3)
        self.contactsTableWidget.setHorizontalHeaderLabels(['Name', 'Phone', 'Email'])
        self.gridLayout.addWidget(self.contactsTableWidget, 3, 0, 1, 4)

        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 2, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Initialize the contact book and update the table view
        self.book = ContactBook()
        self.updateTable()

        # Connect buttons to their respective methods
        self.addContactButton.clicked.connect(self.addContact)
        self.deleteContactButton.clicked.connect(self.deleteContact)
        self.updateContactButton.clicked.connect(self.updateContact)
        self.searchButton.clicked.connect(self.searchContact)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addContactButton.setText(_translate("MainWindow", "Add Contact"))
        self.deleteContactButton.setText(_translate("MainWindow", "Delete Contact"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.phoneLabel.setText(_translate("MainWindow", "Phone"))
        self.emailLabel.setText(_translate("MainWindow", "Email"))
        self.updateContactButton.setText(_translate("MainWindow", "Update Contact"))
        self.searchButton.setText(_translate("MainWindow", "Search"))

    def updateTable(self):
        self.contactsTableWidget.setRowCount(len(self.book.contacts))
        for i, contact in enumerate(self.book.contacts):
            self.contactsTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(contact.name))
            self.contactsTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(contact.phone))
            self.contactsTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(contact.email))

    def addContact(self):
        if self.book.add(self.nameLineEdit.text(), self.phoneLineEdit.text(), self.emailLineEdit.text()):
            self.updateTable()

    def deleteContact(self):
        if self.book.delete(self.nameLineEdit.text()):
            self.updateTable()

    def updateContact(self):
        if self.book.update(self.nameLineEdit.text(), self.phoneLineEdit.text(), self.emailLineEdit.text()):
            self.updateTable()

    def searchContact(self):
        search_results = self.book.search(self.nameLineEdit.text())
        self.contactsTableWidget.setRowCount(len(search_results))
        for i, contact in enumerate(search_results):
            self.contactsTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(contact.name))
            self.contactsTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(contact.phone))
            self.contactsTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(contact.email))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
