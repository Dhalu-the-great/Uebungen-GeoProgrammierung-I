import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import cv2


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('img_measurement_stereo.ui', self)
        self.show()
        # connect interactive gui elements with functions
        self.pbn_add_point.clicked.connect(self.fnc_add_point)  # left mouse click on button "Punkt hinzufügen"
        self.pbn_save.clicked.connect(self.fnc_save)  # left mouse click on button "Punkte speichern"
        self.pbn_load_img_left.clicked.connect(self.fnc_load_img_left)  # left mouse click on button "Bild laden" (l)
        self.pbn_load_img_right.clicked.connect(self.fnc_load_img_right)  # left mouse click on button "Bild laden" (r)
        self.pbn_erase_point.clicked.connect(self.fnc_err_point)  # left mouse click on button "Punkt löschen"
        self.pbn_erase_all.clicked.connect(self.fnc_err_all)  # left mouse click on button "Alles löschen"
        self.cb_point_list.currentIndexChanged.connect(self.fnc_change_color)  # changed selection of combo box

        self.scn_left = QtWidgets.QGraphicsScene(self)
        self.scn_right = QtWidgets.QGraphicsScene(self)
        self.gv_left.viewport().installEventFilter(self)  # connect event filter to the left graphics view
        self.gv_right.viewport().installEventFilter(self)  # connect event filter to the right graphics view
        self.middle_mouse_button_pressed = False  # used for pan function
        self.bool_left_image_loaded = False
        self.bool_right_image_loaded = False

        self.lst_points = list()  # init global point list

    def fnc_add_point(self):
        """
        This function relates to the "Punkt hinzufügen" button.
        The function initializes an empty point and adds it to the list 
        as well as to the combo box below "Punktauswahl für Messung"
        :return: 
        """
        # initialize an empty point
        dct_point = dict()  # point dictionary
        dct_point['nr'] = str(self.led_pt_number.text())  # point number from line edit element
        dct_point['u_left'], dct_point['v_left'] = 0.0, 0.0  # pixel coordinates u & v in the left image
        dct_point['sym_left'], dct_point['lbl_left'] = None, None  # ellipse and label in the left image
        dct_point['cross_1_left'], dct_point['cross_2_left'] = None, None  # cross hair in the left image
        dct_point['u_right'], dct_point['v_right'] = 0.0, 0.0  # pixel coordinates u & v in the right image
        dct_point['sym_right'], dct_point['lbl_right'] = None, None  # ellipse and label in the right image
        dct_point['cross_1_right'], dct_point['cross_2_right'] = None, None  # cross hair in the right image
        # append the point to the global point list
        self.lst_points.append(dct_point)
        # add the point to the combo box
        self.cb_point_list.addItem(dct_point['nr'])
        # select the new point
        int_index = self.cb_point_list.findText(dct_point['nr'], QtCore.Qt.MatchFixedString)
        if int_index >= 0:
            self.cb_point_list.setCurrentIndex(int_index)

    def fnc_save(self):
        """
        This function relates to the "Punkte speichern" button.
        It writes all points to a simple csv file.
        :return: 
        """
        str_header = "# Punktbezeichnung\tu (links) [px]\tv (links) [px]\tu (rechts) [px]\tv (rechts) [px]\n"
        str_tmpl = "{nr}\t{u_left:0.3f}\t{v_left:0.3f}\t{u_right:0.3f}\t{v_right:0.3f}\n"
        try:
            # Select file path with a file dialog
            str_file_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Punkte speichern', r'punkte.csv', r'')[0]
            with open(str_file_path, 'w') as fil_write:
                # Write file header
                fil_write.write(str_header)
                for dct_point in self.lst_points:
                    # Write values for each point
                    fil_write.write(str_tmpl.format(**dct_point))
        except:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,
                                            'Punkte nicht exportiert!',
                                            "Die Punkte konnten nicht exportiert werden.\n"
                                            "Bitte wählen Sie einen gültigen Speicherort aus...",
                                           QtWidgets.QMessageBox.Ok)
            msg_box.exec_()

    def fnc_load_img_left(self):
        """
        This function relates to the "Bild laden" button in the left.
        Opens an image and adds it to the left graphics view
        :return: 
        """
        try:
            str_img_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Bild laden', r'',
                                                                 'Bilder (*.tif *.png *.jpg *.jpeg)')[0]
            # create QImg
            cv2_img = cv2.imread(str_img_path)
            int_height, int_width, int_bytes_per_component = cv2_img.shape
            cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB, cv2_img)
            q_img = QtGui.QImage(cv2_img.data, int_width, int_height, 3 * int_width, QtGui.QImage.Format_RGB888)

            # create pixmap and add to scene
            pixmap = QtGui.QPixmap.fromImage(q_img)
            self.scn_left.addItem(QtWidgets.QGraphicsPixmapItem(pixmap))

            # set scene and zoom to fit
            self.gv_left.setScene(self.scn_left)
            self.gv_left.fitInView(self.scn_left.sceneRect(), QtCore.Qt.KeepAspectRatio)

            self.bool_left_image_loaded = True

        except:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'Kein Bild geladen!',
                                            "Bild konnte nicht geladen werden.\n"
                                            "Bitte wählen Sie ein Bild aus...",
                                            QtWidgets.QMessageBox.Ok)
            msg_box.exec_()

    def fnc_load_img_right(self):
        """
        This function relates to the "Bild laden" button in the right.
        Opens and image and adds it to the right graphics view
        :return: 
        """
        try:
            str_img_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Bild laden', r'',
                                                                 'Bilder (*.tif *.png *.jpg *.jpeg)')[0]
            # create QImg
            cv2_img = cv2.imread(str_img_path)
            int_height, int_width, int_bytes_per_component = cv2_img.shape
            cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB, cv2_img)
            qimg = QtGui.QImage(cv2_img.data, int_width, int_height, 3 * int_width, QtGui.QImage.Format_RGB888)

            # create pixmap and add to scene
            pixmap = QtGui.QPixmap.fromImage(qimg)
            self.scn_right.addItem(QtWidgets.QGraphicsPixmapItem(pixmap))

            # set scene and zoom to fit
            self.gv_right.setScene(self.scn_right)
            self.gv_right.fitInView(self.scn_right.sceneRect(), QtCore.Qt.KeepAspectRatio)

            self.bool_right_image_loaded = True

        except:
            msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'Kein Bild geladen!',
                                           "Bild konnte nicht geladen werden.\n"
                                           "Bitte wählen Sie ein Bild aus...",
                                           QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

    def fnc_change_color(self, int_index):
        """
        This function relates to the combo box below "Punktauswahl für Messung" and will be called, 
        when the selection is changed.
        Changes the point color of the selected point to yellow and of the unselected points to red
        :param int_index: 
        :return: 
        """
        if len(self.lst_points) > 0:
            # define colors
            red = QtGui.QColor(255, 0, 0)
            red_line = QtGui.QPen(red, 0, QtCore.Qt.SolidLine)
            yellow = QtGui.QColor(255, 255, 0)
            yellow_line = QtGui.QPen(yellow, 0, QtCore.Qt.SolidLine)
            # change color of all points to red
            for i in range(len(self.lst_points)):
                if self.lst_points[i]['sym_left']:
                    self.lst_points[i]['sym_left'].setPen(red_line)
                    self.lst_points[i]['cross_1_left'].setPen(red_line)
                    self.lst_points[i]['cross_2_left'].setPen(red_line)
                    self.lst_points[i]['lbl_left'].setDefaultTextColor(red)
                if self.lst_points[i]['sym_right']:
                    self.lst_points[i]['sym_right'].setPen(red_line)
                    self.lst_points[i]['cross_1_right'].setPen(red_line)
                    self.lst_points[i]['cross_2_right'].setPen(red_line)
                    self.lst_points[i]['lbl_right'].setDefaultTextColor(red)
            # change color of the selected point to yellow
            if self.lst_points[int_index]['sym_left']:
                self.lst_points[int_index]['sym_left'].setPen(yellow_line)
                self.lst_points[int_index]['cross_1_left'].setPen(yellow_line)
                self.lst_points[int_index]['cross_2_left'].setPen(yellow_line)
                self.lst_points[int_index]['lbl_left'].setDefaultTextColor(yellow)
            if self.lst_points[int_index]['sym_right']:
                self.lst_points[int_index]['sym_right'].setPen(yellow_line)
                self.lst_points[int_index]['cross_1_right'].setPen(yellow_line)
                self.lst_points[int_index]['cross_2_right'].setPen(yellow_line)
                self.lst_points[int_index]['lbl_right'].setDefaultTextColor(yellow)

    def fnc_err_point(self):
        """
        This function relates to the button "Punkt löschen".
        It removes the point selected (combo box) from both graphic scenes, from the combo box
        as well as from the point list.
        :return: 
        """
        int_index = self.cb_point_list.currentIndex()
        if int_index > -1:
            # remove point from the left graphic scene
            if self.lst_points[int_index]['sym_left']:
                self.scn_left.removeItem(self.lst_points[int_index]['sym_left'])
                self.scn_left.removeItem(self.lst_points[int_index]['cross_1_left'])
                self.scn_left.removeItem(self.lst_points[int_index]['cross_2_left'])
                self.scn_left.removeItem(self.lst_points[int_index]['lbl_left'])
            # remove point from the right graphic scene
            if self.lst_points[int_index]['sym_right']:
                self.scn_right.removeItem(self.lst_points[int_index]['sym_right'])
                self.scn_right.removeItem(self.lst_points[int_index]['cross_1_right'])
                self.scn_right.removeItem(self.lst_points[int_index]['cross_2_right'])
                self.scn_right.removeItem(self.lst_points[int_index]['lbl_right'])
            # remove point from the combo box
            self.cb_point_list.removeItem(int_index)
            # remove point from the point list
            del self.lst_points[int_index]

    def fnc_err_all(self):
        """
        This function relates to the button "Alles löschen" and removes all points.
        :return: 
        """
        if len(self.lst_points) > 0:
            for i in range(len(self.lst_points)):
                self.fnc_err_point()

    def eventFilter(self, source, event):
        """
        This is the global event filter.
        Since it is connected to both graphics views left and right, it catches the following events for both elements:
        - MouseMove and middle mouse button pressed: Pan function
        - DoubleClick of MiddleButton: Fit scene to graphics view (reset zoom)
        - MouseButtonPress of LeftButton: Measure selected Point
        - MouseButtonPress of MiddleButton: mouse button pressed = True (used for pan function)
        - MouseButtonReleased of MiddleButton: mouse button pressed = False (used for pan function)
        - Wheel: Zoom function
        :param source: GUI Element
        :param event: Event type
        :return: 
        """
        # Pan function
        if event.type() == QtCore.QEvent.MouseMove and self.middle_mouse_button_pressed:
            if source is self.gv_left.viewport() and self.bool_left_image_loaded:
                pan_start = self.gv_left.mapToScene(event.globalPos())
                self.gv_left.translate(event.x()-pan_start.x(),
                                       event.y()-pan_start.y())
                return True
            elif source is self.gv_right.viewport() and self.bool_right_image_loaded:
                pan_start = self.gv_right.mapToScene(event.globalPos())
                self.gv_right.translate(event.x()-pan_start.x(),
                                        event.y()-pan_start.y())
                return True
            else:
                return False

        # Zoom reset function
        elif event.type() == QtCore.QEvent.MouseButtonDblClick and event.button() == QtCore.Qt.MiddleButton:
            if source is self.gv_left.viewport() and self.bool_left_image_loaded:
                self.gv_left.fitInView(self.scn_left.sceneRect(), QtCore.Qt.KeepAspectRatio)
                return True
            elif source is self.gv_right.viewport() and self.bool_right_image_loaded:
                self.gv_right.fitInView(self.scn_right.sceneRect(), QtCore.Qt.KeepAspectRatio)
                return True
            else:
                return False

        # Point measurement function
        elif event.type() == QtCore.QEvent.MouseButtonPress and event.button() == QtCore.Qt.LeftButton:
            # measurement in the left graphics view
            if source is self.gv_left.viewport() and self.bool_left_image_loaded:
                int_pt_index = self.cb_point_list.currentIndex()  # get index of selected point from the combo box
                if int_pt_index >= 0:
                    # --------------------------------------------------------------------------------------------------
                    # Image Measurement (left)
                    # --------------------------------------------------------------------------------------------------
                    # transform event position from the graphics view coordinate frame to image coordinate frame
                    scene_click_pos = self.gv_left.mapToScene(event.pos())
                    # add left image measurement to the selected point within the global point list
                    self.lst_points[int_pt_index]['u_left'] = scene_click_pos.x() - 0.5  # 0 = center of the first pixel
                    self.lst_points[int_pt_index]['v_left'] = scene_click_pos.y() - 0.5  # 0 = center of the first pixel
                    # --------------------------------------------------------------------------------------------------
                    # Graphic Elements (left)
                    # --------------------------------------------------------------------------------------------------
                    # if the selected point has already been measured, then remove the former graphic elements
                    # from the left graphic scene
                    if self.lst_points[int_pt_index]['sym_left']:
                        self.scn_left.removeItem(self.lst_points[int_pt_index]['sym_left'])
                        self.scn_left.removeItem(self.lst_points[int_pt_index]['cross_1_left'])
                        self.scn_left.removeItem(self.lst_points[int_pt_index]['cross_2_left'])
                        self.scn_left.removeItem(self.lst_points[int_pt_index]['lbl_left'])

                    # add circle
                    self.lst_points[int_pt_index]['sym_left'] = self.scn_left.addEllipse(
                        self.lst_points[int_pt_index]['u_left'] - 2.5 + 0.5,  # x (left)
                        self.lst_points[int_pt_index]['v_left'] - 2.5 + 0.5,  # y (top)
                        5, 5,  # ellipse width, ellipse height
                        QtGui.QPen(QtGui.QColor(255, 255, 0), 0, QtCore.Qt.SolidLine))

                    # add crosshair
                    self.lst_points[int_pt_index]['cross_1_left'] = self.scn_left.addLine(
                        self.lst_points[int_pt_index]['u_left'] - 4.5 + 0.5,  # x1
                        self.lst_points[int_pt_index]['v_left'] - 4.5 + 0.5,  # y1
                        self.lst_points[int_pt_index]['u_left'] + 4.5 + 0.5,  # x2
                        self.lst_points[int_pt_index]['v_left'] + 4.5 + 0.5,  # y2
                        QtGui.QPen(QtGui.QColor(255, 255, 0), 0, QtCore.Qt.SolidLine))
                    self.lst_points[int_pt_index]['cross_2_left'] = self.scn_left.addLine(
                        self.lst_points[int_pt_index]['u_left'] - 4.5 + 0.5,  # x1
                        self.lst_points[int_pt_index]['v_left'] + 4.5 + 0.5,  # y1
                        self.lst_points[int_pt_index]['u_left'] + 4.5 + 0.5,  # x2
                        self.lst_points[int_pt_index]['v_left'] - 4.5 + 0.5,  # y2
                        QtGui.QPen(QtGui.QColor(255, 255, 0), 0, QtCore.Qt.SolidLine))

                    # add point number
                    self.lst_points[int_pt_index]['lbl_left'] = self.scn_left.addText(
                        self.lst_points[int_pt_index]['nr'],
                        QtGui.QFont("Arial", 20))
                    self.lst_points[int_pt_index]['lbl_left'].setPos(
                        self.lst_points[int_pt_index]['u_left'] + 2.5,  # x (left)
                        self.lst_points[int_pt_index]['v_left'] + 2.5)  # y (top)
                    self.lst_points[int_pt_index]['lbl_left'].setDefaultTextColor(QtGui.QColor(255, 255, 0))
                return True

            # measurement in the right graphics view
            elif source is self.gv_right.viewport() and self.bool_right_image_loaded:
                int_pt_index = self.cb_point_list.currentIndex()  # get index of selected point from the combo box
                if int_pt_index >= 0:
                    # --------------------------------------------------------------------------------------------------
                    # Image Measurement (right)
                    # --------------------------------------------------------------------------------------------------
                    # transform event position from the graphics view coordinate frame to image coordinate frame
                    scene_click_pos = self.gv_right.mapToScene(event.pos())
                    # add right image measurement to the selected point within the global point list
                    self.lst_points[int_pt_index]['u_right'] = scene_click_pos.x() - 0.5  # 0 = center of the first px
                    self.lst_points[int_pt_index]['v_right'] = scene_click_pos.y() - 0.5  # 0 = center of the first px
                    # --------------------------------------------------------------------------------------------------
                    # Graphic Elements (right)
                    # --------------------------------------------------------------------------------------------------
                    # if the selected point has already been measured, then remove the former graphic elements
                    # from the left graphic scene
                    if self.lst_points[int_pt_index]['sym_right']:
                        self.scn_right.removeItem(self.lst_points[int_pt_index]['sym_right'])
                        self.scn_right.removeItem(self.lst_points[int_pt_index]['cross_1_right'])
                        self.scn_right.removeItem(self.lst_points[int_pt_index]['cross_2_right'])
                        self.scn_right.removeItem(self.lst_points[int_pt_index]['lbl_right'])

                    # add circle
                    self.lst_points[int_pt_index]['sym_right'] = self.scn_right.addEllipse(
                        self.lst_points[int_pt_index]['u_right'] - 2.5 + 0.5,  # x (left)
                        self.lst_points[int_pt_index]['v_right'] - 2.5 + 0.5,  # y (top)
                        5, 5,
                        QtGui.QPen(QtGui.QColor(255, 255, 0), 0, QtCore.Qt.SolidLine))

                    # add crosshair
                    self.lst_points[int_pt_index]['cross_1_right'] = self.scn_right.addLine(
                        self.lst_points[int_pt_index]['u_right'] - 4.5 + 0.5,  # x1
                        self.lst_points[int_pt_index]['v_right'] - 4.5 + 0.5,  # y1
                        self.lst_points[int_pt_index]['u_right'] + 4.5 + 0.5,  # x2
                        self.lst_points[int_pt_index]['v_right'] + 4.5 + 0.5,  # y2
                        QtGui.QPen(QtGui.QColor(255, 255, 0), 0, QtCore.Qt.SolidLine))
                    self.lst_points[int_pt_index]['cross_2_right'] = self.scn_right.addLine(
                        self.lst_points[int_pt_index]['u_right'] - 4.5 + 0.5,  # x1
                        self.lst_points[int_pt_index]['v_right'] + 4.5 + 0.5,  # y1
                        self.lst_points[int_pt_index]['u_right'] + 4.5 + 0.5,  # x2
                        self.lst_points[int_pt_index]['v_right'] - 4.5 + 0.5,  # y2
                        QtGui.QPen(QtGui.QColor(255, 255, 0), 0, QtCore.Qt.SolidLine))

                    # add point number
                    self.lst_points[int_pt_index]['lbl_right'] = self.scn_right.addText(
                        self.lst_points[int_pt_index]['nr'],
                        QtGui.QFont("Arial", 20))
                    self.lst_points[int_pt_index]['lbl_right'].setPos(
                        self.lst_points[int_pt_index]['u_right'] + 5,  # x (left)
                        self.lst_points[int_pt_index]['v_right'] + 5)  # y (top)
                    self.lst_points[int_pt_index]['lbl_right'].setDefaultTextColor(QtGui.QColor(255, 255, 0))
                return True
            else:
                return False

        # MiddleButtonPressed function (used for pan function)
        elif event.type() == QtCore.QEvent.MouseButtonPress and event.button() == QtCore.Qt.MiddleButton:
            if source is self.gv_left.viewport() or source is self.gv_right.viewport():
                self.middle_mouse_button_pressed = True
                return True
            else:
                return False

        # MiddleButtonReleased function (used for pan function)
        elif event.type() == QtCore.QEvent.MouseButtonRelease and event.button() == QtCore.Qt.MiddleButton:
            if source is self.gv_left.viewport() or source is self.gv_right.viewport():
                self.middle_mouse_button_pressed = False
                return True
            else:
                return False

        # Zoom function
        elif event.type() == QtCore.QEvent.Wheel:
            if source is self.gv_left.viewport() and self.bool_left_image_loaded:
                self.gv_left.setTransformationAnchor(self.gv_left.AnchorUnderMouse)
                if event.angleDelta().y() > 0:
                    self.gv_left.scale(1.25, 1.25)
                elif event.angleDelta().y() < 0:
                    self.gv_left.scale(0.8, 0.8)
                return True
            elif source is self.gv_right.viewport() and self.bool_right_image_loaded:
                self.gv_right.setTransformationAnchor(self.gv_right.AnchorUnderMouse)
                if event.angleDelta().y() > 0:
                    self.gv_right.scale(1.25, 1.25)
                elif event.angleDelta().y() < 0:
                    self.gv_right.scale(0.8, 0.8)
                return True
            else:
                return False
        else:
            return False


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
