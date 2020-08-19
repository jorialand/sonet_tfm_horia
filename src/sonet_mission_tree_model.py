from PySide2.QtCore import QAbstractListModel, QAbstractItemModel, Qt


class SonetMissionTreeModel(QAbstractListModel):
    """
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :: sonet_mission_tree_model
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    :: Class accommodating the mission tree model logic/functionality.
    :: It contains the data and the model of the mission tree QListView widget displaying the spacecrafts, missions,
    :: etc. artifacts.

    :: Friday 7th Aug 2020
    :: Horia Ghionoiu Martínez
    """

    def __init__(self, parent=None):
        super(SonetMissionTreeModel, self).__init__(parent)
        self._sonet_objects_db = {}  #{'key1': 'value1', 'key2': 'value1'}  # All the spacecrafts, missions, etc. artifacts, are stored here.
        self._data = list(self._sonet_objects_db.keys())

    def list_clicked(self, index):
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        """
        Mandatory function to be implemented.
        :param QModelIndex_parent:
        :param args:
        :param kwargs:
        :return:
        """
        return len(self._data)

    def data(self,  index, role=Qt.DisplayRole):
        """
        Mandatory function to be implemented.
        :param index:
        :param role:
        :return:
        """

        if not index.isValid():
            return None
        row = index.row()

        if row >= self.rowCount():
            return None

        if role == Qt.DisplayRole:
            return str(self._data[row])

    def headerData(self, section, orientation, role = Qt.DisplayRole):
        """
        Convenience function to be implemented if you want to see the column or rows headers in the views that support
        headers.
        :param section:
        :param orientation:
        :param role:
        :return:
        """
        pass

    def flags(self, index):
        """
        Mandatory function to be implemented for editable models.
        :param index:
        :return:
        """
        if not index.isValid():
            return Qt.ItemIsEnabled

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable


    def setData(self, index, value, role = Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            row = index.row()
            self._data[row] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def insertRows(self, row, count, parent):

        self.beginInsertRows(parent, row, row + count - 1)

        for row in range(0,count):
            self._data.insert(row, "Spacecraft" + str(len(self._data)))

        self.endInsertRows()

        return True

# class ListModel(QAbstractListModel):
#     def __init__(self, data, parent=None):
#         super(ListModel, self).__init__(parent)
#         # self._data = sorted(data.keys())
#         self._data = list(data.keys())
#
#     def list_clicked(self, index):
#         row = index.row()
#         key = self._data[row]
#         # table_model.set_key(key)
#
#     def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
#         return len(self._data)
#
#     def data(self, QModelIndex, int_role=None):
#         row = QModelIndex.row()
#         if int_role == Qt.DisplayRole:
#             return str(self._data[row])
#
#     # def flags(self, QModelIndex):
#     #     return Qt.ItemIsEnabled | Qt.ItemIsSelectable
