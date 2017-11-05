# -*- coding: utf-8 -*-
import pymysql
import pandas as pd
class tosql():
	def __init__(self,dbname,host='localhost',port=3306,user='root',passwd=''):
		config={
			'host':host,
			'port':port,
			'user':user,
			'passwd':passwd,
			'db':dbname,
			'charset':'utf8'
			}
		self.con=pymysql.Connect(**config)
		self.cs=self.con.cursor()
	def insert(self,data,table):
		col=list(data)
		col_name=','.join(col)
		exists_table=self.table_if_exist(table)
		if exists_table != (0,):self.create_table(table,col)
		for i in range(len(data)):
			value=list(data.iloc[i])
			value_str=list(map(str,value))
			print(type(value_str))
			value_name=','.join("'"+f+"'" for f in value_str)
			for j in range(len(col)):
				if j == 0:key_value=col[j] + '=' "'" + value_str[j] + "'"
				else:key_value += ' and ' + col[j] + '=' "'" + value_str[j] + "'"
			exist_yon=self.value_if_exist(key_value,table)
			if exist_yon != (0,):
				sql = 'insert into {0} ({1}) values ({2});'.format(table,col_name,value_name)
				self.cs.execute(sql)
				self.con.commit()
				print("the data insert into %s successful" %(table))
			else:print("the data is exist in %s" %(table))

	def value_if_exist(self,arr,table):
		sql='select 0 from {0} where {1};'.format(table,arr)
		self.cs.execute(sql)
		self.con.commit()
		data = self.cs.fetchone()
		return data

	def table_if_exist(self,table):
		sql='select 0 from information_schema.tables where table_name="{0}";'.format(table)
		self.cs.execute(sql)
		self.con.commit()
		data = self.cs.fetchone()
		return data
		
	def create_table(self,table,key):
		for i in range(len(key)):
			if i == 0:key_type=key[i] + ' TEXT '
			else:key_type += ',' + key[i] + ' TEXT'
		sql='create table {0} ({1})'.format(table,key_type)
		self.cs.execute(sql)
		self.con.commit()
		print('create table %s sucessful' %(table))
		return self.con.commit()

			
# if __name__=='__main__':
# 	df=pd.DataFrame({'name':['raa','sssa','k'],'sex':['male','male','male'],'age':[1,3,5]})
# 	ts=tosql('wc')
# 	ts.insert(df,'w1')
