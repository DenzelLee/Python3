*** Setting ***
Library         SeleniumLibrary
Library         libPython.pythonApi.Webadmin

*** Test Cases ***
添加课程1
    [Setup]         deleteallcourseWeb
    RUN KEYWORDS    addcourseWeb          语文课    语文描述    1
    ...  AND        listcourseWeb
    ${course}=      listcourseWeb
    log to console  \n${course}\n
    [Teardown]      deleteallcourseWeb

添加课程2
    [Setup]         deleteallcourseWeb
    RUN KEYWORDS    addcourseWeb          数学课    数学描述
    ...  AND        listcourseWeb
    ${course}=      listcourseWeb
    log to console  \n${course}\n
    [Teardown]      deleteallcourseWeb
