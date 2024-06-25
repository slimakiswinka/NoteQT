import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QToolBar, QAction
from PyQt5.QtCore import Qt

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.toolbar = self.addToolBar("Main Toolbar")
        self.toolbar.setMovable(False)
        self.toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.createActions()
        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.open_action)
        self.toolbar.addAction(self.save_action)
        self.toolbar.addAction(self.copy_action)
        self.toolbar.addAction(self.paste_action)
        self.toolbar.addAction(self.exit_action)

        self.setWindowTitle("Notepad")
        self.setGeometry(100, 100, 800, 600)

    def new_file(self):
        self.text_edit.clear()
        self.text_edit.setUndoRedoEnabled(True)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text files (*.txt);;All files (*.*)")
        if filename:
            with open(filename, 'r') as f:
                self.text_edit.setPlainText(f.read())
                self.text_edit.setUndoRedoEnabled(True)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt);;All files (*.*)")
        if filename:
            with open(filename, 'w') as f:
                f.write(self.text_edit.toPlainText())

    def copy_text(self):
        self.text_edit.copy()

    def paste_text(self):
        self.text_edit.paste()

    def exit_app(self):
        self.close()

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_N:
                self.new_file()
            elif event.key() == Qt.Key_O:
                self.open_file()
            elif event.key() == Qt.Key_S:
                self.save_file()
            elif event.key() == Qt.Key_C:
                self.copy_text()
            elif event.key() == Qt.Key_V:
                self.paste_text()
            elif event.key() == Qt.Key_X:
                self.exit_app()

    def createActions(self):
        self.new_action = QAction("New", self)
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(self.new_file)

        self.open_action = QAction("Open", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.save_file)

        self.copy_action = QAction("Copy", self)
        self.copy_action.setShortcut("Ctrl+C")
        self.copy_action.triggered.connect(self.copy_text)

        self.paste_action = QAction("Paste", self)
        self.paste_action.setShortcut("Ctrl+V")
        self.paste_action.triggered.connect(self.paste_text)

        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.exit_app)

def main():
    app = QApplication(sys.argv)
    notepad = Notepad()
    notepad.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
