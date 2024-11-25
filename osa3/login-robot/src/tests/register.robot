*** Settings ***
Resource  resource.robot
Test Setup  Register Kalle And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  ville123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  d3849328n
    Output Should Contain  User with username kalle already exists 

Register With Too Short Username And Valid Password
    Input Credentials  a  4djj894ur
    Output Should Contain  Username should be at least 3 characters and containing only letters a-z
    Input New Command
    Input Credentials  jl  9fy82hdhsa
    Output Should Contain  Username should be at least 3 characters and containing only letters a-z
    

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  123  dfasvanlk32r3
    Output Should Contain  Username should be at least 3 characters and containing only letters a-z
    Input New Command
    Input Credentials  ABK  djoiwfh092
    Output Should Contain  Username should be at least 3 characters and containing only letters a-z
    Input New Command
    Input Credentials  ab1  fdewf99fjdso
    Output Should Contain  Username should be at least 3 characters and containing only letters a-z
    

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
# ...

*** Keywords ***
Register Kalle And Input New Command
    Create User  kalle  kalle123
    Input New Command
