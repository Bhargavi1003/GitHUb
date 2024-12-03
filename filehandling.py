import os
filename = "students_data.txt"
#OPEN FILE
fileopen = open(filename,'r')
#READ FILE
# records = fileopen.readlines()
#print records in file
# with open(filename,'r') as file:
#     for record in records:
#         print(record)
#ADD NEW RECORD INTO THE FILE
# with open(filename,'a') as file:
#     id = 6
#     name = "Saurab"
#     age = 26
#     department = "Mechanical"
#     file.write(f"{id},{name},{age},{department}\n")
#     print("student record stored successfully")
#READ FILE AFTER ADDING NEW RECORD
# with open(filename,'r') as file:
#     reading = file.readlines()
#     for record in reading:
#         print(record)
#SEARCHING FOR THE RECORD
# found = False
# id = input("enter student id to  search: ")
# with open(filename,'r') as file:
#     for a in file:
#         stu_id,name,age,dept = a.strip().split(",")
#         if id == stu_id:
#             print(f"Record Found: {stu_id},{name},{age},{dept}")
#             found = True
#             break
# if not found:
#     print("No record found in the file")

#UPDATE THE RECORD
# stu_id = input("enter student id to record: ")
# found = False
# updated_records = []
# with open(filename,'r') as file:
#     for record in file:
#         id,name,age,dept = record.strip().split(',')
#         if stu_id == id:
#             print(f"Current record: {id},{name},{age},{dept}")
#             new_id = input("enter updated id: ")
#             new_name = input("enter updated name: ")
#             new_age = input("enter updated age: ")
#             new_dept = input("enter updated dept: ")
#             updated_records.append(f"{new_id},{new_name},{new_age},{new_dept}")
#             found = True
#             break
#         else:
#             updated_records.append(record)
# if not found:
#     print("record not updated")
# else:
#     with open(filename,'w') as file:
#         file.writelines(updated_records)
#     print("Records updated succesfully")
#READ FILE AFTER  UPDATING
# with open(filename,'r') as file:
#     x = file.readlines()
#     for record in x:
#         print(record)
#DELETE THE RECORD
# stu_id = input("enter student id that you want to delete: ")
# found = False
# updated_records = []
# with open(filename,'r') as file:
#     for record in file:
#         id,name,age,dept = record.strip().split(",")
#         if id==stu_id:
#             print(f"Record found to delete: {id},{name},{age},{dept}")
#             found = True
#         else:
#             updated_records.append(record)
# if not found:
#     print("No record found to delete")
# else:
#     with open(filename,'w') as file:
#         file.writelines(updated_records)
#     print("Record deleted succesfully")
#READ FILE AFTER  DELETING
# with open(filename,'r') as file:
#     x = file.readlines()
#     for record in x:
#         print(record)