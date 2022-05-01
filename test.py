import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class LambdaTableWidget(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # position
        qtRectangle = self.frameGeometry()
        centerPoint = qtw.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        # size
        self.resize(700, 410)
        # frame title
        self.setWindowTitle("QTableWidget Test")

        # heading ???
        heading_label = qtw.QLabel('add Widget')
        heading_label.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignTop)

        # add Button
        self.addwidget_button = qtw.QPushButton("to print all the items from the first column")
        self.test_button = qtw.QPushButton("test feature")

        # table Widget
        self.table_widget = qtw.QTableWidget(12, 3)

        # ?        self.table_widget.removeRow(-1)  # Removes the row row and all its items from the table.
        # ?        self.table_widget.insertRow(-1)  # Inserts an empty row into the table at row.

        # layout
        self.main_layout = qtw.QGridLayout()
        self.main_layout.addWidget(self.addwidget_button, 0, 0)
        self.main_layout.addWidget(self.test_button, 1, 0)
        self.main_layout.addWidget(self.table_widget, 2, 0)
        self.setLayout(self.main_layout)

        self.show()

        # functionality
        self.test_button.clicked.connect(self.iterateover)
        self.addwidget_button.clicked.connect(self.iterate)  # +++

    def iterateover(self):
        row = self.table_widget.currentRow()
        colum = self.table_widget.currentColumn()
        value = self.table_widget.item(row, colum)
        print(f'value=`{value}`')
        if value:
            value = value.text()
            print(f'value=`{value}`')

    def iterate(self):
        #        for item in self.table_widget.items():

        column = 0
        # rowCount() This property holds the number of rows in the table
        for row in range(self.table_widget.rowCount()):
            # item(row, 0) Returns the item for the given row and column if one has been set; otherwise returns nullptr.
            _item = self.table_widget.item(row, column)
            if _item:
                item = self.table_widget.item(row, column).text()
                print(f'row: {row}, column: {column}, item={item}')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = LambdaTableWidget()
    sys.exit(app.exec_())