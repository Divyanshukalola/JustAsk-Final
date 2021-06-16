from django.db import models
from datetime import datetime
from django import forms

from django.utils.html import strip_tags

import random 
import string 

from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.conf import settings




try:
    from django.conf import settings
    User = settings.AUTH_USER_MODEL
except AttributeError:
    from django.conf import settings
    from django.contrib.auth.models import User



# Create your models here.
class Student(models.Model):

	OT = 'other'
	CS = 'computer science'
	MATH = 'math'
	PSE = 'physical science and engineering'
	AAD = 'arts and designing'
	SS = 'social science'
	HEALTH = 'health'
	DS = 'data science'
	LANG = 'language'
	BUS = 'business'


	TYPE__OF_COR = [
		(OT, 'OT - other'),
        (CS, 'CS - computer science'),
        (MATH, 'MT - math'),
        (PSE, 'PE - physical science and engineering'),
        (AAD, 'AD - arts and designing'),
        (SS, 'SS - social science'),
        (HEALTH, 'HL - health'),
        (DS, 'DS - data science'),
        (LANG, 'LG - language'),
        (BUS, 'BS - business'),

    ]



	Cuser = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
	FirstName = models.CharField("First Name",max_length=200,blank=True, default="")
	SecondName = models.CharField("Second Name",max_length=200, blank=True, default="")
	Email = models.EmailField("Email",max_length=254,default="")
	Studentid = models.CharField("Student ID",max_length=9, default="A20435927", unique=True)
	expert = models.BooleanField("expert?",default=False,blank=True)
	Country = models.CharField("Country(Lowercase)",max_length=200, default="india")
	subs = models.BooleanField("Subscribed?",default=False,blank=True)
	confirm = models.BooleanField("Confirmed?",default=False,blank=True)
	First = models.BooleanField("First Time?",default=True,blank=True)
	anual = models.BooleanField("Yearly?",default=False,blank=True)
	StartDate = models.DateTimeField("Start Date of Subscription",auto_now=False, auto_now_add=False, blank=True, null=True , default=datetime.now())
	EndDate = models.DateTimeField("End Date of Subscription",auto_now=False, auto_now_add=False, blank=True, null=True , default=datetime.now())
	ProfilePicture = models.FileField("File",upload_to='covers/', default='covers/profile.png', max_length=100, blank=True)
	credits = models.IntegerField("Credits Earned",default=0,blank=True)
	testscore = models.IntegerField("Test Score / 100",default=0,blank=True)
	fieldofexpertise = models.CharField("Field of expertise",max_length=255,blank=True)
	qscore = models.IntegerField("Questions yet to ask..",default=0,blank=True)
	quiz = models.BooleanField("quiz given?",default=False,blank=True)
	QuizDate = models.DateTimeField("Date of Last Quiz",auto_now=False, auto_now_add=False, blank=True, null=True , default=datetime.now())
	QuizScoreCard = models.FileField("Score Card",upload_to='ScoreCards/',blank=True, default='', max_length=255)
	#PayPalID = models.CharField("PayPal Subscriber ID",max_length=30, default="",blank=True)
	playlist = models.URLField(max_length=200, default='https://open.spotify.com/embed/playlist/0EEokYI5NzQa0Wfw5BieuS')
	def __str__(self):
		return f"{self.Email} - {self.FirstName}" 


class Document(models.Model):
  file = models.FileField('Document', upload_to='mydocs/')

  @property
  def filename(self):
     name = self.file.name.split("/")[1].replace('_',' ').replace('-',' ')
     return name
  def get_absolute_url(self):
     return reverse('myapp:document-detail', kwargs={'pk': self.pk})


