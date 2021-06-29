# PelagoAssignment
This assignment includes below things

Language Used : Python(3.8)
Tools Used : RobotFramework(3.2.1)
Installation guide for robotframework:
  a.Install python 3.8 and latest pip
  b.Run Command : pip install robotframework and robotframework-selenium2library
  c.Install PyCharm and open this project
  d.Open .txt file in terminal and enter following command
    robot <filename>


Automation Type : API

Breif on the Automation Strategy :
My whole idea for this automation was to perform validations between API response and UI, as UI was not working for dev.pelago have used pelago website to perform some operations, following things has been done to acheive this automation

1. Python script is prepared for getting the response from APIs for valid and invalid data so it can be further use in the validation part
2. RobotFramework is used to integrate python script and perform validations by creating test suite which is a combination of Variables, Keywords and Test Cases

I have covered 2 APIs (Product Info and Product Review) , whatever I could see on the UI which was matching to the response parameters have included in the validation part , for more covereage i may need some product knowledge.

Attached logs for your reference , can open the keywords by simply clicking on the + sign and follow the hirerchy you will get the more details in it.
