import smtplib


from_addr = 'stephanieramsay6@gmail.com'
to_addr = 'classiestephy67@yahoo.com'

Subject = 'Sending an email using python'
message = 'Whats up!!'




server = smtplib.SMTP('smtp.gmail.com',587) #error fixed
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_addr, password)

BODY = '\r\n'.join(['To: %s' %to_addr,
        'From: %s' %from_addr,
        'Subject: %s' %Subject,
        '',
        message
        ])
try:
    server.sendmail(from_addr, [to_addr], BODY)
    print 'EMAIL SENT'
except:
    print 'ERROR Sending Email'

server.quit()