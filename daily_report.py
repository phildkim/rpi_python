#!/usr/bin/python
import os
import csv
import time
from smtp_service import Mailer
from mariadb_service import Mariadb
from thread_service import ThreadCount


def create_mariadb():
    try:
        db = Mariadb()
        db.execute("CREATE TABLE IF NOT EXISTS temperature_tbl"
                "(id INT(20) NOT NULL AUTO_INCREMENT," 
                "degree VARCHAR(8)," 
                "date VARCHAR(24)," 
                "PRIMARY KEY(id));")
        print "\t\tCREATE TABLE"
    except:
        pass
    return

def remove_mariadb():
    cmd = 'rm ' + os.path.abspath('daily_reports/report-*')
    os.system(cmd)
    try:
        db = Mariadb()
        db.execute('DROP TABLE temperature_tbl;')
        print "\t\tDROP TABLE"
    except:
        pass
    return

def csv_filename():
    return os.path.abspath('daily_reports/report-' + str(time.strftime('%d')) + '.csv')

def write_csv_file():
    db = Mariadb()
    query = db.query('SELECT * FROM temperature_tbl;')
    csv_file = open(csv_filename(), 'a')
    csv_attachment = csv.writer(csv_file)
    csv_attachment.writerows(query)
    csv_file.close()
    return

def query_to_html(list_2d):
    html_table=u'<table align="center" border="1" bordercolor=00000 cellspacing="0" cellpadding="1" style="table-layout:fixed;vertical-align:bottom;font-size:15px;font-family:verdana,sans-serif;border-collapse:collapse;border:1px solid rgb(130,130,130)" >'
    list_2d[0] = [u'<b>' + i + u'</b>' for i in list_2d[0]]
    for row in list_2d:
        html_row = u'<tr>'
        html_row += u'<td align="left" style="padding:1px 4px">'+unicode(row[0])+u'</td>'
        row.remove(row[0])
        html_row = html_row + ''.join([u'<td align="left" style="padding:1px 4px">'+unicode(x)+u'</td>'for x in row])
        html_row += '</tr>'
        html_table += html_row
    html_table += '</table>'
    return html_table

def html_db_table(sql):
    db = Mariadb()
    return query_to_html(db.get_rows(sql))

def send_email():
    mailer = Mailer()
    html_table = str(html_db_table('SELECT * FROM temperature_tbl;'))
    mailer.send_report(str(time.strftime('%m/%d/%Y')), str(time.ctime()), html_table, 'DAILY REPORT', csv_filename())
    return


def main():
    write_csv_file()
    send_email()
    remove_mariadb()
    create_mariadb()
    return

if __name__ == '__main__':
    main()