class Question(models.Model):

	def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
		return ''.join(random.choice(chars) for x in range(size))


	OT = 'other'
	CS = 'computer science'
	MATH = 'math'
	PSE = 'physical science and engineering'
	AAD = 'arts and designing'
	SS = 'social science'
	HEALTH = 'health'
	DS = 'data science'
	LANG = 'language'
	BUS = 'business'


	TYPE__OF_COR = [
		(OT, 'OT - other'),
        (CS, 'CS - computer science'),
        (MATH, 'MT - math'),
        (PSE, 'PE - physical science and engineering'),
        (AAD, 'AD - arts and designing'),
        (SS, 'SS - social science'),
        (HEALTH, 'HL - health'),
        (DS, 'DS - data science'),
        (LANG, 'LG - language'),
        (BUS, 'BS - business'),

    ]



	student = models.ForeignKey(Student, on_delete=models.CASCADE,default='')
	question = HTMLField('Question')
	question_field = models.CharField("Question Field",max_length=200,choices=TYPE__OF_COR,default=OT)
	question_cover = models.ImageField("Cover Image",upload_to='covers/', default='', max_length=100,blank=True)
	question_cover2 = models.ImageField("Cover Image 2",upload_to='covers/', default='', max_length=100,blank=True)
	question_cover3 = models.ImageField("Cover Image 3",upload_to='covers/', default='', max_length=100,blank=True)
	question_cover4 = models.ImageField("Cover Image 4",upload_to='covers/', default='', max_length=100,blank=True)
	question_cover5 = models.ImageField("Cover Image 5",upload_to='covers/', default='', max_length=100,blank=True)
	question_cover6 = models.ImageField("Cover Image 6",upload_to='covers/', default='', max_length=100,blank=True)
	question_cover7 = models.ImageField("Cover Image 7",upload_to='covers/', default='', max_length=100,blank=True)
	question_cover8 = models.ImageField("Cover Image 8",upload_to='covers/', default='', max_length=100,blank=True)
	qid = models.CharField("Question ID",max_length=8, default=ran_gen(8, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"), unique=True)
	answered = models.BooleanField("Answered?",default=False)
	def __str__(self):
		return strip_tags(f'{self.question} - {self.qid} ')

	def question_str(self):
		return strip_tags(self.question)


class Feedback(models.Model):

	user = models.CharField("User",max_length=700,blank=True, default="")
	where = models.CharField("From Where?",max_length=2000,default='')
	concern = models.CharField("how?",max_length=2000,default='')
	suggestions = models.CharField("suggestions?",max_length=2000,default='')

	def __str__(self):
		return strip_tags(f'{self.suggestions} - {self.concern}')




class Like(models.Model):
	qid = models.CharField("Question ID",max_length=200,blank=True, default="")
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	
	def __str__(self):
		return f"{self.qid} - {self.student.FirstName}" 


class Searche(models.Model):
	text = models.TextField("search", default='')
	date = models.DateTimeField("Date",auto_now=False, auto_now_add=False, blank=True, null=True , default=datetime.now())
	user = models.CharField("User",max_length=700,blank=True, default="")

	def __str__(self):
		return f"{self.text} - {self.user}" 

class Dislike(models.Model):
	qid = models.CharField("Question ID",max_length=200,blank=True, default="")
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	reason = models.TextField("Reason", default='')
	
	def __str__(self):
		return f"{self.qid} - {self.student.FirstName}" 

class Answer(models.Model):

	answer = models.TextField("Answer", default='', blank=True)
	ans_file = models.FileField("Answer File",upload_to='files/',blank=True, default='', max_length=500)
	ans_file2 = models.FileField("Answer File 2",upload_to='files/',blank=True, default='', max_length=500)
	ans_file3 = models.FileField("Answer File 3",upload_to='files/',blank=True, default='', max_length=500)
	ans_file4 = models.FileField("Answer File 4",upload_to='files/',blank=True, default='', max_length=500)
	ans_file5 = models.FileField("Answer File 5",upload_to='files/',blank=True, default='', max_length=500)
	ans_file6 = models.FileField("Answer File 6",upload_to='files/',blank=True, default='', max_length=500)
	ans_file7 = models.FileField("Answer File 7",upload_to='files/',blank=True, default='', max_length=500)
	ans_file8 = models.FileField("Answer File 8",upload_to='files/',blank=True, default='', max_length=500)
	ans_file9 = models.FileField("Answer File 9",upload_to='files/',blank=True, default='', max_length=500)
	ans_file10 = models.FileField("Answer File 10",upload_to='files/',blank=True, default='', max_length=500)
	ans_file11 = models.FileField("Answer File 11",upload_to='files/',blank=True, default='', max_length=500)
	ans_file12 = models.FileField("Answer File 12",upload_to='files/',blank=True, default='', max_length=500)
	ans_file13 = models.FileField("Answer File 13",upload_to='files/',blank=True, default='', max_length=500)
	ans_file14 = models.FileField("Answer File 14",upload_to='files/',blank=True, default='', max_length=500)
	ans_file15 = models.FileField("Answer File 15",upload_to='files/',blank=True, default='', max_length=500)
	ans_file16 = models.FileField("Answer File 16",upload_to='files/',blank=True, default='', max_length=500)
	ans_file17 = models.FileField("Answer File 17",upload_to='files/',blank=True, default='', max_length=500)
	ans_file18 = models.FileField("Answer File 18",upload_to='files/',blank=True, default='', max_length=500)
	ans_file19 = models.FileField("Answer File 19",upload_to='files/',blank=True, default='', max_length=500)
	ans_file20 = models.FileField("Answer File 20",upload_to='files/',blank=True, default='', max_length=500)
	ans_file21 = models.FileField("Answer File 21",upload_to='files/',blank=True, default='', max_length=500)
	ans_file22 = models.FileField("Answer File 22",upload_to='files/',blank=True, default='', max_length=500)
	ans_file23 = models.FileField("Answer File 23",upload_to='files/',blank=True, default='', max_length=500)
	ans_file24 = models.FileField("Answer File 24",upload_to='files/',blank=True, default='', max_length=500)

	question = models.OneToOneField(Question, on_delete=models.CASCADE,primary_key = True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	likes = models.IntegerField("Likes", default=0)
	dislikes = models.IntegerField("Dislikes", default=0)
	Verify = models.BooleanField("Verified?",default=True)

	def __str__(self):
		return strip_tags(self.answer)


	def answer_(self):
		return strip_tags(self.answer)


	def qid(self):
		return strip_tags(self.question.qid)

class EBook(models.Model):

	OT = 'other'
	CS = 'computer science'
	MATH = 'math'
	PSE = 'physical science and engineering'
	AAD = 'arts and designing'
	SS = 'social science'
	HEALTH = 'health'
	DS = 'data science'
	LANG = 'language'
	BUS = 'business'


	TYPE__OF_COR = [
		(OT, 'OT - other'),
        (CS, 'CS - computer science'),
        (MATH, 'MT - math'),
        (PSE, 'PE - physical science and engineering'),
        (AAD, 'AD - arts and designing'),
        (SS, 'SS - social science'),
        (HEALTH, 'HL - health'),
        (DS, 'DS - data science'),
        (LANG, 'LG - language'),
        (BUS, 'BS - business'),

    ]

	Bcover = models.FileField("Book Cover",upload_to='ebook/', default='', max_length=100, blank=True)
	File_name = models.CharField("Title",max_length=200, default="")
	Edition = models.CharField("Edition",max_length=200, default="1st Edition")
	book_field = models.CharField("Book Field",max_length=200,choices=TYPE__OF_COR,default=OT)
	File = models.FileField("Ebook",upload_to='ebook/', default='', blank=True)
	Auth = models.CharField("Book Author",max_length=200, default="")
	BID = models.CharField("BOOK ID",max_length=200, default="", blank=True)
	Description = HTMLField("Body", default='')
	price = models.IntegerField("Rental Price (USD 8 min)",default=0,blank=True)
	price2 = models.IntegerField("Buy Price (USD 10 min)",default=0,blank=True)
	Email = models.EmailField("Email",max_length=254,default="",blank=True)
	Uploaded = models.BooleanField("Contributed Book?",default=False,blank=True)
	def __str__(self):
		return f"{self.File_name} - {self.book_field}"



class BookSol(models.Model):

	OT = 'other'
	CS = 'computer science'
	MATH = 'math'
	PSE = 'physical science and engineering'
	AAD = 'arts and designing'
	SS = 'social science'
	HEALTH = 'health'
	DS = 'data science'
	LANG = 'language'
	BUS = 'business'


	TYPE__OF_COR = [
		(OT, 'OT - other'),
        (CS, 'CS - computer science'),
        (MATH, 'MT - math'),
        (PSE, 'PE - physical science and engineering'),
        (AAD, 'AD - arts and designing'),
        (SS, 'SS - social science'),
        (HEALTH, 'HL - health'),
        (DS, 'DS - data science'),
        (LANG, 'LG - language'),
        (BUS, 'BS - business'),

    ]

	Ebook = models.OneToOneField(EBook, on_delete=models.CASCADE,primary_key = True)
	Bcover = models.FileField("Book Cover",upload_to='ebook/', default='', max_length=100, blank=True)
	File_name = models.CharField("Title",max_length=200, default="")
	Edition = models.CharField("Edition",max_length=200, default="1st Edition")
	book_field = models.CharField("Book Field",max_length=200,choices=TYPE__OF_COR,default=OT)
	File = models.FileField("Solution(PDF)",upload_to='ebook/', default='', max_length=100, blank=True)
	Auth = models.CharField("Solution Author",max_length=200, default="")
	Description = HTMLField("Body", default='')
	def __str__(self):
		return f"{self.File_name} - {self.book_field}"

class Note(models.Model):

	OT = 'other'
	CS = 'computer science'
	MATH = 'math'
	PSE = 'science and engineering'
	SS = 'social science and history'
	LANG = 'language'
	BUS = 'business'


	TYPE__OF_COR = [
		(OT, 'OT - other'),
        (CS, 'CS - computer science'),
        (MATH, 'MT - math'),
        (PSE, 'SE - science and engineering'),
        (SS, 'SS - social science and history'),
        (LANG, 'LG - language'),
        (BUS, 'BS - business'),

    ]

	File_name = models.CharField("File Name",max_length=200, default="")
	book_field = models.CharField("Notes Field",max_length=200,choices=TYPE__OF_COR,default=OT)
	File = models.FileField("Notes",upload_to='notes/', default='', max_length=100)
	Auth = models.CharField("Notes Author",max_length=200, default="")
	Description = HTMLField("Body", default='')
	price = models.IntegerField("Price",default=0,blank=True)
	Chapter = models.CharField("Section/Chapter Number",max_length=200, default="",blank=True)
	Email = models.EmailField("Email",max_length=254,default="",blank=True)
	Uploaded = models.BooleanField("Contributed Notes?",default=False)

	def __str__(self):
		return f"{self.File_name} - {self.book_field}"

class Paper(models.Model):

	OT = 'other'
	CS = 'computer science'
	MATH = 'math'
	PSE = 'physical science and engineering'
	AAD = 'arts and designing'
	SS = 'social science'
	HEALTH = 'health'
	DS = 'data science'
	LANG = 'language'
	BUS = 'business'


	TYPE__OF_COR = [
		(OT, 'OT - other'),
        (CS, 'CS - computer science'),
        (MATH, 'MT - math'),
        (PSE, 'PE - physical science and engineering'),
        (AAD, 'AD - arts and designing'),
        (SS, 'SS - social science'),
        (HEALTH, 'HL - health'),
        (DS, 'DS - data science'),
        (LANG, 'LG - language'),
        (BUS, 'BS - business'),

    ]

	File_name = models.CharField("File Name",max_length=200, default="")
	book_field = models.CharField("Paper's Field",max_length=200,choices=TYPE__OF_COR,default=OT)
	File = models.FileField("Paper",upload_to='notes/', default='', max_length=100, blank=True)
	Date = models.DateTimeField("Date Of Paper",auto_now=False, auto_now_add=False, blank=True, null=True , default=datetime.now())
	Description = models.TextField("Body", default='')
	def __str__(self):
		return f"{self.File_name} - {self.book_field}"



class BuyBook(models.Model):
	book = models.ForeignKey(EBook, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	duration = models.BooleanField("Permanent?",default=False,blank=True)
	StartDate = models.DateTimeField("Start Date Rental book",auto_now=False, auto_now_add=False, blank=True, null=True , default=datetime.now())
	EndDate = models.DateTimeField("End Date of Rental book",auto_now=False, auto_now_add=False, blank=True, null=True , default=datetime.now())
	rental = models.BooleanField("Book rental?",default=False,blank=True)
	
	def __str__(self):
		return f"{self.book} - {self.student.FirstName}" 

class BookRequest(models.Model):
	Description = models.TextField("Body", default='')
	def __str__(self):
		return self.Description

class Refer(models.Model):
	student = models.ForeignKey(Student, on_delete=models.DO_NOTHING,default='')
	referedby = models.CharField("Refer ID",max_length=200,default='')
	madeon = models.DateTimeField(auto_now_add=True)
	credits = models.IntegerField()

	def __str__(self):
		return f"{self.student} - {self.referedby}" 

class CreditTransaction(models.Model):
	student = models.ForeignKey(Student, on_delete=models.DO_NOTHING,default='')
	madeon = models.DateTimeField(auto_now_add=True)
	credits = models.IntegerField()
	orderid = models.CharField(unique=True, max_length=100, null=True, blank=True)
	checksum = models.CharField(max_length=100, null=True, blank=True)
	applied = models.BooleanField("applied?",default=False,blank=True)

	
	def __str__(self):
		return f"{self.student} - {self.orderid}" 

class BookTransaction(models.Model):
	book = models.ForeignKey(EBook, on_delete=models.DO_NOTHING,default='')
	student = models.ForeignKey(Student, on_delete=models.DO_NOTHING,default='')
	duration = models.BooleanField("Permanent?",default=False,blank=True)

	madeon = models.DateTimeField(auto_now_add=True)
	amount = models.FloatField()
	orderid = models.CharField(unique=True, max_length=100, null=True, blank=True)
	checksum = models.CharField(max_length=100, null=True, blank=True)
	applied = models.BooleanField("applied?",default=False,blank=True)

	
	def __str__(self):
		return f"{self.student} - {self.orderid}" 


class SubsTransaction(models.Model):
	student = models.ForeignKey(Student, on_delete=models.DO_NOTHING,default='')

	madeon = models.DateTimeField(auto_now_add=True)
	amount = models.FloatField()
	orderid = models.CharField(unique=True, max_length=100, null=True, blank=True)
	checksum = models.CharField(max_length=100, null=True, blank=True)
	applied = models.BooleanField("applied?",default=False,blank=True)

	
	def __str__(self):
		return f"{self.student} - {self.orderid}" 

class Message(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField("Email",max_length=254,default="")
	subject = models.CharField(max_length=200, null=True, blank=True)
	message = models.TextField('message')

	def __str__(self):
		return f"{self.email} - {self.subject}" 


class Text(models.Model):
	text = models.TextField('text')


class Choice(models.Model):
	question = models.ForeignKey('QuizeQuestion',on_delete=models.CASCADE,default='')
	choice = models.TextField('choice')
	is_answer = models.BooleanField(default=False) # or True.
	answer_cover = models.ImageField("Answer Image",upload_to='quizquestion_choice/', default='', max_length=255,blank=True)

	def __str__(self):
		return f"{self.choice}"

class QuizeQuestion(models.Model):


	CHEM = 'chemistry'
	CS = 'computer science'
	MATH = 'math'
	PHY = 'physics'
	ECON = 'economics'



	TYPE__OF_COR = [	
		(CHEM, 'CHEM - chemistry'),
        (CS, 'CS - computer science'),
        (MATH, 'MT - math'),
        (PHY, 'PHY - Physics'),
        (ECON, 'ECON - Economics'),
        

    ]

	question = models.TextField('Question')
	question_field = models.CharField("Question Field",max_length=200,choices=TYPE__OF_COR,default=MATH)
	question_cover = models.ImageField("Cover Image",upload_to='quizquestion/', default='', max_length=200,blank=True)
	style = models.BooleanField('List Style',default=False)
	
	def check_answer(self, choice):
	    return self.choice_set.filter(id=choice.id, is_answer=True).exists()

	def get_answers(self):
	    return self.choice_set.filter(is_answer=True)

	def __str__(self):
		return f"{self.question} - {self.question_field}" 

class Comments(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE,default='')
	ans = models.ForeignKey(Answer, on_delete=models.CASCADE,default='')
	text = models.TextField('text')

	def __str__(self):
		return f"{self.student.Email} - {self.text}" 
 

# class BookTransaction(models.Model):
# 	made_by = models.ForeignKey(Student, related_name='transactions',on_delete=models.CASCADE, default='')
# 	Book = models.ForeignKey(EBook, related_name='BookBuy',on_delete=models.CASCADE,default='')
# 	duration = models.BooleanField("Permanent?",default=False,blank=True)

# 	made_on = models.DateTimeField(auto_now_add=True)
# 	amount = models.IntegerField()
# 	order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
# 	checksum = models.CharField(max_length=100, null=True, blank=True)

# 	def __str__(self):
# 		return f"{self.made_by} - {self.order_id}"



User = settings.AUTH_USER_MODEL

# Model to store the list of logged in users
class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user',on_delete=models.DO_NOTHING)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username
