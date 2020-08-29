"""
https://stackoverflow.com/questions/21269692/pyqt-link-list-view-and-table-view-with-model-using-python-dictionary

# pyqt link list view and table view with model using python dictionary [closed]
"""

import sys

from PySide2 import QtCore, QtWidgets

from src import sonet_spacecraft

new_spacecraft = sonet_spacecraft.SonetSpacecraft
#mock_data = {'Spacecraft 1': new_spacecraft('mock1.txt'), 'Spacecraft 2': new_spacecraft('mock2.txt')}

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(TableModel, self).__init__(parent)
        self._data = data
        # defualt key
        self.dict_key = 'key0'

    def set_key(self, key):
        self.beginResetModel()
        self.dict_key = key
        self.endResetModel()

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self._data[self.dict_key])

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self._data[self.dict_key][0])

    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()
        column = QModelIndex.column()
        if int_role == QtCore.Qt.DisplayRole:
            return str(self._data[self.dict_key][row][column])

class ListModel(QtCore.QAbstractListModel):
    def __init__(self, data, parent=None):
        super(ListModel, self).__init__(parent)
        self._data = data.keys()

    def list_clicked(self, index):
        row = index.row()
        key = self._data[row]
        table_model.set_key(key)

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self._data)

    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()
        if int_role == QtCore.Qt.DisplayRole:
            return str(self._data[row])

    def flags(self, QModelIndex):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


#########################################
# temporary just to get above code to run
app = QtWidgets.QApplication(sys.argv)

list_view = QtWidgets.QListView()
list_model = ListModel(mock_data)
list_view.setModel(list_model)
list_view.clicked.connect(list_model.list_clicked)
list_view.show()

table_view = QtWidgets.QTableView()
table_model = TableModel(mock_data)
table_view.setModel(table_model)
table_view.show()

sys.exit(app.exec_())