# This is the demo project to use sql and database connection
# to work please install mysql-connector pip install mysql-connector
import mysql.connector as connector
import time

class DBHelper:

  def __init__(self):
    self.con = connector.connect(host='',
                                 user='',
                                 password='',
                                 database='')
    query = 'create table if not exists user(userID int AUTO_INCREMENT,username varchar(200),phone varchar(12),primary key(userID))'
    cur = self.con.cursor()
    cur.execute(query)
    print("created!!")

  #insert
  def insert_user(self, username, phone):
    query = "insert into user(username,phone) values('{}','{}')".format(
      username, phone)
    cur = self.con.cursor()
    cur.execute(query)
    self.con.commit(
    )  #This here helps the query to change the items in the table
    print("USer saved!!")

  #Fetch All of the data from the database
  def fetch_all(self):
    query = "select * from user"
    cur = self.con.cursor()
    cur.execute(query)
    for i in cur:
      print("User ID:", i[0])
      print("User Name:", i[1])
      print("User Phone:", i[2])
      print("\n")

  # Deleting from table
  def delete_user(self, id):
    query = f"delete * from user where userID={id}"
    print(query)
    cur = self.con.cursor()
    cur.execute(query)
    self.con.commit()
    print(f"Removed user with id {id} sucessfully")
    print("\n")
    
  def searchli(self,serach):
      query=f"select * from `user` where username like '%{search}%'"
      cur = self.con.cursor()
      cur.execute(query)
      print(f"Search results for {search}")
      for i in cur:
          print("ID:",i[0])
          print("Name:",i[1])
          print("Phone:",i[2])
          print()
          
      
    # Searching for pericular user 
  def particular(self,userid):
      query="SELECT * FROM `user` where userID={}".format(userid)
      cur = self.con.cursor()
      cur.execute(query)
      for i in cur:
        name=i[1]
        phone=i[2]
      return name,phone
    
  def advanced(self,ad):
    # making this so that only the working query gets executed
    try:
      query=ad
      cur=self.con.cursor()
      cur.execute(query)
      for i in cur:
        print(i)
    except:
      print("Could not process the query you have entered\n")
        
  #updating the user
  def update_user(self,userid,new_name,new_phone):
      f_name,f_phone=helper.particular(userid)
      if new_name=="":
        new_name=f_name
      if new_phone=="":
        new_phone=f_phone
      query=f"update user set username='{new_name}',phone='{new_phone}' where userID={userid}"
      cur = self.con.cursor()
      cur.execute(query)
      self.con.commit()
      print(f"The user with {userid} from Name {f_name} to {new_name} and Phone {f_phone} to {new_phone}")
      
      
      
helper = DBHelper()
while True:
    case=int(input("Select from the following\n 1. Insert\n 2. Delete\n 3. Show All\n 4. Update\n 5. Search in DB\n 6. Advanced\n 7. Exit\n"))
    if case==1:
        name=input("Enter the name\n")
        phone=input("Enter the phone number\n ")
        if name!="" and phone!="":
           helper.insert_user(name,phone)
        else:
          print("Name and phone cannot be empty")
    elif case==2:
        delete=int(input("Enter the id to be deleted\n"))
        helper.delete_user(delete)
    elif case==3:
        helper.fetch_all()
    elif case==4:
        id=int(input("Enter the id of the user to be changed\n"))
        new_name=input("Enter the name\n")
        new_phone=input("Enter the phone number\n")
        if id!="":
            helper.update_user(id,new_name,new_phone)
        else:
            print("ID cannot be empty")
    elif case==5:
        search=input("Enter the Nam e\n")
        helper.searchli(search)
    elif case==6:
      pas=input("Enter password to continue\n")
      if pas=="1234":
        ad=input("Enter the query\n")
        helper.advanced(ad)
      else:
        print("Wrong password enterd going back to main menu in 2 seconds!!")
        time.sleep(2)
        continue
    else:
        exit()
