*** Setting ***
Library  SeleniumLibrary

*** Test Cases ***
百度一下1
    # This is testCase
    open browser    http://www.baidu.com    chrome
    set selenium implicit wait  10
    input text      id=kw    selenium
    click element   id=su
    ${eles}=       get webelements  css=#container #content_left div h3>a
    :FOR    ${ele}     IN              @{eles}
       \               log to console  ${ele}
       \               log to console  ${ele.text}
       \               run keyword if  '${ele.text}'=='selenium_百度翻译'     log to console   yes!
       \               should be equal  '${ele.text}'  'selenium_百度翻译1'    notequeal报错提示：

百度一下2
    # this is test
    [Documentation]  baidu_yixia
    Open Browser                  http://www.baidu.com    chrome
    Set Selenium Implicit Wait    5
    Input Text                    id=kw                   selenium\n
    ${firstRet}=                  Get Text                id=1
    Should Contain                ${firstRet}             selenium

百度一下3
    # this is test2
    open browser    http://www.baidu.com    firefox
    Set Selenium Implicit wait    5
    input text    id=kw    selenium2
    click element    id=su
    ${title}    get title
    should contain     ${title}    百度一下，你就知道