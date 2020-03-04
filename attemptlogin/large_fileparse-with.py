#!/usr/bin/env python3

#parse keyston.common.wsgi and return number of failed login attempts

loginfail = 0
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 

print("The number of failed log in attempts is ", loginfail)




