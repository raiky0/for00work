# for00work
just for search the job from JS|AH|ZJ RSJ（人社局） about teacher in high school
tosql.py:
      dataFrame to mysql through  pymysql
      before I use DataFrame.to_sql , but it need engine of sqlalchemy.create_engine, it depend of mysqldb. 
      But for python 3.6 , dont find the mysqldb for python3.X .so I modify the code of to_sql about pymysql-->mysqldb.
      It has some error and irresistible reasons, so I write tosql to replace DataFrame.to_sql.
      Its function is simple,just work for main.py
      
      function:  check the table exist, and if no create the table, else check the row data exist, if no insert the row data to table.
      
      important: the data to mysql, every sting must add '''',  if not show error ,because of mysql consider some string as one string.
                 it only show in value, key or columns not need.
main.py:
       it is just a web crawler.
       
