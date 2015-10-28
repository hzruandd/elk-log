#encoding=utf8
#wget  http://s.qdcdn.com/17mon/17monipdb.zip
#unzip  17monipdb.zip

import re,sys,os,csv,smtplib
from ipip import IP
from ipip import IPX
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from optparse import OptionParser
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

nginx_log_path="/app/nginx/logs/apptest_www.access.log"
pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
def stat_ip_views(log_path):
    ret={}
    f = open(log_path, "r")
    for line in f:
        match = pattern.match(line)
        if match:
            ip=match.group(0)
            if ip in ret:
                views=ret[ip]
            else:
                views=0
            views=views+1
            ret[ip]=views
    return ret

def run():
    ip_views=stat_ip_views(nginx_log_path)
    max_ip_view={}
    fileName='out.csv'
    f=open('out.csv','w+')
    b = 'IP,国家,访问数总数'
    print >> f,b
    for ip in ip_views:
        IP.load(os.path.abspath("17monipdb.dat"))
        count=IP.find("%s"% (ip))
        conut_s=count.split()
        countery=conut_s[0]
        views=ip_views[ip]
        c = '%s,%s,%s' %(ip,countery,views)
        print >> f,c
        if len(max_ip_view)==0:
            max_ip_view[ip]=views
        else:
            _ip=max_ip_view.keys()[0]
            _views=max_ip_view[_ip]
            if views>_views:
                max_ip_view[ip]=views
                max_ip_view.pop(_ip)
        print "IP:", ip, "国家:", countery, "访问数:", views

    print "总共有多少IP:", len(ip_views)
    print "最大访问IP数:", max_ip_view
    g = ""
    d = '总共有多少IP:%s' %(len(ip_views))
    e = '最大访问IP数:%s' %(max_ip_view)
    print >> f,g
    print >> f,d
    print >> f,e

def sendMail(html,emailaddress,mailSubject,from_address="other@test.com"):
        mail_list=emailaddress.split(",")
        msg=MIMEMultipart()
        msg['Accept-Language']='zh-CN'
        msg['Accept-Charset']= 'ISO-8859-1,utf-8'
        msg['From']=from_address
        msg['to']=";".join(mail_list)
        msg['Subject']=mailSubject.decode("utf-8")
        txt=MIMEText(html,'html','utf-8')
        txt.set_charset('utf-8')
        msg.attach(txt)
        file=MIMEBase('application', 'octet-stream')
        file.set_payload(open(fileName, 'rb').read())
        encoders.encode_base64(file)
        file.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(fileName))
        msg.attach(file)
        smtp=smtplib.SMTP("mail.test.com")
        smtp.sendmail(msg["From"],mail_list,msg.as_string())
        smtp.close()

if __name__ == '__main__':
    run()
    fileName='out.csv'
    cmd = 'iconv -f UTF8 -t GB18030 %s -o %s.bak && mv %s.bak %s' %(fileName,fileName,fileName,fileName)
    os.system(cmd)
    Content= 'Dear ALL: <br> &nbsp;&nbsp; 附件内国家IP访问数据分析统计，请查收！  <br> &nbsp;&nbsp; 如有任何问题，请及时与我联系！'
    Subject = '[分析]国家创建数据IP分析统计'
    sendMail(html=Content,emailaddress='kuangl@test.com',mailSubject=Subject)
