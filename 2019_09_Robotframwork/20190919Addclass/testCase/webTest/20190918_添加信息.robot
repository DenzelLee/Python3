*** Setting ***
Library            SeleniumLibrary
Library            /2019_目录添加培训班/libPython/pythonApi.Webadmin
*** Test Cases ***
test_name
    # This is testCase
    ${w}=   set variable  Webadmin()
    setupWeb()
    loginWeb()
    addcourseWeb()
    listcourseWeb()
    deleteallcourseWeb()