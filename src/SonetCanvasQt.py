# Qt imports
from PySide2.QtWidgets import QWidget, QTreeWidgetItem, \
    QTreeWidgetItemIterator  # , QGraphicsScene, QGraphicsItem, QGraphicsRectItem

from src import database
# SONet imports
from src import sonet_canvas_ui
from src.SonetSpacecraft import SonetSpacecraft
from src.SonetTrajectoryFilter import SonetTrajectoryFilter
from src.SonetUtils import sonet_log, SonetLogType, SpacecraftType, TripType


# ==============================================================================================
# ==============================================================================================
#
#
#                                    CLASS SonetCanvasQt
#
#
# ==============================================================================================
# ==============================================================================================


class SonetCanvasQt(QWidget, sonet_canvas_ui.Ui_sonet_canvas):
    def __init__(self, *args, mw=None):
        super(SonetCanvasQt, self).__init__(*args)
        self.setupUi(self)
        self.mw = mw  # Pointer to the main window.
        self.show()

    def clear_tree_view(self, p_tw='All'):
        """
        Clear the all the tree widgets (p_tw='All') or a specific one.

        :param p_tw: 'All'|'S/C Info'|'Trajectories Filter'|'Active Trips'
        """
        if p_tw == 'All':
            self.treeW_sc_info_filter.clear()
            self.treeW_trajectories_filter.clear()
            self.treeW_active_trips.clear()
        elif p_tw == 'S/C Info':
            self.treeW_sc_info_filter.clear()
        elif p_tw == 'Trajectories Filter':
            self.treeW_trajectories_filter.clear()
        elif p_tw == 'Active Trips':
            self.treeW_active_trips.clear()

    def clicked_sc(self, a_index):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.clicked_sc')

        sc: SonetSpacecraft = self.mw.get_list_model().get_spacecraft(a_index=a_index)

        # Update the tree widgets.
        self.clear_tree_view(p_tw='All')
        self.fill_tree_widget_sc_info(sc)
        # self.fill_tree_widget_trajectories_filter() #TODO
        # self.fill_tree_widget_trajectories_filter() #TODO

        self.post_actions()

    def expand_tree_widget(self, p_tw='All'):
        # For the selected tree widgets.
        tree_widgets = self.get_tree_widgets(p_tw)

        # Expand their items.
        for tw in tree_widgets:
            for item in SonetCanvasQt.iter_tree_widget(tw):
                item.setExpanded(True)

    def fill_dependencies(self, a_tw_dependencies_root, a_sc):
        sc_dependencies = self.get_dependencies_sc(a_sc)

        for dependency in sc_dependencies:
            new_item = QTreeWidgetItem(a_tw_dependencies_root, [dependency, sc_dependencies.get(dependency)])
        stop = True

    def fill_dependents(self, a_tw_dependents_root, a_sc):
        pass

    def fill_tree_widget_active_trips(self):
        pass

    def fill_tree_widget_sc_info(self, a_sc: SonetSpacecraft):
        # Get the s/c payload type.
        sc_payload = self.get_sc_payload(a_sc)

        self.treeW_sc_info_filter.setHeaderLabels(['S/C', ''])

        tw_item_sc = QTreeWidgetItem(self.treeW_sc_info_filter, [a_sc.get_name(), sc_payload])

        tw_item_sc_dependencies = QTreeWidgetItem(tw_item_sc, ['Dependencies', ''])
        self.fill_dependencies(tw_item_sc_dependencies, a_sc)

        tw_item_sc_dependents = QTreeWidgetItem(tw_item_sc, ['Dependents', ''])
        self.fill_dependents(tw_item_sc_dependents, a_sc)

    def fill_tree_widget_trajectories_filter(self):
        pass

    def get_dependencies_sc(self, a_sc):
        """
        Get the s/c on which a_sc depends on (e.g. one of its trajectories depend on another s/c's given trajectory.
        :param a_sc: the s/c to which query all its dependencies s/cs.
        :return: str
        """
        res = {}

        the_filters = a_sc.get_filter(p_get_list=True)
        stop = True
        for f in the_filters:
            data = SonetTrajectoryFilter._get_activated_filters_of_a_given_type(f.get_data(), True, 'ComplexDate')
            n = len(data)  # LESSON LEARNED: if you put len(data) inside range(), strange things happen. :S
            if not data.empty:
                for row in range(n):
                    complex_date_filter = data[row]
                    dependency_name = complex_date_filter[6]
                    dependency_payload = self.get_sc_payload(database.get_spacecraft(dependency_name))

                    f_trip = TripType.convert_to_str(f.get_trip_type())
                    dependency_trip = complex_date_filter[7]
                    dependency_type = self.get_dependency_type(f_trip, dependency_trip)

                    res[dependency_name] = dependency_payload + ' ' + dependency_type

        return res

    def get_dependency_type(self, a_sc_trip: str, a_dependency_trip: str):
        res = ''

        if a_sc_trip == 'Earth - Mars':
            res = res + '>'
        elif a_sc_trip == 'Mars - Earth':
            res = res + '<'

        if a_dependency_trip == 'Earth - Mars':
            res = res + '>'
        elif a_dependency_trip == 'Mars - Earth':
            res = res + '<'

        return '(' + res + ')'

    def get_dependents_sc(self, a_sc):
        """
        Get the s/c which depend on a_sc (e.g. one of their trajectories depend on a_sc given trajectory.
        :param a_sc: the s/c to which query all its dependent s/cs.
        :return: str
        """
        pass

    def get_sc_payload(self, a_sc):
        sc_payload = SpacecraftType.get_str(a_sc.get_type())
        # Add a '*' if the s/c has also Earth-Mars trajectory.
        if a_sc.get_has_return_trajectory():
            sc_payload = sc_payload + '*'
        return sc_payload

    def get_tree_widgets(self, p_tw='All'):
        res = []

        if p_tw == 'All':
            res.append(self.treeW_sc_info_filter)
            res.append(self.treeW_trajectories_filter)
            res.append(self.treeW_active_trips)
        elif p_tw == 'S/C Info':
            res.append(self.treeW_sc_info_filter)
        elif p_tw == 'Trajectories Filter':
            res.append(self.treeW_trajectories_filter)
        elif p_tw == 'Active Trips':
            res.append(self.treeW_active_trips)

        return res

    def init(self):
        # Align the window position with the main window.
        new_pos = self.mw.pos()
        new_pos.setX(new_pos.x() + self.mw.width())
        new_pos.setY(self.mw.y())
        self.move(new_pos)

        # Widgets settings.

        # Connect the main window list click event to the canvas window.
        self.mw.sonet_mission_tree_qlv.clicked.connect(self.clicked_sc)

    def iter_tree_widget(a_root):
        iterator = QTreeWidgetItemIterator(a_root)
        while True:
            item = iterator.value()
            if item is not None:
                yield item
                iterator += 1
            else:
                break

    def post_actions(self):
        self.expand_tree_widget(p_tw='All')
        self.resize_columns_to_contents(p_tw='All')

    def resize_columns_to_contents(self, p_tw='All'):
        # For the selected tree widgets.
        tree_widgets = self.get_tree_widgets(p_tw)

        # Resize their columns to the contents.
        for tw in tree_widgets:
            n_cols = tw.columnCount()
            for col in range(n_cols):
                tw.resizeColumnToContents(col)

