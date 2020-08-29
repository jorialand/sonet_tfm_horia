from src.Utils import ObjectType, build_mock_DataFrame

class SonetSpacecraft:
    def __init__(self):
        # Attributes
        self._type = ObjectType.SPACECRAFT

        # Pandas model
        dir_path = '/Users/Jorialand/code/tfm/sonet/sonet_tfm_horia/src/'
        #self._df_outgoing = pd.read_csv(dir_path + '10kPCP_Earth2Mars.txt')
        #self._df_incoming = pd.read_csv(dir_path + '10kPCP_Mars2Earth.txt')
        self._df_outgoing = build_mock_DataFrame()
        self._df_incoming = build_mock_DataFrame()
        #self.model_outgoing = PCPPandasModel(df_outgoing)
        #self.model_incoming = PCPPandasModel(df_incoming)

        # print(df_outgoing.head())
        # print(df_incoming.head( ))


# class PCPPandasModel(QAbstractTableModel):
#
#     """
#     Qt table model representing the Porkchop plot data coming from Pandas.
#     rowCount(), columnCount(), and data() are required to be implemented to properly subclass QAbstractTableModel.
#     +info: https://www.learnpyqt.com/courses/model-views/qtableview-modelviews-numpy-pandas/
#     """
#
#     def __init__(self, data):
#         # QAbstractTableModel.__init__(self)
#         super(PCPPandasModel, self).__init__()
#         self._data = data
#
#     def rowCount(self, parent=None):
#         """
#         The number of rows of the table.
#         """
#
#         return self._data.shape[0]
#
#     def columnCount(self, parent=None):
#         """
#         The number of columns of the table.
#         """
#         return self._data.shape[1]
#
#     def data(self, index, role=Qt.DisplayRole):
#         """
#         The structure of the pandas data.
#         :param index: the current index. The row and the column.
#         :param role: Qt.DisplayRole means what is being represented.
#         """
#
#         if not index.isValid():
#             return None
#
#         row = index.row()
#         # column = index.column()
#
#         if role == Qt.DisplayRole:
#             # Get the raw value
#             value = self._data.iloc[index.row(), index.column()]
#             # return str(self._data.iloc[index.row(), index.column()])
#
#             # Perform per-type checks and render accordingly.
#             if isinstance(value, datetime):
#                 # Render time to YYY-MM-DD.
#                 return value.strftime("%Y-%m-%d")
#
#             if isinstance(value, float):
#                 # Render float to 2 dp
#                 return "%.2f" % value
#
#             if isinstance(value, str):
#                 # Render strings with quotes
#                 return '"%s"' % value
#
#             # Default (anything not captured above: e.g. int)
#             return value
#
#         if role == Qt.BackgroundRole:
#             # Pair rows will have different color, to visually distinguish them from the even ones.
#             if row % 2 is not 0:
#                 return QColor(255, 230, 255)
#             # Very light blue 230, 242, 255
#             # Very light purple 240, 240, 245
#             # Very light pink 255, 230, 255
#
#         return None
#
#     def headerData(self, section, orientation, role):
#         """
#
#         :param section:
#         :param orientation:
#         :param role:
#         """
#         if role == Qt.DisplayRole:
#             if orientation == Qt.Horizontal:
#                 return str(self._data.columns[section])
#             if orientation == Qt.Vertical:
#                 return str(self._data.index[section])
#         return None
