# -*- coding: utf-8 -*-

import sys
import os
import config
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential

from PIL import Image

CLEANUP_RESIZE = []

class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Document Scanner")
        MainWindow.resize(1118, 786)

        self.setMaximumWidth(1118)
        self.setMaximumHeight(786)

        self.form_recognizer = FormRecognizerClient(config.ENDPOINT, AzureKeyCredential(config.API_KEY))

        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExport_To_CSV = QAction(MainWindow)
        self.actionExport_To_CSV.setObjectName(u"actionExport_To_CSV")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 20, 1071, 711))
        self.DriversLicense = QWidget()
        self.DriversLicense.setObjectName(u"DriversLicense")
        self.licenseDragAndDrop = QLabel(self.DriversLicense)
        self.licenseDragAndDrop.setObjectName(u"licenseDragAndDrop")
        self.licenseDragAndDrop.setGeometry(QRect(150, 370, 761, 291))
        self.licenseDragAndDrop.setStyleSheet(u"QLabel{\n"
                                              "	border: 2px dashed #aaa;\n"
                                              "	border-radius: 30px;\n"
                                              "}")

        self.licenseDragAndDrop.setAlignment(Qt.AlignCenter)

        self.dlNumberLabel = QLabel(self.DriversLicense)
        self.dlNumberLabel.setObjectName(u"dlNumberLabel")
        self.dlNumberLabel.setGeometry(QRect(130, 60, 91, 41))
        font = QFont()
        font.setFamily(u"Acumin Variable Concept Condens")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dlNumberLabel.setFont(font)
        self.dlNumberLabel.setStyleSheet(u"QLabel{\n"
                                         "	border: 2px solid #aaa;\n"
                                         "	border-radius: 9px;\n"
                                         "	background-color: rgba(207, 207, 207, .4);\n"
                                         "	\n"
                                         "}")
        self.dlNumberLabel.setAlignment(Qt.AlignCenter)
        self.dlNumberText = QLineEdit(self.DriversLicense)
        self.dlNumberText.setObjectName(u"dlNumberText")
        self.dlNumberText.setGeometry(QRect(230, 60, 261, 41))
        self.addressText = QLineEdit(self.DriversLicense)
        self.addressText.setObjectName(u"addressText")
        self.addressText.setGeometry(QRect(610, 60, 321, 41))
        self.addressLabel = QLabel(self.DriversLicense)
        self.addressLabel.setObjectName(u"addressLabel")
        self.addressLabel.setGeometry(QRect(510, 60, 91, 41))
        self.addressLabel.setFont(font)
        self.addressLabel.setStyleSheet(u"QLabel{\n"
                                        "	border: 2px solid #aaa;\n"
                                        "	border-radius: 9px;\n"
                                        "	background-color: rgba(207, 207, 207, .4);\n"
                                        "	\n"
                                        "}")
        self.addressLabel.setAlignment(Qt.AlignCenter)
        self.firstNameText = QLineEdit(self.DriversLicense)
        self.firstNameText.setObjectName(u"firstNameText")
        self.firstNameText.setGeometry(QRect(230, 130, 191, 41))
        self.firstLabel = QLabel(self.DriversLicense)
        self.firstLabel.setObjectName(u"firstLabel")
        self.firstLabel.setGeometry(QRect(130, 130, 91, 41))
        self.firstLabel.setFont(font)
        self.firstLabel.setStyleSheet(u"QLabel{\n"
                                      "	border: 2px solid #aaa;\n"
                                      "	border-radius: 9px;\n"
                                      "	background-color: rgba(207, 207, 207, .4);\n"
                                      "	\n"
                                      "}")
        self.firstLabel.setAlignment(Qt.AlignCenter)
        self.lastLabel = QLabel(self.DriversLicense)
        self.lastLabel.setObjectName(u"lastLabel")
        self.lastLabel.setGeometry(QRect(440, 130, 91, 41))
        self.lastLabel.setFont(font)
        self.lastLabel.setStyleSheet(u"QLabel{\n"
                                     "	border: 2px solid #aaa;\n"
                                     "	border-radius: 9px;\n"
                                     "	background-color: rgba(207, 207, 207, .4);\n"
                                     "	\n"
                                     "}")
        self.lastLabel.setAlignment(Qt.AlignCenter)
        self.lastNameText = QLineEdit(self.DriversLicense)
        self.lastNameText.setObjectName(u"lastNameText")
        self.lastNameText.setGeometry(QRect(540, 130, 161, 41))
        self.sexText = QLineEdit(self.DriversLicense)
        self.sexText.setObjectName(u"sexText")
        self.sexText.setGeometry(QRect(820, 130, 111, 41))
        self.sexLabel = QLabel(self.DriversLicense)
        self.sexLabel.setObjectName(u"sexLabel")
        self.sexLabel.setGeometry(QRect(720, 130, 91, 41))
        self.sexLabel.setFont(font)
        self.sexLabel.setStyleSheet(u"QLabel{\n"
                                    "	border: 2px solid #aaa;\n"
                                    "	border-radius: 9px;\n"
                                    "	background-color: rgba(207, 207, 207, .4);\n"
                                    "	\n"
                                    "}")
        self.sexLabel.setAlignment(Qt.AlignCenter)
        self.ExpirationText2 = QLineEdit(self.DriversLicense)
        self.ExpirationText2.setObjectName(u"ExpirationText2")
        self.ExpirationText2.setGeometry(QRect(820, 200, 111, 41))
        self.countryText = QLineEdit(self.DriversLicense)
        self.countryText.setObjectName(u"countryText")
        self.countryText.setGeometry(QRect(540, 200, 161, 41))
        self.dobText = QLineEdit(self.DriversLicense)
        self.dobText.setObjectName(u"dobText")
        self.dobText.setGeometry(QRect(230, 200, 191, 41))
        self.dobLabel = QLabel(self.DriversLicense)
        self.dobLabel.setObjectName(u"dobLabel")
        self.dobLabel.setGeometry(QRect(130, 200, 91, 41))
        self.dobLabel.setFont(font)
        self.dobLabel.setStyleSheet(u"QLabel{\n"
                                    "	border: 2px solid #aaa;\n"
                                    "	border-radius: 9px;\n"
                                    "	background-color: rgba(207, 207, 207, .4);\n"
                                    "	\n"
                                    "}")
        self.dobLabel.setAlignment(Qt.AlignCenter)
        self.expirationLabel = QLabel(self.DriversLicense)
        self.expirationLabel.setObjectName(u"expirationLabel")
        self.expirationLabel.setGeometry(QRect(720, 200, 91, 41))
        self.expirationLabel.setFont(font)
        self.expirationLabel.setStyleSheet(u"QLabel{\n"
                                           "	border: 2px solid #aaa;\n"
                                           "	border-radius: 9px;\n"
                                           "	background-color: rgba(207, 207, 207, .4);\n"
                                           "	\n"
                                           "}")
        self.expirationLabel.setAlignment(Qt.AlignCenter)
        self.countryLabel = QLabel(self.DriversLicense)
        self.countryLabel.setObjectName(u"countryLabel")
        self.countryLabel.setGeometry(QRect(440, 200, 91, 41))
        self.countryLabel.setFont(font)
        self.countryLabel.setStyleSheet(u"QLabel{\n"
                                        "	border: 2px solid #aaa;\n"
                                        "	border-radius: 9px;\n"
                                        "	background-color: rgba(207, 207, 207, .4);\n"
                                        "	\n"
                                        "}")
        self.countryLabel.setAlignment(Qt.AlignCenter)
        self.licenseButton = QPushButton(self.DriversLicense)
        self.licenseButton.setObjectName(u"pushButton")
        self.licenseButton.setGeometry(QRect(440, 290, 191, 61))
        font1 = QFont()
        font1.setFamily(u"Acumin Variable Concept Condens")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.licenseButton.setFont(font1)
        self.licenseButton.setStyleSheet(u"QPushButton {\n"
                                         "    color: #333;\n"
                                         "    border: 2px solid #555;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "    background: qradialgradient(\n"
                                         "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                         "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                         "        );\n"
                                         "    padding: 5px;\n"
                                         "    }\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background: qradialgradient(\n"
                                         "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                         "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                         "        );\n"
                                         "    }\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    border-style: inset;\n"
                                         "    background: qradialgradient(\n"
                                         "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                         "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                         "        );\n"
                                         "    }")

        self.licenseButton.clicked.connect(self.uploadLicense)

        self.tabWidget.addTab(self.DriversLicense, "")

        self.BusinessCards = QWidget()
        self.BusinessCards.setObjectName(u"BusinessCards")
        self.phoneText = QLineEdit(self.BusinessCards)
        self.phoneText.setObjectName(u"phoneText")
        self.phoneText.setGeometry(QRect(540, 130, 161, 41))
        self.jobText = QLineEdit(self.BusinessCards)
        self.jobText.setObjectName(u"jobText")
        self.jobText.setGeometry(QRect(820, 130, 111, 41))
        self.merchantText = QLineEdit(self.BusinessCards)
        self.merchantText.setObjectName(u"merchantText")
        self.merchantText.setGeometry(QRect(230, 60, 261, 41))
        self.merchantLabel = QLabel(self.BusinessCards)
        self.merchantLabel.setObjectName(u"merchantLabel")
        self.merchantLabel.setGeometry(QRect(130, 60, 91, 41))
        self.merchantLabel.setFont(font)
        self.merchantLabel.setStyleSheet(u"QLabel{\n"
                                         "	border: 2px solid #aaa;\n"
                                         "	border-radius: 9px;\n"
                                         "	background-color: rgba(207, 207, 207, .4);\n"
                                         "	\n"
                                         "}")
        self.merchantLabel.setAlignment(Qt.AlignCenter)
        self.bCardDragAndDrop = QLabel(self.BusinessCards)
        self.bCardDragAndDrop.setObjectName(u"bCardDragAndDrop")
        self.bCardDragAndDrop.setGeometry(QRect(150, 370, 761, 291))
        self.bCardDragAndDrop.setStyleSheet(u"QLabel{\n"
                                            "	border: 2px dashed #aaa;\n"
                                            "	border-radius: 30px;\n"
                                            "}")

        self.bCardDragAndDrop.setAlignment(Qt.AlignCenter)

        self.emailText = QLineEdit(self.BusinessCards)
        self.emailText.setObjectName(u"emailText")
        self.emailText.setGeometry(QRect(230, 130, 191, 41))
        self.emailLabel = QLabel(self.BusinessCards)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(130, 130, 91, 41))
        self.emailLabel.setFont(font)
        self.emailLabel.setStyleSheet(u"QLabel{\n"
                                      "	border: 2px solid #aaa;\n"
                                      "	border-radius: 9px;\n"
                                      "	background-color: rgba(207, 207, 207, .4);\n"
                                      "	\n"
                                      "}")
        self.emailLabel.setAlignment(Qt.AlignCenter)
        self.phoneLabel = QLabel(self.BusinessCards)
        self.phoneLabel.setObjectName(u"phoneLabel")
        self.phoneLabel.setGeometry(QRect(440, 130, 91, 41))
        self.phoneLabel.setFont(font)
        self.phoneLabel.setStyleSheet(u"QLabel{\n"
                                      "	border: 2px solid #aaa;\n"
                                      "	border-radius: 9px;\n"
                                      "	background-color: rgba(207, 207, 207, .4);\n"
                                      "	\n"
                                      "}")
        self.phoneLabel.setAlignment(Qt.AlignCenter)
        self.jobLabel = QLabel(self.BusinessCards)
        self.jobLabel.setObjectName(u"jobLabel")
        self.jobLabel.setGeometry(QRect(720, 130, 91, 41))
        self.jobLabel.setFont(font)
        self.jobLabel.setStyleSheet(u"QLabel{\n"
                                    "	border: 2px solid #aaa;\n"
                                    "	border-radius: 9px;\n"
                                    "	background-color: rgba(207, 207, 207, .4);\n"
                                    "	\n"
                                    "}")
        self.jobLabel.setAlignment(Qt.AlignCenter)
        self.merchantAddressLabelText = QLineEdit(self.BusinessCards)
        self.merchantAddressLabelText.setObjectName(u"merchantAddressLabelText")
        self.merchantAddressLabelText.setGeometry(QRect(610, 60, 321, 41))
        self.merchantAddressLabel = QLabel(self.BusinessCards)
        self.merchantAddressLabel.setObjectName(u"merchantAddressLabel")
        self.merchantAddressLabel.setGeometry(QRect(510, 60, 91, 41))
        self.merchantAddressLabel.setFont(font)
        self.merchantAddressLabel.setStyleSheet(u"QLabel{\n"
                                                "	border: 2px solid #aaa;\n"
                                                "	border-radius: 9px;\n"
                                                "	background-color: rgba(207, 207, 207, .4);\n"
                                                "	\n"
                                                "}")
        self.merchantAddressLabel.setAlignment(Qt.AlignCenter)
        self.businessButton = QPushButton(self.BusinessCards)
        self.businessButton.setObjectName(u"pushButton_2")
        self.businessButton.setGeometry(QRect(440, 290, 191, 61))
        self.businessButton.setFont(font1)
        self.businessButton.setStyleSheet(u"QPushButton {\n"
                                          "    color: #333;\n"
                                          "    border: 2px solid #555;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "    background: qradialgradient(\n"
                                          "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                          "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                          "        );\n"
                                          "    padding: 5px;\n"
                                          "    }\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background: qradialgradient(\n"
                                          "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                          "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                          "        );\n"
                                          "    }\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-style: inset;\n"
                                          "    background: qradialgradient(\n"
                                          "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                          "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                          "        );\n"
                                          "    }")

        self.businessButton.clicked.connect(self.uploadBusinessCard)

        self.tabWidget.addTab(self.BusinessCards, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1118, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExport_To_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

        self.actionExport_To_CSV.triggered.connect(self.exportRouter)

        self.actionQuit.triggered.connect(self.quit)

        self.actionAbout.triggered.connect(self.about)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Document Scanner", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        # if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
        # endif // QT_CONFIG(shortcut)
        self.actionExport_To_CSV.setText(QCoreApplication.translate("MainWindow", u"Export To CSV", None))
        # if QT_CONFIG(shortcut)
        self.actionExport_To_CSV.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
        # endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        # if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
        # endif // QT_CONFIG(shortcut)
        self.licenseDragAndDrop.setText("")
        self.dlNumberLabel.setText(QCoreApplication.translate("MainWindow", u"DL #:", None))
        self.addressLabel.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.firstLabel.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.lastLabel.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.sexLabel.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.dobLabel.setText(QCoreApplication.translate("MainWindow", u"DOB:", None))
        self.expirationLabel.setText(QCoreApplication.translate("MainWindow", u"Expiration:", None))
        self.countryLabel.setText(QCoreApplication.translate("MainWindow", u"Country:", None))
        self.licenseButton.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DriversLicense),
                                  QCoreApplication.translate("MainWindow", u"Drivers License", None))
        self.merchantLabel.setText(QCoreApplication.translate("MainWindow", u"Merchant:", None))
        self.bCardDragAndDrop.setText("")
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.phoneLabel.setText(QCoreApplication.translate("MainWindow", u"Phone:", None))
        self.jobLabel.setText(QCoreApplication.translate("MainWindow", u"Job Title:", None))
        self.merchantAddressLabel.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.businessButton.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BusinessCards),
                                  QCoreApplication.translate("MainWindow", u"Business Cards", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))

    # retranslateUi

    def uploadLicense(self):
        '''
        This function will open, resize, and read drivers license images
        '''

        
        # Open Filepath from system
        file, _ = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")
        file_name = QUrl(file)
        if file != '':
            # Resize Image for Display
            newFile = file[:-len(file_name.fileName())] + file_name.fileName()[:-4] + "_resize.jpg"
            baseheight = 200
            img = Image.open(file)
            hpercent = (baseheight / float(img.size[1]))
            wsize = int((float(img.size[0]) * float(hpercent)))
            img = img.resize((wsize, baseheight), Image.ANTIALIAS)
            img.save(newFile)

            # Append filename to global variable to be cleaned up later

            CLEANUP_RESIZE.append(newFile)

            # Display Resized Image

            licenseImage = QPixmap(newFile)
            self.licenseDragAndDrop.setStyleSheet("")
            self.licenseDragAndDrop.setPixmap(licenseImage)

            # Begin text extraction and set text to QLineEdits


            QMessageBox.information(self, "Beginning Extraction",
                                    "Beginning Text Extraction\nThis will take about 10 seconds...")

            print("Extracting Text from: " + file)

            with open(file, 'rb') as f:
                data = f.read()

            try:
                # Begin the recognition process utilizing the Azure Form Recognizer AI
                task = self.form_recognizer.begin_recognize_identity_documents(data)
                form_result = task.result()

                # Parse the extracted text to the appropriate fields

                dl_number = form_result[0].fields['DocumentNumber'].value_data.text
                first_name = form_result[0].fields['FirstName'].value_data.text
                last_name = form_result[0].fields['LastName'].value_data.text
                dob = form_result[0].fields['DateOfBirth'].value_data.text
                sex = form_result[0].fields['Sex'].value_data.text
                address = form_result[0].fields['Address'].value_data.text
                country = form_result[0].fields['CountryRegion'].value
                expires = form_result[0].fields['DateOfExpiration'].value
            except:
                print("Unable to extract")
            self.dlNumberText.setText(QCoreApplication.translate("MainWindow", dl_number, None))
            self.firstNameText.setText(first_name)
            self.lastNameText.setText(last_name)
            self.dobText.setText(str(dob))
            self.sexText.setText(sex)
            self.addressText.setText(address)
            self.countryText.setText(country)
            self.ExpirationText2.setText(str(expires))

            self.finishedExtracting()
            for file in CLEANUP_RESIZE:
                os.remove(file)

        return

    def finishedExtracting(self):
        """
        Simple message box to inform use that the extraction process is finished.
        """
        QMessageBox.information(self, "Done!", "Finished Extracting")

    def uploadBusinessCard(self):
        """
        This function will extract information from a business card and return to user
        """
        # Open Filepath from system
        file, _ = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")
        file_name = QUrl(file)
        if file != '':
            # Resize Image for Display
            newFile = file[:-len(file_name.fileName())] + file_name.fileName()[:-4] + "_resize.jpg"
            baseheight = 200
            img = Image.open(file)
            hpercent = (baseheight / float(img.size[1]))
            wsize = int((float(img.size[0]) * float(hpercent)))
            img = img.resize((wsize, baseheight), Image.ANTIALIAS)
            img.save(newFile)

            # Append file to global variable for later cleanup
            CLEANUP_RESIZE.append(newFile)

            # Display Resized Image

            businessCardImage = QPixmap(newFile)
            self.bCardDragAndDrop.setStyleSheet("")
            self.bCardDragAndDrop.setPixmap(businessCardImage)

            # Begin Extracting business card text and set QLineEdits

            QMessageBox.information(self, "Beginning Extraction",
                                    "Beginning Text Extraction\nThis will take about 10 seconds...")

            image_path = file

            print("Extracting Text from: " + image_path)

            with open(image_path, 'rb') as f:
                data = f.read()

            # Pass data to form recognizer

            try:
                task = self.form_recognizer.begin_recognize_business_cards(data)
                form_result = task.result()

                # Parse fields and assign to appropriate fields for return

                merchant = str(form_result[0].fields['ContactNames'].value[0].value_data.text)
                email = str(form_result[0].fields['Emails'].value[0].value_data.text)
                phone = str(form_result[0].fields['OtherPhones'].value[0].value_data.text)
                address = str(form_result[0].fields['Addresses'].value[0].value_data.text)
                job_title = str(form_result[0].fields['JobTitles'].value[0].value_data.text)
                    
                # Set the text fields utilizing the information parsed from above.
                self.merchantText.setText(merchant)
                self.emailText.setText(email)
                self.phoneText.setText(phone)
                self.merchantAddressLabelText.setText(address)
                self.jobText.setText(job_title)

                self.finishedExtracting()

                for file in CLEANUP_RESIZE:
                    os.remove(file)



            except:
                print("Unable to Extract")

        return

    def exportRouter(self):
        """
        Connected to action Export to Text in file menu
        This function will send that command to the right function based on the tab that is open

        If the tab open is 'Drivers License' it will be prepared to export drivers license info
        Else, it will be prepared to export Business Card Info
        :return:
        """
        if self.tabWidget.currentIndex() == 0:
            if self.dlNumberText.text() != "" or self.addressText.text() != "" \
                    or self.firstNameText.text() != "" or self.lastNameText != "" \
                    or self.sexText.text() != "" or self.dobText.text() != "" \
                    or self.countryText.text() != "" or self.ExpirationText2.text() != "":
                self.exportLicenseToText()
            else:
                print("Nothing To Export!")
        if self.tabWidget.currentIndex() == 1:
            if self.merchantText.text() != "" or self.merchantAddressLabelText.text() != "" \
                    or self.emailText.text() != "" or self.phoneText.text() != "" or self.jobText != "":
                self.exportBusinessCardToText()

    def exportLicenseToText(self):

        """
        This function will create a csv file out of drivers license fields
        This function will take available fields extracted using the form recognizer and export them to a CSV file
        It will first remove any commas found in the fields to ensure extra columns aren't added on export
        :return:
        """

        fields = [self.dlNumberText.text(), self.addressText.text(), self.firstNameText.text(),
                  self.lastNameText.text(), self.sexText.text(), self.dobText.text(), self.countryText.text(),
                  self.ExpirationText2.text()]

        cleanFields = []

        # Clean up any commas found in the fields

        for field in fields:
            field = field.replace(",", "")
            cleanFields.append(field)

        appendFileResponse = QMessageBox.question(self, "Append?", "Add Information to Previous CSV?",
                                                  QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        # User answered No, so create new CSV File

        if appendFileResponse == QMessageBox.No:

            try:
                directory = str(QFileDialog.getExistingDirectory())

                filename = directory + "/" + self.firstNameText.text() + "_DriversLicense.csv"
                print(filename)
                # CSV File Variation:

                with open(filename, 'w') as f:
                    f.write("DL#,Address,First Name,Last Name,Sex,DOB,Country,Expiration\n")
                    f.write(",".join(cleanFields))
                    f.close()

                QMessageBox.about(self, "Wrote CSV File", "Exported CSV to " + directory)

            except:
                print("Unable to Open Directory")

        # User answered yes, so find an existing CSV file.

        elif appendFileResponse == QMessageBox.Yes:
            try:

                file, _ = QFileDialog.getOpenFileName(filter="csv(*.csv)")
                print(file)

                with open(file, "a") as f:
                    f.write("\n")
                    f.write(','.join(cleanFields))
                    f.close()

                QMessageBox.about(self, "Added To File", "Added Info to " + file)
            except:
                QMessageBox.about(self, "Unable To Write", "Unable To Write to That File")

        else:
            QMessageBox.information(self, "Canceled", "Canceled Export")

    def exportBusinessCardToText(self):
        """
        This function will create a csv file out of the business card fields
        This function will take available fields extracted using the form recognizer and export them to a CSV file
        It will first remove any commas found in the fields to ensure extra columns aren't added on export
        :return:
        """
        fields = [self.merchantText.text(), self.merchantAddressLabelText.text(), self.emailText.text(),
                  self.phoneText.text(), self.jobText.text()]
        cleanFields = []
        for field in fields:
            field = field.replace(",", "")
            cleanFields.append(field)

        appendFileResponse = QMessageBox.question(self, "Append?", "Add Information to Previous CSV?",
                                                  QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        # User answered no, so create a new CSV file

        if appendFileResponse == QMessageBox.No:

            try:
                directory = str(QFileDialog.getExistingDirectory())

                filename = directory + "/" + self.merchantText.text() + "_BusinessCard.csv"
                print(filename)
                # CSV File Variation:

                with open(filename, 'w') as f:
                    f.write("Merchant,Address,Email,Phone#,Job Title\n")
                    f.write(",".join(cleanFields))
                    f.close()

                QMessageBox.about(self, "Wrote CSV File", "Exported CSV to " + directory)
            except:
                print("Unable to Open Directory")

        # User answered yes, so append to a previous CSV file

        elif appendFileResponse == QMessageBox.Yes:
            try:

                file, _ = QFileDialog.getOpenFileName(filter="csv(*.csv)")
                print(file)

                with open(file, "a") as f:
                    f.write("\n")
                    f.write(','.join(cleanFields))
                    f.close()

                QMessageBox.about(self, "Added To File", "Added Info to " + file)
            except:
                QMessageBox.about(self, "Unable To Write", "Unable To Write to That File")

        else:
            QMessageBox.information(self, "Canceled", "Canceled Export")

    def quit(self):
        """
        Quit functionality for the file menu
        :return:
        """
        sys.exit(0)

    def about(self):
        """
        About textbox for file menu
        :return:
        """
        msg = QMessageBox()
        msg.about(self, "About", "<p align='center'>App by Adrien Clay<br>adrienclay36@gmail.com</p>")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setMaximumHeight(786)
    ui.setMaximumWidth(1118)
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
