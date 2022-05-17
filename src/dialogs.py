from PyQt5 import QtWidgets

def warning_dialog(title:str, text: str) -> None:
  msg = QtWidgets.QMessageBox()
  msg.setIcon(QtWidgets.QMessageBox.Warning)
  msg.setText(text)
  msg.setWindowTitle(title)
  msg.exec_()
