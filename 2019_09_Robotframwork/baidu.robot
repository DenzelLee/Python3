*** Setting ***
Library  SeleniumLibrary

*** Test Cases ***
baidu
    # this is test
    [Documentation]  baidu_yixia
    Open Browser                  http://www.baidu.com    chrome
    Set Selenium Implicit Wait    5
    Input Text                    id=kw                   selenium\n
    ${firstRet}=                  Get Text                id=1
    Should Contain                ${firstRet}             selenium

baidu2
    # this is test2
    open browser    http://www.baidu.com    firefox
    Set Selenium Implicit wait    5
    input text    id=kw    selenium2
    click element    id=su
    ${title}    get title
    should contain     ${title}    百度一下，你就知道