#!/usr/bin/env python3

# Define Dictionary
info_Dict = {}
student = {}

#Create Dictionary with four keys and values
for any in range(0,3):
        id = input('Enter Student I.D.: ')
#Populate the dictionary with student's information using input()
        info_Dict['Name'] = input('Name: ')
        info_Dict['Age'] = input('Age: ')
        info_Dict['Gender'] = input('Gender: ')
        info_Dict['Phone Number'] = input('Phone Number: ')
#Add (info_Dict) to another dictionary (Student) whose keys are student's I.D.  
        student['ID00'+id]=(info_Dict)
#Empty Dictionary of students (info_Dict) so we can add new entry on next loop - temp variable
        info_Dict={}

print(student)
