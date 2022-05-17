import sys
import numpy as np
import pyqtgraph as pg
from random import randint
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.qt_designer import Ui_MainWindow
from dialogs import warning_dialog
from validators import get_equation_result, validate_equation

class MyApp(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super(self.__class__, self).__init__()
    self.setupUi(self)
    self.graph_btn.setEnabled(False)
    self.graph_btn.clicked.connect(self.plot_data)
    self.clear_graph_btn.clicked.connect(self.clear_graph)
    self.input_equation_text.textChanged.connect(self.toggle_graph_btn)
    self.actionNew.triggered.connect(self.create_new_window)
    self.actionExit.triggered.connect(self.close)
    
    self.plot.setBackground('w')
    self.plot.plotItem.showGrid(True, True)

  def create_new_window(self: QApplication) -> None:
    self.newWindow = MyApp()
    self.newWindow.show()

  def toggle_graph_btn(self: QApplication) -> None:
    equation = self.input_equation_text.text()
    if equation == '':
      self.graph_btn.setEnabled(False)
    else:
      self.graph_btn.setEnabled(True)


  def plot_data(self: QApplication) -> None:
    self.plot.plotItem.addLegend()
    equation = self.input_equation_text.text()
    x_min = self.range_from_spin.value()
    x_max = self.range_to_spin.value()
    x_step = self.range_step_spin.value()

    if x_min >= x_max:
      warning_dialog("Invalid Range", "From has to be less than To.")
      self.graph_btn.setEnabled(False)
      return

    if x_step >= x_max - x_min:
      warning_dialog("Invalid Step", "Step is to big for the range.")
      self.graph_btn.setEnabled(False)
      return

    if not validate_equation(equation):
      warning_dialog("Invalid Equation", "Please enter a valid equation.")
      self.graph_btn.setEnabled(False)
      return
    else:
      self.graph_btn.setEnabled(True)
      y_data = []
      x_data = np.arange(x_min, x_max + 1, x_step)
      for point in x_data:
        y = get_equation_result(equation, point)
        if type(y) == float:
          y_data.append(y)
        else:
          y_data.append(float('inf'))
        
      self.plot.plot(x_data, y_data, name=f'f(x)={equation}', 
        pen=pg.mkPen(color=(randint(0, 255), randint(0, 255), randint(0, 255)), 
        width=3))
      self.plot.plotItem.addLegend()

  def clear_graph(self: QApplication) -> None:
    self.plot.clear()
    pass

def main() -> None:
  app = QtWidgets.QApplication(sys.argv)
  form = MyApp()
  form.show()
  app.exec_()

if __name__ == '__main__':
  main()
