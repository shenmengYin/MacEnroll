import requests


with requests.Session() as c:
    url = 'https://epprd.mcmaster.ca/psp/prepprd/?cmd=login'
    TIMEZONEOFFSET = 300
    PTMODE = 'f'
    PTLANGCD = 'ENG'
    PTINSTALLEDLANG = 'ENG'
    USERID = 'yins1'
    PWD = 'Ysm19970325'
    c.get(url)
    login_data = dict(timezoneoffset = TIMEZONEOFFSET, ptmode = PTMODE, ptlangcd = PTLANGCD, ptinstalledlang = PTINSTALLEDLANG, userid = USERID, pwd = PWD)
    c.post(url, data = login_data, headers = {})
    page = c.get('https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL')
    print(page.content)


#print(r.json())