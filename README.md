# 简单的医院挂号管理系统
Simple Hospital Registration Management System  
Project for *SE3003L: Software Engineering Outline*.
Implemented using **Python 3**, with **Tkinter** and **MySQL**.

# Getting Started
Before getting started, please make sure you have these installed:
  * Python 3
  * MySQL

#### Installing Packages
  ```shell
  pip install Faker mysql-connector
  ```

#### Creating Tables in MySQL
Run `sql/tables.sql` in MySQL, using either:  
  * MySQL Workbench, if installed
  * Or `mysql -e sql/tables.sql`

#### Configuring MySQL Connector
Configurations are inside `resources\mysql_config.json`  
For details, please visit [MySQL: Python Connection Arguments](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html).

Name       | Description
:--------: | ----------------------------------
`user`     | The user name used to authenticate with the MySQL server.
`password` | The password to authenticate the user with the MySQL server.
`host`     | The host name or IP address of the MySQL server. Default is `localhost`.
`database` | The database name to use when connecting with the MySQL server. Default is `hospital` according to `tables.sql`.

#### Generating Random Entities
Please make sure you have package `Faker` installed.  
Run the generation scripts in the following order:
  * `gen_users.py`  Usernames, passwords, user types
  * `gen_departments.py`  Department names, locations
  * `gen_doctors.py`  Names, assign doctors to departments
  * `gen_patients.py`  Names, balance, personal info
  * `gen_registration.py` Registration entries, states

You should be able to see loads of entries in your database now.

#### Running the Application
Run `ui_login.py` to get started.
> Default logins:  
> Doctor: username `doctor`, password `doctor`  
> Patient: username `patient`, password `patient`