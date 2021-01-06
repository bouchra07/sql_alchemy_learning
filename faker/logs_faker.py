#faker.py
from faker import Faker
from helpers import *
import csv

fake = Faker()
tablename='logs'
filename = 'log_file.csv'

with open('log_file.csv', mode='w') as log_file:
    log_writer = csv.writer(log_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for _ in range(50000):
        date=fake.date_between(start_date='-0d', end_date='now')
        time=fake.time(pattern='%H:%M:%S', end_datetime=None)
        code1=fake.bothify(text='???#-C#',letters='ABCDEFJHIJKLMNOPQRSTUVWXYZ')
        code2=fake.pyint(min_value=50, max_value=1000, step=1)
        ip_address=fake.ipv4()
        url_identifier=fake.pystr()
        method=fake.http_method()
        user_agents=fake.user_agent()
        content_type=fake.mime_type(category='application')
        image_path=fake.file_path(depth=5, category='image')
        hostname=fake.hostname(levels=1)
        hostname2=fake.hostname(levels=1)
        port_number=fake.pyint(min_value=50, max_value=1000, step=1)
        http_version=fake.word(ext_word_list=['HTTP/2.0', 'HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/1.1 bis'])
        time_response1=fake.pyfloat(left_digits=0,positive=True)
        time_response2=fake.pyfloat(left_digits=0,positive=True)
        tls_versions=fake.word(ext_word_list=['TLSv1.0', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3'])
        cypher_suite=fake.word(ext_word_list=['TLS_RSA_EXPORT1024_WITH_DES_CBC_SHA' ,'TLS_RSA_WITH_AES_256_GCM_SHA384','TLS_DHE_RSA_WITH_AES_256_GCM_SHA384' ,'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384' ,'TLS_AES_256_GCM_SHA384', 'TLS_PSK_WITH_AES_128_CBC_SHA256'])
        log_type=fake.word(ext_word_list=['Hit', 'Error'])
        protocol=fake.word(ext_word_list=['http', 'https'])
        status=fake.word(ext_word_list=['101', '102', '103', '200','201','202','203','204','205','206','207','300','301','302','303','304','305','306','307','308','400','401','402','403','404','405','406','407','408','409','410'])
        v_number=fake.pystr_format(string_format='?=###{{random_int}}{{random_letter}}', letters='v')
        url1=fake.url()
        amp_connector=fake.bothify(text='#####.0')
        log_writer.writerow([date, time, code1, code2, ip_address, method, hostname, image_path, status, url1,
                  user_agents, v_number, log_type,
                  url_identifier, hostname2, protocol, port_number, time_response1,
                  tls_versions, cypher_suite, http_version, amp_connector,
                  time_response2, content_type])


df = log_import(filename)
df = preprocess(df)
implement_to_postgres(tablename, df)







