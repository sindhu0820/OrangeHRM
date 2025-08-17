# OrangeHRM

**Manual Test Script – OrangeHRM PIM Workflow**
**Test Case ID:** TC_ORANGEHRM_PIM_001
Title:Login, Add Employee(s), Verify, and Logout in OrangeHRM

**Preconditions:**
User has valid OrangeHRM credentials: Admin / admin123
Browser is installed and working.

**Steps & Expected Results:**
1.	Open browser & navigate to https://opensource-demo.orangehrmlive.com/web/index.php/auth/login,	Login page should load
2.	Enter username: Admin and password: admin123	
3.	Click Login	Dashboard loads successfully
4.	Click on PIM and PIM page loads.
5.	Click Add Employee and	Add Employee form loads
6.	Fill First Name and Last Name,	Fields will accept the inputs
7.	Click Save.	Employee will be added successfully
8.	Repeat steps 5–7 for adding 3 employees and	All employees will be added
9.	Navigate to Employee List and	Employee list page will be displayed
10.	Search for added employees and	Names will appear in the list
11.	Logout from Dashboard.
    
**Expected Final Result:**
All added employees are present in Employee List, and user logs out successfully.
