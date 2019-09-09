*** Setting ***
Library  SeleniumLibrary
Library  Tmp.py

*** Test Cases ***
test_name
    # This is testCase
    ${var1}=    anum
    log to console  \n---${var1}---\n

    ${var2}=    alist
    log to console  \n---@{var2}---\n

    ${var3}=    adict
    log to console  \n---${var3}---\n

    :FOR    ${i}    in    @{var2}
    \    log to console  ${i}