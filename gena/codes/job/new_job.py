import pymysql
import subprocess
import os
conn = pymysql.connect(autocommit ='True', host='localhost', user='hogking', password='',db='HUBMED', charset='utf8') 
curs = conn.cursor(pymysql.cursors.DictCursor)
query = "SELECT * FROM JOB where PMID_COLLECT =0"
curs.execute(query)
row = curs.fetchone()

if row is not None:
	j_id = str(row['J_ID'])
	if not os.path.exists("/home/hogking/hubmed/backend/files/"+j_id+"/"):
		os.makedirs("/home/hogking/hubmed/backend/files/"+j_id+"/")
	python_call ="nohup python "
	main_dir = " /home/hogking/hubmed/backend/codes/pmid/get_pmid.py "
	std_out = " > /home/hogking/hubmed/backend/files/"+j_id+"/get_pmid_log.out "
	command = ""
	command += python_call
	command += main_dir
	command += j_id
	command += std_out
	print (command)
	query = "UPDATE JOB SET PMID_COLLECT =1 WHERE J_ID = (%s)"
	curs.execute(query,j_id)
	subprocess.call(command,shell=True)
