# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#!/usr/bin/python
from __future__ import division
from collections import defaultdict
import json


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (Student)):
            return o.__dict__
        else:
			return json.JSONEncoder.encode(self, o)


class Student:
	
	def __init__(self,name,surrname):
		self.name=name
		self.surrname=surrname
		self.scores=defaultdict(list)
		self.attendance=defaultdict(list)
	
	def _avg(self,numbers):
		return 	sum(numbers)/len(numbers)

	def get_total_avarage(self):
		partial_avarages=[]		
		for scoreboard in self.scores.itervalues():
			partial_avarages.append(self._avg(scoreboard))
		return self._avg(partial_avarages)
		
	def get_subject_avarage(self,subject):
		if subject in self.scores:
			return self._avg(self.scores[subject])

	def get_total_attendance(self):
		expected=0
		actual=0		
		for attendance in self.attendance.itervalues():
			expected+=len(attendance)
			actual+=sum(attendance)
		return actual/expected
	
	def get_subject_attendance(self,subject):
		return self._avg(self.attendance[subject])

	def add_score(self,subject,score):
		self.scores[subject].append(score)

	def mark_presence(self,subject):
		self.attendance[subject].append(1)		
	
	def mark_absence(self,subject):
		self.attendance[subject].append(0)


class School:
	def __init__(self):
		self.students={}
	def add_student(self,student):
		self.students[student.name+student.surrname]=student
	def dump_school(self):
		with open("school_dump.json", 'a') as fp:		
			json.dump(self.students, fp, cls=CustomJsonEncoder)
			

