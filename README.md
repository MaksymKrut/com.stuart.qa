
Test Automation Framework for Stuart.com

Written on Python+Selenium+Behave(BDD) bundle.

@author 'Maksym Krutskykh'

@email 'maximkrut@yahoo.com'

@github 'https://gist.github.com/MaksymKrut'

To start using it just do next steps:
1. sudo pip install selenium behave
2. Clone repository
3. cd com.stuart.qa
4. Ask from your fellow contributor config.ini file with credentials
   and put it into support folder
5. Use tags to run specific test scenarios:
    behave --tags @login
    behave --tags @logout
    behave --tags @order