# DocumentScanner
Scans Drivers Licenses and Business Cards using Azure AI Form Recognizer and PyQT5 with QTDesigner to add a GUI.


This app utilizes Azure AI Form Recognizer Client to read images of drivers licenses or business cards and extract the text information from them in an organized way that also allows the user to export to CSV.


# UI information

![image](https://user-images.githubusercontent.com/69426533/133862469-049e412e-a25d-425a-a3bf-c46d40a2a841.png)


# Upload Image:

#### After clicking 'upload image' the user will be prompted for a file location, this will be an image of a drivers license in the case that the user is on the 'Drivers License' tab, and would be in a Business Card should the user be on the 'Business Card' tab page.

##### After selecting the file, the user will be informed that the extraction is beginning.

![image](https://user-images.githubusercontent.com/69426533/133862542-aea22275-f2e3-4883-88aa-9ce712e9d2f5.png)


After extraction, the information that could be extracted will appear in their respective fields in the window.

![image](https://user-images.githubusercontent.com/69426533/133862610-58ae7210-ff28-4392-be39-ce2fa02d0fa3.png)



### Exporting to CSV:

The user is able to export to CSV by clicking File < Export to CSV or by using **Ctrl+E**

This will then prompt the user to either create a new CSV file or to append the information to a previously created CSV file.

In the case that the user wants to add multiple sets of information from a drivers license to one CSV, they should click 'Yes'.

Otherwise, a CSV file will be created in the directory of the users choosing.

![image](https://user-images.githubusercontent.com/69426533/133862684-74ec0b76-5fd3-4aeb-94a8-9291376a1dbf.png)

