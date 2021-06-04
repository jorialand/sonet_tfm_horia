# Qt imports
from PySide2.QtCore import Qt
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
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.clear_tree_view')

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

        if a_index.row() is -1:
            sonet_log(SonetLogType.INFO, 'SonetCanvasQt.clicked_sc."No s/c selected"')
            return

        # Update the tree widgets.
        self.clear_tree_view(p_tw='All')
        self.fill_tree_widget_sc_info(sc)
        self.fill_tree_widget_trajectories_filter(sc)
        self.fill_tree_widget_active_trips(sc)

        self.post_actions()

    def expand_tree_widget(self, p_tw='All'):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.expand_tree_widget')

        # For the selected tree widgets.
        tree_widgets = self.get_tree_widgets(p_tw)

        # Expand their items.
        for tw in tree_widgets:
            for item in SonetCanvasQt.iter_tree_widget(tw):
                item.setExpanded(True)

    def fill_dependencies(self, a_tw_dependencies_root, a_sc):
        """
        Add the items which a_sc depends on.
        :param a_tw_dependencies_root: dependencies item root.
        :param a_sc: s/c
        """
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.fill_dependencies')

        sc_dependencies = self.get_dependencies_sc(a_sc)

        for dependency in sc_dependencies:
            new_item = QTreeWidgetItem(a_tw_dependencies_root, [dependency, sc_dependencies.get(dependency)])

    def fill_dependents(self, a_tw_dependents_root, a_sc):
        """
        Add the items which depend on a_sc.
        :param a_tw_dependents_root: dependents item root.
        :param a_sc: s/c
        """
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.fill_dependents')

        sc_dependents = self.get_dependents_sc(a_sc)

        for dependent in sc_dependents:
            new_item = QTreeWidgetItem(a_tw_dependents_root, [dependent, sc_dependents.get(dependent)])

    def fill_tree_widget_active_trips(self, a_sc: SonetSpacecraft):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.fill_tree_widget_active_trips')

        selected_trajectories = a_sc.get_trajectory_selected(p_get_trajectories=True)

        self.treeW_active_trips.setHeaderLabels(['Trip', 'DepDates', 'ArrivDates','tof', 'dvt'])
        if a_sc.get_has_return_trajectory():
            tw_item_earth_mars = QTreeWidgetItem(self.treeW_active_trips, ['Earth - Mars', '', '', '', ''])
            self.fill_active_trips(a_sc, 'Earth - Mars', tw_item_earth_mars)

            tw_item_mars_earth = QTreeWidgetItem(self.treeW_active_trips, ['Mars - Earth', '', '', '', ''])
            self.fill_active_trips(a_sc, 'Mars - Earth', tw_item_mars_earth)
        else:
            tw_item_earth_mars = QTreeWidgetItem(self.treeW_active_trips, ['Earth - Mars', '', '', '', ''])
            self.fill_active_trips(a_sc, 'Earth - Mars', tw_item_earth_mars)

    def fill_active_trips(self, a_sc, a_trip, a_tw_trip_root):
        trajectories = a_sc.get_trajectory_selected(p_get_trajectories=True)
        trajectory = trajectories.get(a_trip)
        if trajectory is not None:
            new_item = QTreeWidgetItem(a_tw_trip_root,
                                       ['',
                                        trajectory.DepDates.toString(Qt.SystemLocaleShortDate),
                                        trajectory.ArrivDates.toString(Qt.SystemLocaleShortDate),
                                        "{:.0f}".format(trajectory.tof),
                                        "{:.2f}".format(trajectory.dvt)])

    def fill_tree_widget_sc_info(self, a_sc: SonetSpacecraft):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.fill_tree_widget_sc_info')

        self.treeW_sc_info_filter.setHeaderLabels(['S/C', ''])

        tw_item_sc = QTreeWidgetItem(self.treeW_sc_info_filter, [a_sc.get_name(), self.get_sc_payload(a_sc)])

        tw_item_sc_dependencies = QTreeWidgetItem(tw_item_sc, ['Dependencies', ''])
        self.fill_dependencies(tw_item_sc_dependencies, a_sc)

        tw_item_sc_dependents = QTreeWidgetItem(tw_item_sc, ['Dependents', ''])
        self.fill_dependents(tw_item_sc_dependents, a_sc)

    def fill_tree_widget_trajectories_filter(self, a_sc: SonetSpacecraft):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.fill_tree_widget_trajectories_filter')

        self.treeW_trajectories_filter.setHeaderLabels(['Trip', 'Filter Type', 'Filter'])

        if a_sc.get_has_return_trajectory():
            tw_item_earth_mars = QTreeWidgetItem(self.treeW_trajectories_filter, ['Earth - Mars', '', ''])
            self.fill_filter(a_sc, 'Earth - Mars', tw_item_earth_mars)

            tw_item_mars_earth = QTreeWidgetItem(self.treeW_trajectories_filter, ['Mars - Earth', '', ''])
            self.fill_filter(a_sc, 'Mars - Earth', tw_item_mars_earth)
        else:
            tw_item_earth_mars = QTreeWidgetItem(self.treeW_trajectories_filter, ['Earth - Mars', '', ''])
            self.fill_filter(a_sc, 'Earth - Mars', tw_item_earth_mars)

    def fill_filter(self, a_sc, a_trip, a_tw_trip_root):
        if a_trip == 'Earth - Mars':
            a_trip = 0
        elif a_trip == 'Mars - Earth':
            a_trip = 1

        the_filters_dict = \
            SonetTrajectoryFilter._get_activated_filters_of_a_given_type(
                a_sc.get_filter(p_get_list=True)[a_trip]._data, True, 'All')
        filters_list = the_filters_dict.keys()
        for f in filters_list:
            filter = the_filters_dict.get(f)
            for ff in filter:
                new_item = QTreeWidgetItem(a_tw_trip_root, ['', f, ' '.join(ff)])

    def get_dependencies_sc(self, a_sc):
        """
        Get the s/c on which a_sc depends on (e.g. one of its trajectories depend on another s/c's given trajectory.
        :param a_sc: the s/c to which query all its dependencies s/cs.
        :return: str
        """
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.get_dependencies_sc')

        res = {}

        # It can be a list of one or two filters (e.g. Earth-Mars, or E-M + Mars-Earth).
        the_filters = a_sc.get_filter(p_get_list=True)

        for f in the_filters:
            # Get the ComplexDate filter (only consider activated ones).
            data = SonetTrajectoryFilter._get_activated_filters_of_a_given_type(f.get_data(), True, 'ComplexDate')
            n = len(data)  # LESSON LEARNED: if you put len(data) inside range(), strange things happen. :S
            if n:
                data = data.to_list()
                for row in range(n):
                    # Add all the ComplexDate filters (aka rows) of this filter.
                    complex_date_filter = data[row]
                    dependency_name = complex_date_filter[6]
                    dependency_payload = self.get_sc_payload(database.get_spacecraft(dependency_name))

                    my_trip = TripType.convert_to_str(f.get_trip_type())
                    dependency_trip = complex_date_filter[7]
                    dependency_type = self.get_dependency_type(my_trip, dependency_trip)

                    res[dependency_name] = dependency_payload + ' ' + dependency_type

        return res

    def get_dependency_type(self, a_sc_trip: str, a_dependency_trip: str):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.get_dependency_type')

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
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.get_dependents_sc')

        res = {}

        # Traverse all s/c but this one.
        sc_list = database.get_spacecrafts_list(p_return_objects=True)
        sc_list.remove(a_sc)

        # Check which filters are pointing to a_sc.
        for sc in sc_list:
            # the_filters can be a list of one or two filters (e.g. Earth-Mars, or E-M + Mars-Earth).
            the_filters = sc.get_filter(p_get_list=True)
            for f in the_filters:
                # Get the ComplexDate filter (only consider activated ones).
                data = SonetTrajectoryFilter._get_activated_filters_of_a_given_type(f.get_data(), True, 'ComplexDate')
                n = len(data)  # LESSON LEARNED: if you put len(data) inside range(), strange things happen. :S
                if n:
                    data = data.to_list()
                    for row in range(n):
                        complex_date_filter = data[row]
                        # If a given s/c points to this one, then it's dependent.
                        is_dependent = complex_date_filter[6] == a_sc.get_name()
                        if is_dependent:
                            # Add all the ComplexDate filters (aka rows) of this filter.
                            dependent_name = sc.get_name()
                            dependent_payload = self.get_sc_payload(sc)

                            my_trip = complex_date_filter[7]
                            dependent_trip = TripType.convert_to_str(f.get_trip_type())
                            dependent_type = self.get_dependency_type(my_trip, dependent_trip)

                            res[dependent_name] = dependent_payload + ' ' + dependent_type

        return res

    def get_sc_payload(self, a_sc):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.get_sc_payload')

        sc_payload = SpacecraftType.get_str(a_sc.get_type())
        # Add a '*' if the s/c has also Earth-Mars trajectory.
        if a_sc.get_has_return_trajectory():
            sc_payload = sc_payload + '*'
        return sc_payload

    def get_tree_widgets(self, p_tw='All'):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.get_tree_widgets')

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
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.init')

        # Align the window position with the main window.
        new_pos = self.mw.pos()
        new_pos.setX(new_pos.x() + self.mw.width())
        new_pos.setY(self.mw.y())
        self.move(new_pos)

        # Widgets settings.

        # Connect the main window list click event to the canvas window.
        self.mw.sonet_mission_tree_qlv.clicked.connect(self.clicked_sc)

    def iter_tree_widget(a_root):
        # sonet_log(SonetLogType.INFO, 'SonetCanvasQt.iter_tree_widget')

        iterator = QTreeWidgetItemIterator(a_root)
        while True:
            item = iterator.value()
            if item is not None:
                yield item
                iterator += 1
            else:
                break

    def post_actions(self):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.post_actions')

        self.expand_tree_widget(p_tw='All')
        self.resize_columns_to_contents(p_tw='All')

    def resize_columns_to_contents(self, p_tw='All'):
        sonet_log(SonetLogType.INFO, 'SonetCanvasQt.resize_columns_to_contents')

        # For the selected tree widgets.
        tree_widgets = self.get_tree_widgets(p_tw)

        # Resize their columns to the contents.
        for tw in tree_widgets:
            n_cols = tw.columnCount()
            for col in range(n_cols):
                tw.resizeColumnToContents(col)
