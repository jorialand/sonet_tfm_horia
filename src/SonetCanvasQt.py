

from PySide2.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem, QGraphicsRectItem
from PySide2.QtCore import QRectF
from src import sonet_canvas_ui

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
    def __init__(self, *args, **kwargs):
        super(SonetCanvasQt, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.sonet_canvas_scene = QGraphicsScene(self)
        self.sonet_canvas_view.setScene(self.sonet_canvas_scene)
        self.draw_rectangle()

    def draw_rectangle(self):
        self.sonet_canvas_scene.addText('Hello!')

        rect_item = QGraphicsRectItem(QRectF(0, 0, 100, 100))
        rect_item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.sonet_canvas_scene.addItem(rect_item)


