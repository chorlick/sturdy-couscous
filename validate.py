from lxml import etree
from io import StringIO
from PyQt4 import QtCore, QtGui, uic
import validator
import sys

class Validator(QtGui.QMainWindow, validator.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.xmlSchemaFileName=""
        self.xmlFileName=""
        self.xmlSchemaSelectButton.clicked.connect(self.selectXmlSchema)
        self.xmlInputSelectButton.clicked.connect(self.selectXmlFile)
        self.validationValidateAction.triggered.connect(self.validateXml)
        self.validationValidateClearAction.triggered.connect(self.clearOutput)

    def selectXmlSchema(self):
        self.xmlSchemaFileName = QtGui.QFileDialog.getOpenFileName(self, 'Open Schema', './', "Schema Files (*.xsd)" )
        self.xmlSchemaLineEdit.setText(self.xmlSchemaFileName)

    def selectXmlFile(self):
        self.xmlFileName = QtGui.QFileDialog.getOpenFileName(self, 'Open XML', './', "XML Files (*.xml)" )
        self.xmlInputLineEdit.setText(self.xmlFileName)

    def validateXml(self):
        if not self.xmlSchemaFileName:
            QtGui.QMessageBox.warning(self, "Validation Error", "Please select a valid schema file first.")
            return

        if not self.xmlFileName:
            QtGui.QMessageBox.warning(self, "Validation Error", "Please select a valid xml file first.")
            return

    def clearOutput(self):
        self.validationOutputArea.clear()


    def validateXml(self):
        with open(self.xmlSchemaFileName, 'r') as schema_file:
            schema_to_check = schema_file.read()

        with open(self.xmlFileName, 'r') as xml_file:
            xml_to_check = xml_file.read()

        xmlschema_doc = etree.parse(StringIO(schema_to_check))
        xmlschema = etree.XMLSchema(xmlschema_doc)

        # parse xml
        try:
            doc = etree.parse(StringIO(xml_to_check))
            self.validationOutputArea.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            self.validationOutputArea.insertPlainText('XML well formed, syntax ok.\n')

        # check for file IO error
        except IOError:
            self.validationOutputArea.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            self.validationOutputArea.insertPlainText('Invalid File\n')

        # check for XML syntax errors
        except etree.XMLSyntaxError as err:
            self.validationOutputArea.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            self.validationOutputArea.insertPlainText('XML Syntax Error\n')
            self.validationOutputArea.insertPlainText(str(err.error_log))
            return

        except Exception as e:
            print('Unknown error, exiting.', e)
            return

        # validate against schema
        try:
            xmlschema.assertValid(doc)
            self.validationOutputArea.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            self.validationOutputArea.insertPlainText('XML valid, schema validation ok.\n')

        except etree.DocumentInvalid as err:
            print('Schema validation error, see error_schema.log')
            with open('error_schema.log', 'w') as error_log_file:
                error_log_file.write(str(err.error_log))
                return

        except:
            print('Unknown error, exiting.')
            return

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Validator()
    window.show()
    sys.exit(app.exec_())
