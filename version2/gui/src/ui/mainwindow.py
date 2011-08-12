# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Tue Aug  9 16:15:37 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1024, 768)
        mainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.mainFrame = QtGui.QWidget(mainWindow)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.outputFrame = QtGui.QFrame(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputFrame.sizePolicy().hasHeightForWidth())
        self.outputFrame.setSizePolicy(sizePolicy)
        self.outputFrame.setObjectName(_fromUtf8("outputFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.outputFrame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.outputFrame)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setSpacing(-1)
        self.horizontalLayout_3.setMargin(2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.outputDirText = QtGui.QLineEdit(self.groupBox_2)
        self.outputDirText.setObjectName(_fromUtf8("outputDirText"))
        self.horizontalLayout_3.addWidget(self.outputDirText)
        self.outputDirButton = QtGui.QPushButton(self.groupBox_2)
        self.outputDirButton.setObjectName(_fromUtf8("outputDirButton"))
        self.horizontalLayout_3.addWidget(self.outputDirButton)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.outputFrame)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.settingWarningError = QtGui.QCheckBox(self.groupBox_3)
        self.settingWarningError.setObjectName(_fromUtf8("settingWarningError"))
        self.gridLayout_2.addWidget(self.settingWarningError, 0, 0, 1, 1)
        self.settingVerbose = QtGui.QCheckBox(self.groupBox_3)
        self.settingVerbose.setChecked(True)
        self.settingVerbose.setObjectName(_fromUtf8("settingVerbose"))
        self.gridLayout_2.addWidget(self.settingVerbose, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.outputFrame)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout.setMargin(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formatRaw = QtGui.QCheckBox(self.groupBox_4)
        self.formatRaw.setObjectName(_fromUtf8("formatRaw"))
        self.gridLayout.addWidget(self.formatRaw, 0, 0, 1, 1)
        self.formatPaged = QtGui.QCheckBox(self.groupBox_4)
        self.formatPaged.setChecked(True)
        self.formatPaged.setObjectName(_fromUtf8("formatPaged"))
        self.gridLayout.addWidget(self.formatPaged, 0, 1, 1, 1)
        self.formatHtml = QtGui.QCheckBox(self.groupBox_4)
        self.formatHtml.setObjectName(_fromUtf8("formatHtml"))
        self.gridLayout.addWidget(self.formatHtml, 1, 0, 1, 1)
        self.formatNroff = QtGui.QCheckBox(self.groupBox_4)
        self.formatNroff.setObjectName(_fromUtf8("formatNroff"))
        self.gridLayout.addWidget(self.formatNroff, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.line_2 = QtGui.QFrame(self.outputFrame)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.convertButton = QtGui.QPushButton(self.outputFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convertButton.sizePolicy().hasHeightForWidth())
        self.convertButton.setSizePolicy(sizePolicy)
        self.convertButton.setMinimumSize(QtCore.QSize(100, 0))
        self.convertButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.horizontalLayout.addWidget(self.convertButton)
        self.verticalLayout_3.addWidget(self.outputFrame)
        self.splitter = QtGui.QSplitter(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.fileGroupBox = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileGroupBox.sizePolicy().hasHeightForWidth())
        self.fileGroupBox.setSizePolicy(sizePolicy)
        self.fileGroupBox.setFlat(True)
        self.fileGroupBox.setObjectName(_fromUtf8("fileGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.fileGroupBox)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.fileButtonFrame = QtGui.QFrame(self.fileGroupBox)
        self.fileButtonFrame.setLineWidth(0)
        self.fileButtonFrame.setObjectName(_fromUtf8("fileButtonFrame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.fileButtonFrame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonClear = QtGui.QPushButton(self.fileButtonFrame)
        self.buttonClear.setObjectName(_fromUtf8("buttonClear"))
        self.horizontalLayout_2.addWidget(self.buttonClear)
        self.buttonAdd = QtGui.QPushButton(self.fileButtonFrame)
        self.buttonAdd.setObjectName(_fromUtf8("buttonAdd"))
        self.horizontalLayout_2.addWidget(self.buttonAdd)
        self.verticalLayout.addWidget(self.fileButtonFrame)
        self.fileList = QtGui.QListWidget(self.fileGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileList.sizePolicy().hasHeightForWidth())
        self.fileList.setSizePolicy(sizePolicy)
        self.fileList.setLineWidth(1)
        self.fileList.setObjectName(_fromUtf8("fileList"))
        self.verticalLayout.addWidget(self.fileList)
        self.infoFrame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoFrame.sizePolicy().hasHeightForWidth())
        self.infoFrame.setSizePolicy(sizePolicy)
        self.infoFrame.setStyleSheet(_fromUtf8("/* Disable tabwidget in-set bg\'s */\n"
"QTabWidget::pane\n"
"{\n"
"    background: none;\n"
"}"))
        self.infoFrame.setObjectName(_fromUtf8("infoFrame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.infoFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.infoSplitter = QtGui.QSplitter(self.infoFrame)
        self.infoSplitter.setOrientation(QtCore.Qt.Vertical)
        self.infoSplitter.setObjectName(_fromUtf8("infoSplitter"))
        self.groupBox = QtGui.QGroupBox(self.infoSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 19, 0, 0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.previewTabWidget = QtGui.QTabWidget(self.groupBox)
        self.previewTabWidget.setObjectName(_fromUtf8("previewTabWidget"))
        self.xmlTab = QtGui.QWidget()
        self.xmlTab.setObjectName(_fromUtf8("xmlTab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.xmlTab)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.textXml = LinedEditor(self.xmlTab)
        self.textXml.setReadOnly(True)
        self.textXml.setObjectName(_fromUtf8("textXml"))
        self.verticalLayout_7.addWidget(self.textXml)
        self.previewTabWidget.addTab(self.xmlTab, _fromUtf8(""))
        self.pagedTab = QtGui.QWidget()
        self.pagedTab.setObjectName(_fromUtf8("pagedTab"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.pagedTab)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.textPaged = LinedEditor(self.pagedTab)
        self.textPaged.setReadOnly(True)
        self.textPaged.setObjectName(_fromUtf8("textPaged"))
        self.verticalLayout_8.addWidget(self.textPaged)
        self.previewTabWidget.addTab(self.pagedTab, _fromUtf8(""))
        self.rawTab = QtGui.QWidget()
        self.rawTab.setObjectName(_fromUtf8("rawTab"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.rawTab)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.textRaw = LinedEditor(self.rawTab)
        self.textRaw.setReadOnly(True)
        self.textRaw.setObjectName(_fromUtf8("textRaw"))
        self.verticalLayout_9.addWidget(self.textRaw)
        self.previewTabWidget.addTab(self.rawTab, _fromUtf8(""))
        self.htmlTab = QtGui.QWidget()
        self.htmlTab.setObjectName(_fromUtf8("htmlTab"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.htmlTab)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.htmlView = QtWebKit.QWebView(self.htmlTab)
        self.htmlView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.htmlView.setObjectName(_fromUtf8("htmlView"))
        self.verticalLayout_10.addWidget(self.htmlView)
        self.previewTabWidget.addTab(self.htmlTab, _fromUtf8(""))
        self.nroffTab = QtGui.QWidget()
        self.nroffTab.setObjectName(_fromUtf8("nroffTab"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.nroffTab)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.textNroff = LinedEditor(self.nroffTab)
        self.textNroff.setReadOnly(True)
        self.textNroff.setObjectName(_fromUtf8("textNroff"))
        self.verticalLayout_11.addWidget(self.textNroff)
        self.previewTabWidget.addTab(self.nroffTab, _fromUtf8(""))
        self.verticalLayout_6.addWidget(self.previewTabWidget)
        self.outputTabWidget = QtGui.QTabWidget(self.infoSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.outputTabWidget.sizePolicy().hasHeightForWidth())
        self.outputTabWidget.setSizePolicy(sizePolicy)
        self.outputTabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.outputTabWidget.setObjectName(_fromUtf8("outputTabWidget"))
        self.tabOutput = QtGui.QWidget()
        self.tabOutput.setObjectName(_fromUtf8("tabOutput"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabOutput)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.textOutput = QtGui.QPlainTextEdit(self.tabOutput)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(12)
        self.textOutput.setFont(font)
        self.textOutput.setReadOnly(True)
        self.textOutput.setObjectName(_fromUtf8("textOutput"))
        self.verticalLayout_5.addWidget(self.textOutput)
        self.outputTabWidget.addTab(self.tabOutput, _fromUtf8(""))
        self.tabErrors = QtGui.QWidget()
        self.tabErrors.setObjectName(_fromUtf8("tabErrors"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabErrors)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.textErrors = QtGui.QPlainTextEdit(self.tabErrors)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(12)
        self.textErrors.setFont(font)
        self.textErrors.setStyleSheet(_fromUtf8("QPlainTextEdit\n"
"{\n"
"    color: red;\n"
"}"))
        self.textErrors.setReadOnly(True)
        self.textErrors.setObjectName(_fromUtf8("textErrors"))
        self.verticalLayout_4.addWidget(self.textErrors)
        self.outputTabWidget.addTab(self.tabErrors, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.infoSplitter)
        self.verticalLayout_3.addWidget(self.splitter)
        mainWindow.setCentralWidget(self.mainFrame)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(mainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(mainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAboutQt = QtGui.QAction(mainWindow)
        self.actionAboutQt.setObjectName(_fromUtf8("actionAboutQt"))
        self.actionPreferences = QtGui.QAction(mainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionAdd = QtGui.QAction(mainWindow)
        self.actionAdd.setObjectName(_fromUtf8("actionAdd"))
        self.actionClear = QtGui.QAction(mainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.menuFile.addAction(self.actionAdd)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuOptions.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(mainWindow)
        self.previewTabWidget.setCurrentIndex(0)
        self.outputTabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonAdd, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionAdd.trigger)
        QtCore.QObject.connect(self.buttonClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionClear.trigger)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "xml2rfc GUI", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("mainWindow", "Output directory", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDirText.setPlaceholderText(QtGui.QApplication.translate("mainWindow", "Output directory", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDirButton.setText(QtGui.QApplication.translate("mainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("mainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.settingWarningError.setText(QtGui.QApplication.translate("mainWindow", "Treat Warnings as Errors", None, QtGui.QApplication.UnicodeUTF8))
        self.settingVerbose.setText(QtGui.QApplication.translate("mainWindow", "Verbose output", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("mainWindow", "Formats", None, QtGui.QApplication.UnicodeUTF8))
        self.formatRaw.setText(QtGui.QApplication.translate("mainWindow", "Raw Text", None, QtGui.QApplication.UnicodeUTF8))
        self.formatPaged.setText(QtGui.QApplication.translate("mainWindow", "Paginated Text", None, QtGui.QApplication.UnicodeUTF8))
        self.formatHtml.setText(QtGui.QApplication.translate("mainWindow", "HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.formatNroff.setText(QtGui.QApplication.translate("mainWindow", "Nroff", None, QtGui.QApplication.UnicodeUTF8))
        self.convertButton.setText(QtGui.QApplication.translate("mainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.fileGroupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Documents", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClear.setText(QtGui.QApplication.translate("mainWindow", "Clear Queue", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setText(QtGui.QApplication.translate("mainWindow", "Add File(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.xmlTab), QtGui.QApplication.translate("mainWindow", "XML", None, QtGui.QApplication.UnicodeUTF8))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.pagedTab), QtGui.QApplication.translate("mainWindow", "Paginated Text", None, QtGui.QApplication.UnicodeUTF8))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.rawTab), QtGui.QApplication.translate("mainWindow", "Raw Text", None, QtGui.QApplication.UnicodeUTF8))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.htmlTab), QtGui.QApplication.translate("mainWindow", "HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.nroffTab), QtGui.QApplication.translate("mainWindow", "Nroff", None, QtGui.QApplication.UnicodeUTF8))
        self.outputTabWidget.setTabText(self.outputTabWidget.indexOf(self.tabOutput), QtGui.QApplication.translate("mainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.outputTabWidget.setTabText(self.outputTabWidget.indexOf(self.tabErrors), QtGui.QApplication.translate("mainWindow", "Errors", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("mainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("mainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("mainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("mainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("mainWindow", "About Xml2rfc", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setText(QtGui.QApplication.translate("mainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("mainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd.setText(QtGui.QApplication.translate("mainWindow", "Add File(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("mainWindow", "Clear Queue", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
from editor import LinedEditor
