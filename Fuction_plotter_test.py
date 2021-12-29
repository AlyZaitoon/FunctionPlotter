import unittest
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from Function_plotter import Ui_FunctionPlotter
import sys
#defining Qtapplication and main window object for testing
app = QtWidgets.QApplication(sys.argv)
FunctionPlotter=Ui_FunctionPlotter()
FunctionPlotter.setupUi()
#test function plotter containing all unit tests for modules used
class TestFunctionPlotter(unittest.TestCase):
    #testing plot function with different type of plots
    def test_curve_linear_plot(self):
        #defining x as numpy array of length 200
        x=np.linspace(1,2,200)
        #defining y as numpy array of length 200 from the range of x's defined
        y=2*x-2
        #setting the gui text and line edits to test the plot_function
        FunctionPlotter.MinimumLineEdit.setText("1")
        FunctionPlotter.MaximumLineEdit.setText("2")
        FunctionPlotter.functionTextEdit.setText("2*x-2")
        #calling the plot_fucnction to be tested
        plot,=FunctionPlotter.plot_function(False)
        #extracting the x and y arrays plotted
        x_data=plot.get_data()[0]
        y_data=plot.get_data()[1]
        #comparing the plotted x,y arrays with the mathematically calculated arrays
        self.assertTrue((y==y_data).all())
        self.assertTrue((x==x_data).all())
    #following test cases are similar with more complex functions
    def test_curve_sqr_plot(self):
        x=np.linspace(1,2,200)
        y=np.square(x)
        FunctionPlotter.MinimumLineEdit.setText("1")
        FunctionPlotter.MaximumLineEdit.setText("2")
        FunctionPlotter.functionTextEdit.setText("x^2")
        plot,=FunctionPlotter.plot_function(False)
        x_data=plot.get_data()[0]
        y_data=plot.get_data()[1]
        self.assertTrue((y==y_data).all())
        self.assertTrue((x==x_data).all())
    def test_curve_polynominal_plot(self):
        x=np.linspace(2,4,200)
        y=np.power(x,3)-3*np.square(x)+2*x-5
        FunctionPlotter.MinimumLineEdit.setText("2")
        FunctionPlotter.MaximumLineEdit.setText("4")
        FunctionPlotter.functionTextEdit.setText("x^3-3*x^2+2*x-5")
        plot,=FunctionPlotter.plot_function(False)
        x_data=plot.get_data()[0]
        y_data=plot.get_data()[1]
        self.assertTrue((y==y_data).all())
        self.assertTrue((x==x_data).all())
    def test_curve_exponential_plot(self):
        x=np.linspace(2,4,200)
        y=np.exp(x)+2*x
        FunctionPlotter.MinimumLineEdit.setText("2")
        FunctionPlotter.MaximumLineEdit.setText("4")
        FunctionPlotter.functionTextEdit.setText("exp(x)+2*x")
        plot,=FunctionPlotter.plot_function(False)
        x_data=plot.get_data()[0]
        y_data=plot.get_data()[1]
        self.assertTrue((y==y_data).all())
        self.assertTrue((x==x_data).all())
    def test_curve_sinusoidal_plot(self):
        x=np.linspace(2,4,200)
        y=np.sin(x)+np.cos(x)-2*x
        FunctionPlotter.MinimumLineEdit.setText("2")
        FunctionPlotter.MaximumLineEdit.setText("4")
        FunctionPlotter.functionTextEdit.setText("sin(x)+cos(x)-2*x")
        plot,=FunctionPlotter.plot_function(False)
        x_data=plot.get_data()[0]
        y_data=plot.get_data()[1]
        self.assertTrue((y==y_data).all())
        self.assertTrue((x==x_data).all())
    #testing the function validation function and making sure it displays the right message when empty function is entered by the user
    def test_function_validation(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.function_validation()
        self.assertEqual(FunctionPlotter.msgFunction.text(),"U must enter a function to be plotted")
    #testing all the buttons and making sure they type properly to the function text edit
    def test_type_function_1(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.oneButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"1")
    def test_type_function_2(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.twoButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"2")
    def test_type_function_3(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.threeButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"3")
    def test_type_function_4(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.fourButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"4")
    def test_type_function_5(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.fiveButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"5")
    def test_type_function_6(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.sixButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"6")
    def test_type_function_7(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.sevenButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"7")
    def test_type_function_8(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.eightButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"8")
    def test_type_function_9(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.nineButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"9")
    def test_type_function_0(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.zeroButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"0")
    def test_type_function_dec(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.decimalButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),".")
    def test_type_function_var(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.variableButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"x")
    def test_type_function_power(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.powerButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"^")
    def test_type_function_add(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.additionButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"+")
    def test_type_function_sub(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.subtractionButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"-")
    def test_type_function_mul(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.multiplicationButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"*")
    def test_type_function_div(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.divisionButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"/")
    def test_type_function_cos(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.cosineButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"cos(x)")
    def test_type_function_sin(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.sineButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"sin(x)")
    def test_type_function_exp(self):
        FunctionPlotter.functionTextEdit.setText("")
        FunctionPlotter.exponentialButton.click()
        self.assertEqual(FunctionPlotter.functionTextEdit.toPlainText(),"exp(x)")
    #testing the range_validation function that makes sure that at each case of eneting empty input the right mesage is dispalyed to user
    #to make him/her understand which field is empty
    def test_range_validation_firstcase(self):
        FunctionPlotter.MinimumLineEdit.setText("")
        FunctionPlotter.MaximumLineEdit.setText("")
        FunctionPlotter.range_validation()
        self.assertEqual(FunctionPlotter.msgRange.text(),"U must enter Maximum and Minimum value for range")
    def test_range_validation_secondcase(self):
        FunctionPlotter.MinimumLineEdit.setText("1")
        FunctionPlotter.MaximumLineEdit.setText("")
        FunctionPlotter.range_validation()
        self.assertEqual(FunctionPlotter.msgRange.text(),"U must enter Maximum value for range")
    def test_range_validation_thirdcase(self):
        FunctionPlotter.MinimumLineEdit.setText("")
        FunctionPlotter.MaximumLineEdit.setText("1")
        FunctionPlotter.range_validation()
        self.assertEqual(FunctionPlotter.msgRange.text(),"U must enter Minimum value for range")
    #testing range_validation_numeric function and making sure that all cases are working correctly and displaying messages to make the user 
    #understand which field is not numeric or if minimum value is greater than or equal maximum value for range of plotting(identifing the problems introduced by invalid inputs)
    def test_range_validation_numeric_firstcase(self):
        FunctionPlotter.MinimumLineEdit.setText("a")
        FunctionPlotter.MaximumLineEdit.setText("b")
        FunctionPlotter.range_validation_numeric()
        self.assertEqual(FunctionPlotter.msgRangenumeric.text(),"U must enter a numeric value for range of plotting(space is not a numeric value)")
    def test_range_validation_numeric_secondcase(self):
        FunctionPlotter.MinimumLineEdit.setText("1")
        FunctionPlotter.MaximumLineEdit.setText("b")
        FunctionPlotter.range_validation_numeric()
        self.assertEqual(FunctionPlotter.msgRangenumeric.text(),"U must enter a numeric value for maxiumum range of plotting(space is not a numeric value)")
    def test_range_validation_numeric_thirdcase(self):
        FunctionPlotter.MinimumLineEdit.setText("a")
        FunctionPlotter.MaximumLineEdit.setText("1")
        FunctionPlotter.range_validation_numeric()
        self.assertEqual(FunctionPlotter.msgRangenumeric.text(),"U must enter a numeric value for minimum range of plotting(space is not a numeric value)")
    def test_range_validation_numeric_fourthcase(self):
        FunctionPlotter.MinimumLineEdit.setText("2")
        FunctionPlotter.MaximumLineEdit.setText("1")
        FunctionPlotter.range_validation_numeric()
        self.assertEqual(FunctionPlotter.msgRangenumeric.text(),"minimum value is larger than maximum value for range of plotting")
    def test_range_validation_numeric_fifthcase(self):
        FunctionPlotter.MinimumLineEdit.setText("1")
        FunctionPlotter.MaximumLineEdit.setText("1")
        FunctionPlotter.range_validation_numeric()
        self.assertEqual(FunctionPlotter.msgRangenumeric.text(),"minimum value is equal to maximum value for range of plotting")
        self.assertEqual(FunctionPlotter.msgRangenumeric.detailedText(),"Range of plotting with equal minimum and maximum values means that u are ploting 1 point so plot will not be visible")
    

if __name__ == '__main__':
    unittest.main()
    