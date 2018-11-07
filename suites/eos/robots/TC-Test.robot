*** Settings ***
Documentation    接口测试
Library         RequestsLibrary
Library         suites.eos.resource.source
Variables       suites/eos/resource/source.py


*** Test Cases ***
1.测试githu接口返回值
    Create Session	github  ${domain}
    ${resp} =   Get Request	github  /users/bulkan
    Should Be Equal As Strings  ${resp.status_code}  200

2.测试proxy请求
#    ${proxies}=	Create Dictionary	http=http://acme.com:912	https=http://acme.com:913
    ${proxies} =    Github Param
    Create Session	github	http://api.github.com	proxies=${proxies}
    ${resp}=	Get Request	github	/
    Should Be Equal As Strings	${resp.status_code}	200