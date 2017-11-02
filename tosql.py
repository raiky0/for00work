# -*- coding: utf-8 -*-
import pymysql
import pandas as pd
class tosql():
	def __init__(self,dbname,host='localhost',port=3306,user='root',passwd=''):
		config={
			'host':host,
			'port':port,
			'user':user,
			'passwd':passwd.decode('latin1'),
			'db':dbname,
			'charset':'utf8'
			}
		self.con=pymysql.Connect(**config)
	def insert(self,data,table):
		col=list(data)
		col_name=','.join(col)
		print col_name
		for i in range(len(data)):
			value=list(data.iloc[i])
			print value
			value_name=','.join(map(str,value)) 
			print value_name
			try:
				with self.con.cursor() as cs:
					sql = 'insert into %s (%s) values (%s);' %(table,col_name,value_name)
			#		sql = 'insert into w1 (age,name,sex) values (20,"ww","ww");'
					opt=table,col_name,value_name
					cs.execute(sql)
					self.con.commit()
			finally:
	#			self.con.close()
				pass

if __name__=='__main__':
	df=pd.DataFrame({'name':['raa','sssa','k'],'sex':['male','male','male'],'age':[1,3,5]})
	ts=tosql('wc')
	ts.insert(df,'w1')
