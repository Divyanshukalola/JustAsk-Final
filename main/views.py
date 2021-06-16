from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

from . models import Student,Question,Answer,EBook,Note,Paper,Like,Dislike,BuyBook,BookSol,BookRequest,Document,BookTransaction,SubsTransaction,Message,Text,Comments
from . models import CreditTransaction,QuizeQuestion,Choice,Searche,Refer,Feedback
import numpy as np
import re

from django.urls import reverse

from django.contrib.auth.models import User
from django.core.paginator import Paginator


import re

from django.utils.html import strip_tags


import random 
import string 
from gingerit.gingerit import GingerIt
import nltk.data
from nltk import sent_tokenize

from . import Checksum
from .Checksum import verify_checksum
from django.views.decorators.csrf import csrf_exempt
from .utils import VerifyPaytmResponse
from JUSTASK import settings
import requests
from datetime import datetime
from datetime import timedelta , timezone
from django.conf import settings 
from django.core.mail import send_mail 

from django.contrib import auth
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
import Levenshtein as lev
import csv
import codecs
import numpy as np
import pandas as pd
from paypal.standard.forms import PayPalPaymentsForm


def unanswered(request):
	ques = []

	for q in Question.objects.all():
		if q.answered == False:
			ques.append(q)



	paginator = Paginator(ques,6)

	page2 = request.GET.get('page')

	ques = paginator.get_page(page2)

	data={
		'questions':ques,
	}

	return render(request, 'main/unanswered.html',data)


def qsearch_request(request):
	bad_chars = [';', ':', '!', "*",")","(","{","}","[","]"]
	qu = []
	ques = []

	
	search_r = re.sub(' +', ' ',request.GET.get('search')).rstrip().lstrip()

	for i in bad_chars :
		search_r = search_r.replace(i, '')

	if (search_r == ''):
		return redirect("main:homepage")
	else:

		
		
		for qd in Question.objects.all():
			if qd.answered == False:
				cleantext = strip_tags(qd.question)
				match = lev.ratio(search_r,cleantext)
				cord = (qd,match*100)
				qu.append(cord)

				if len(qu) == 100:
					break

		sortlist = Sort_Tuple(qu)


		for s in range(len(sortlist)):
			ques.append(sortlist[s][0])



		paginator = Paginator(ques,6)

		page = request.GET.get('page')

		ques = paginator.get_page(page)


	data={
		'question':strip_tags(search_r),
		'questions':ques,
	}


	return render(request,"main/unanswered.html",data)
	

def expert_apply(request):
	# if request.user.student.quiz == True:
	# 	return redirect('main:profile')
	return render(request, 'main/expert_apply.html')
	# return redirect("main:profile")


def feedback(request):
	where = request.POST.get('where')
	sug = request.POST.get('suggestions')
	how = request.POST.get('how')
	user = request.user.student

	fd = Feedback(concern=how,suggestions=sug,where=where,user=user)
	fd.save()

	return redirect('main:homepage')


def quiz(request):
	email = request.POST.get('email')
	field = request.POST.get('field')
	field2 = request.POST.get('field2')
	qlistf1=[]
	qlistf2=[]

	if email == '':
		return redirect('main:expert_apply')

	if field == 'economics/commerce':
		field == 'economics'

	if field2 == 'economics/commerce':
		field2 == 'economics'


	for q in QuizeQuestion.objects.order_by('?'):

		if q.question_field == field:
			if(len(qlistf1) == 20):
				break
			qlistf1.append(q)

		if q.question_field == field2:
			if(len(qlistf2) == 20):
				break
			qlistf2.append(q)

		else:
			pass

	# print('fields here')
	# print(field,field2)

	for x in qlistf2:
		#print(x)
		qlistf1.append(x)


	random.shuffle(qlistf1)
	#print(Choice.objects.all())
	data={

		'field1':field2,
		'questions':qlistf1,
		'choice':Choice.objects.order_by('?'),
		'field3':field,
	}

	request.user.student.quiz = True
	request.user.student.save(update_fields=['quiz'])
	return render(request, 'main/quiz.html',data)

def QuizCheck(request):

	if request.user.is_anonymous != True:

		field = request.POST.get('field')
		field2 = request.POST.get('field2')
		#print(field,field2)
		#print('----------')
		choice = []
		result = []
		score = 0

		for q in QuizeQuestion.objects.all():

			if q.question_field == field or q.question_field == field2:
				# print(request.POST.get(f'{q.id}'))
				# print('-------------')
				choice.append(request.POST.get(f'{q.id}'))
				#print(request.POST.get(f'{q.id}'))
			else:
				pass

		#print(choice)

		for c in choice:
			#print('==============')
			#print(c)
			for i in Choice.objects.all():
				if c == str(i.id):
					result.append((strip_tags(i.question),i.choice,i.is_answer))
					#print(i.is_answer)
					if i.is_answer:
						score = score + 1
						# print("score : ",score)
						break

		dataframe = pd.DataFrame(result,columns=['Question','Choice','Answer'])
		dataframe.to_csv(f"/home/JustAsk/media/ScoreCards/{request.user.student.Studentid}.csv")

		#print(int((score/len(choice))*100))
		request.user.student.QuizScoreCard = f"./media/ScoreCards/{request.user.student.Studentid}.csv"    #/home/JustAsk/media/ScoreCards
		request.user.student.testscore = int((score/len(choice))*100)
		request.user.student.fieldofexpertise = f'{field}, {field2}'
		request.user.student.QuizDate = datetime.now()
		request.user.student.save(update_fields=['fieldofexpertise','testscore','QuizScoreCard','QuizDate'])

		if request.user.student.testscore > 70:
			print("--------Expert--------")
			request.user.student.expert = True
			request.user.student.save(update_fields=['expert'])

	else:
		return redirect('main:login')

	return redirect('main:profile')

	
def TYDONATE(request):
	return render(request, 'main/thankyou.html')
	
def CSV(request):
	return render(request, 'main/csv.html')

def csvImport(request):
	file = request.FILES['csv']

	df = pd.read_csv(file)
	lenght = len(df)
	print('===================')
	logic = False
	for i in range(lenght):
		fn = df._get_value(i, 'File_name')
		a = df._get_value(i, 'Auth')
		des = df._get_value(i, 'Description')
		file = df._get_value(i, 'File')
		bf = df._get_value(i, 'book_field')
		up = df._get_value(i, 'Bcover')
		Edition = df._get_value(i, 'Edition')
		bid = df._get_value(i, 'BID')

		book = EBook(Bcover=up,File_name=fn,Edition=Edition,book_field=bf,File=file,Email='support@just-ask.in',Auth=a,BID=bid,Description=des,Uploaded=False)
		book.save()
		


	return render(request, 'main/csv.html')



def checkbook(request): # check if the rented book is expired or not
	try:
		user = auth.get_user(request)
		if user.is_anonymous == False:
			print(request.user)
			students = Student.objects.all()
			for student in students:
				if (student.Email == request.user.email):
					
					if student.subs == True and student.First != True:
						if numOfDays(datetime.now(timezone.utc), student.EndDate) <= 0:
							student.subs = False
							student.save(update_fields=['subs'])
					else:
						pass

					for bb in student.buybook_set.all():
						if bb.rental == True:
							if numOfDays(datetime.now(timezone.utc), bb.EndDate) <= 0:
								book = bb
								book.delete()
						else:
							pass
		else:
			return redirect('main:login')
						
		
	except:
		pass

# def ReferFriend(request):
# 	Studentid = request.POST.get('studid')

# 	students = Student.objects.all()
# 	for student in students:
# 		if (student.Email == request.user.email):

#     return redirect("main:profile")

def RedeemCredts(request):
	creditVal = 0.1 #hours/credit
	user = auth.get_user(request)
	if user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				hours_added = timedelta(hours = (creditVal*student.credits))
				student.EndDate = student.EndDate + hours_added
				student.credits = 0
				student.save(update_fields=['EndDate','credits'])

	else:
		return redirect("main:login")
	return redirect("main:profile")

def sub_ceck(request):
	try:
		user = auth.get_user(request)
		if user.is_anonymous == False:
			print(request.user)
			students = Student.objects.all()
			for student in students:
				if (student.Email == request.user.email):
					if student.subs == True:
						if student.credits >= 2000:
							student.credits = 2000
							student.save(update_fields=['credits'])
						if numOfDays(datetime.now(timezone.utc), student.EndDate) <= 0:
							student.subs = False
							student.qscore = 0
							student.save(update_fields=['subs','qscore'])
							messages.error(request, f"Your Subscription has ended. Renew to continue using other features!")
							messages.error(request, f"Subscribe Anually and pay for 10 months instead of 12.")
						if numOfDays(student.QuizDate, datetime.now(timezone.utc)) >= 365:
							student.expert = False
							student.quiz = False
							student.save(update_fields=['expert','quiz'])
							messages.error(request, f"Your Subscription has ended. Renew to continue using other features!")
							messages.error(request, f"Subscribe Anually and pay for 10 months instead of 12.")
					else:
						pass
							
		else:
			pass
	except:
		pass

def game(request): # main home page it will check if the subscription is ended or not
	return render(request,"main/game.html")



def homepage(request): # main home page it will check if the subscription is ended or not
	sub_ceck(request)
	checkbook(request)
	stud = 'Empty'
	try:
		user = auth.get_user(request)
		if user.is_anonymous == False:
			print(request.user)
			students = Student.objects.all()
			for student in students:
				if (student.Email == request.user.email):
					stud = student
					if student.subs != True and student.First == True:
						messages.error(request, f"First Time User? Try our Special Offer* for Free! Limited time only.")
					else:
						pass

					data={
					'stud':stud,
					'books':EBook.objects.all().count(),
					'notes':Note.objects.all().count(),
					'questions':Question.objects.all().count(),
					}
					return render(request,"main/home.html",data)
		else:
			pass
			#messages.error(request, f"Register now and get Free Subscription for 1 month!")
	except:
		pass
		#messages.error(request, f"Register now and get Free Subscription for 1 month!")


	data={
	'stud':stud,
	'books':EBook.objects.all().count(),
	'notes':Note.objects.all().count(),
	'questions':Question.objects.all().count(),
	}
	return render(request,"main/home.html",data)



# def home(request): # main home page it will check if the subscription is ended or not
# 	sub_ceck(request)
# 	checkbook(request)
# 	stud = 'Empty'
# 	try:
# 		user = auth.get_user(request)
# 		if user.is_anonymous == False:
# 			print(request.user)
# 			students = Student.objects.all()
# 			for student in students:
# 				if (student.Email == request.user.email):
# 					stud = student
# 					if student.subs != True and student.First == True:
# 						messages.error(request, f"First Time User? Try our Special Offer* for Free! Limited time only.")
# 					else:
# 						pass

# 					data={
# 					'stud':stud,
# 					'books':EBook.objects.all().count(),
# 					'notes':Note.objects.all().count(),
# 					'questions':Question.objects.all().count(),
# 					}
# 					return render(request,"main/home.html",data)
# 		else:
# 			messages.error(request, f"Register now and get Free Subscription for 1 months now!")
# 	except:
# 		messages.error(request, f"Register now and get Free Subscription for 1 months now!")


# 	data={
# 	'stud':stud,
# 	'books':EBook.objects.all().count(),
# 	'notes':Note.objects.all().count(),
# 	'questions':Question.objects.all().count(),
# 	}
# 	return render(request,"main/home.html",data)


def Cancel(request):

	user = auth.get_user(request)
	if user.is_anonymous == False:
		print(request.user)
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				student.subs = False
				student.anual = False
				student.confirm = False
				student.StartDate = datetime.now(timezone.utc)
				student.EndDate = datetime.now(timezone.utc)
				student.save(update_fields=['subs','StartDate','EndDate','anual','confirm'])
				messages.error(request, f"Your Subscription has been Canceled.")			
	else:
		return redirect("main:login")
	return redirect("https://www.paypal.com/cgi-bin/webscr?cmd=_subscr-find&alias=DEVGBPZQWD3UY")


def QNA(request):
	sub_ceck(request)
	return render(request=request,	
				  template_name="main/Q&A.html")

def terms(request):
	sub_ceck(request)
	return render(request=request,	
				  template_name="main/terms.html")

def contrib(request):
	sub_ceck(request)
	return render(request=request,	
				  template_name="main/contribute.html")


def notes(request):
	sub_ceck(request)
	return render(request=request,	
				  template_name="main/notes_field.html")

def customer_service(request):
	sub_ceck(request)
	return render(request,"main/customer_service.html")


def note_contrib(request):
	user = auth.get_user(request)
	if user.is_anonymous == False:
		print(request.user)
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				student.credits = subject.credits + 100
				student.save(update_fields=['credits'])
	else:
		return redirect("main:login")

	auth = request.POST.get('auth')
	title = request.POST.get('title')
	email = request.POST.get('email')
	description = request.POST.get('foo')
	file = request.FILES['file']
	field = request.POST.get('field')
	note = Note(File_name=title,book_field=field,File=file,Auth=auth,Description=description,Email=email,Uploaded=True)
	note.save()

	subject = 'Thank you for contributing to Just Ask'
	text_content = f''
	html_content = f'''
	<p style='font-size:20px'>Hello {auth}, <br>Thank you for contributing in Just Ask! <br>Your submission helps us provide better solution to students like you.<br></p>
	<p style='font-size:20px'><b>You are contributing the following notes:</b></p>
	<hr>

	<p><b>Title: </b>{timedeltatle}</p>
	<p><b>Author: </b>{auth}</p>
	<p><b>Field: </b>{field}</p>
	<p><b>Description: </b>{description}</p>
	<p><b>File Name: </b>{file}</p>
	<hr>
	'''
	email_from = settings.EMAIL_HOST_USER 
	recipient_list = [email,email_from, ] 

	msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
	msg.attach_alternative(html_content, "text/html")
	msg.send()

	messages.success(request, f"Your Book '{title}' is added Successfully")

	return render(request,"main/contribute.html")

def book_contrib(request):
	auth = request.POST.get('auth')
	title = request.POST.get('title')
	email = request.POST.get('email')
	name = request.POST.get('name')
	edition = request.POST.get('edition')
	field = request.POST.get('field')
	ISBN = request.POST.get('isbn')
	description = request.POST.get('foo1')
	file = request.FILES['file']
	cover = request.FILES['file2']

	book = EBook(Bcover=cover,File_name=title,Edition=edition,book_field=field,File=file,Auth=auth,BID=ISBN,Description=description,Email=email,Uploaded=True)
	book.save()


	subject = 'Thank you for contributing to Just Ask'
	text_content = f''
	html_content = f'''
	<p style='font-size:20px'>Hello {auth}, <br>Thank you for contributing to Just Ask! <br>Your submission helps us provide better solution to students like you.<br></p>
	<p style='font-size:20px'><b>You are contributing the following book:</b></p>
	<hr>

	<p><b>Title: </b>{title}</p>
	<p><b>Author: </b>{auth}</p>
	<p><b>Edition: </b>{edition}</p>
	<p><b>ISBN: </b>{ISBN}</p>
	<p><b>Field: </b>{field}</p>
	<p><b>Description: </b>{description|safe}</p>
	<p><b>File Name: </b>{file}</p>
	<hr>
	'''
	email_from = settings.EMAIL_HOST_USER 
	recipient_list = [email, email_from,] 

	msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	messages.success(request, f"Your Book '{title}' is added Successfully")

	return render(request,"main/contribute.html")



def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
		return ''.join(random.choice(chars) for x in range(size))

def questionpost(request):
	name = request.POST.get('auth')
	email = request.POST.get('email')
	
	field = request.POST.get('field')
	
	question = request.POST.get('question')
	
	qid = ran_gen(8, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")



	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				if student.qscore != 0:
					student.qscore = student.qscore - 1
					student.save(update_fields=['qscore'])
					ques = Question(student=student,question=question,question_field=field,qid=qid)
					ques.save()

					try:
						file = request.FILES['file-1']
						ques.question_cover = file
						ques.save(update_fields=['question_cover'])
					except:
						raise Http404("No File Attached")
					
				else:
					return redirect("main:question_p")

	else:
		return redirect("main:login") 



	subject = 'Question Added - Just Ask'
	text_content = f''
	html_content = f'''
	
	<p style='font-size:20px'><b>Question Information: </b></p>
	<hr>
	
	<p><b>Question: </b>{question} USD</p>
	<p><b>QID: </b>{qid}</p>
	<p><b>Date: </b>{datetime.now()}</p>
	<p><b>Student: </b>{request.user.email} {request.user.student.Studentid}</p>

	<hr>
	<p style='font-size:15px'>Fore more information please email us on <b>support@just-ask.in</b></p>
	'''
	email_from = settings.EMAIL_HOST_USER 
	recipient_list = ['support@just-ask.in', ]

	msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	messages.success(request, f"Your question is added Successfully")

	return render(request,"main/question_p.html")

def inquire(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	sub = request.POST.get('subject')
	message = request.POST.get('message')

	ms = Message(name = name,email=email,subject=sub,message=message)
	messages.success(request, f"Your Message Recieved")
	ms.save()


	return redirect("main:customer_service")

def profile(request):
	sub_ceck(request)
	data={
		'student':'',
		'book': 'False',
		'Student': ''
	}
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				if len(student.buybook_set.all()) != 0:
					data={
					'student':student,
					'book': student.buybook_set.all(),
					'Student': student,
					'diff': numOfDays(datetime.now(timezone.utc), student.EndDate),
					'questions':student.question_set.all(),
					'count':len(student.question_set.all()),
					'transactions':student.substransaction_set.all()
					}
				else:
					data={
					'student':student,
					'book': 'False',
					'Student': student,
					'diff': numOfDays(datetime.now(timezone.utc), student.EndDate),
					'questions':student.question_set.all(),
					'count':len(student.question_set.all()),
					'transactions':student.substransaction_set.all()
					}
	else:
		return redirect("main:login")
				


	return render(request,"main/profile.html",data)




def rates(request):
	sub_ceck(request)
	data={}
	if request.user.is_authenticated:
		for stud in Student.objects.all():
			if stud.Email == request.user.email:

				host = request.get_host()

				# if subscription_plan == '1-month':
				#     price = "7"
				#     billing_cycle = 1
				#     billing_cycle_unit = "M"
				# else:
				#     price = "70"
				#     billing_cycle = 1
				#     billing_cycle_unit = "Y"

				pricem = "7.99"
				billing_cyclem = 1
				billing_cycle_unitm = "M"


				paypal_dictm  = {
					"cmd": "_xclick-subscriptions",
					'business': 'DEVGBPZQWD3UY',
					"a3": pricem,  # monthly price
					"p3": billing_cyclem,  # duration of each unit (depends on unit)
					"t3": billing_cycle_unitm,  # duration unit ("M for Month")
					"src": "1",  # make payments recur
					"sra": "1",  # reattempt payment on payment error
					"no_note": "1",  # remove extra notes (optional)
					'item_name': 'Monthly Subscription',
					'custom': 1,     # custom data, pass something meaningful here
					'currency_code': 'USD',
					'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
					'return_url': 'http://{}{}'.format(host,reverse('main:paypalcallbackmonth')),
					'cancel_return': 'http://{}{}'.format(host,reverse('main:profile')),
					'payer': request.user,
					'custom':request.user.student.Studentid,
				}

				pricey = "79.99"
				billing_cycley = 1
				billing_cycle_unity = "Y"


				paypal_dicty  = {
					"cmd": "_xclick-subscriptions",
					'business': 'DEVGBPZQWD3UY',
					"a3": pricey,  # monthly price
					"p3": billing_cycley,  # duration of each unit (depends on unit)
					"t3": billing_cycle_unity,  # duration unit ("M for Month")
					"src": "1",  # make payments recur
					"sra": "1",  # reattempt payment on payment error
					"no_note": "1",  # remove extra notes (optional)
					'item_name': 'Yearly Subscription',
					'custom': 1,     # custom data, pass something meaningful here
					'currency_code': 'USD',
					'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
					'return_url': 'http://{}{}'.format(host,reverse('main:paypalcallbackyear')),
					'cancel_return': 'http://{}{}'.format(host,reverse('main:profile')),
					'payer': request.user,
					'custom':request.user.student.Studentid,
				}

				formm = PayPalPaymentsForm(initial=paypal_dictm, button_type="subscribe")
				formy = PayPalPaymentsForm(initial=paypal_dicty, button_type="subscribe")
				data={
				'stud':stud,
				'formm':formm,
				'formy':formy,
				}
	else:
		pass


	return render(request,"main/rates.html",data)


def already_sub(request):
	students = Student.objects.all()
	if requests.user.is_authenticated:
		for student in students:
			if (student.Email == request.user.email):
				data={
					'student':student,
					'diff': numOfDays(datetime.now(timezone.utc), student.EndDate)
				}
	else:
		return redirect("main:login")

	return render(request, 'main/already_subs.html',data)


def register(request):

	def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
		return ''.join(random.choice(chars) for x in range(size))

	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			print('---------------------in----------------')
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			register = True
			emails = []
			for stud in Student.objects.all():
				emails.append(stud.Email)

			for e in emails:
				if e == email:
					register = False


			
			if register:
				messages.success(request, f"Account Created for {username}")
				print('------------------')
				stid = ran_gen(9, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz")
				user = form.save()
				student = Student(Cuser=user,FirstName=username,Email=form.cleaned_data.get('email'),Studentid=stid,credits=200,qscore=20,PayPalID=stid)
				student.save()
				data={
				'student':username,
				}
				
				subject = 'Welcome to Just Ask'
				text_content = f''
				html_content = render_to_string('registration/email_test.html',data)
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [email, ] 

				msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
				msg.attach_alternative(html_content, "text/html")
				msg.send()


				subject = 'User Registered - Just Ask'
				text_content = f''
				html_content = f'''
				<p style='font-size:20px'>User Added, <br>This is an email notification for user registration.<br></p>
				<p style='font-size:20px'><b>User Information: </b></p>
				<hr>
				<p><b>Username: </b>{username}</p>
				<p><b>Email: </b>{email}</p>
				<p><b>Student ID: </b>{stid}</p>
				<hr>
				
				'''
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = ['support@just-ask.in', ] 

				msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				login(request, user)
				return redirect("main:homepage")
			else:
				messages.error(request, f"{email} is already registered")
				pass
		else:
			messages.error(request, f"Please Check You Password and Username if they have correct formate.")

	form = NewUserForm()
	return render(request,"main/register.html",context={"form":form})


def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
	return ''.join(random.choice(chars) for x in range(size))

def logout_request(request):
	logout(request)
	messages.info(request, "Logged Out Successfully")
	return redirect("main:homepage")

def login_request(request):

	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			
			if user is not None:
				login(request, user)
				messages.success(request, f"You are logged in as {username}")
				return redirect("main:homepage")
			else:	
				messages.error(request, "Invalid username or password")
		else:	
				messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,"main/login.html",{"form":form})


def Sort_Tuple(tup):  
  
    # reverse = None (Sorts in Ascending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used  
    tup.sort(reverse = True,key = lambda x: x[1])  
    return tup 

def search_request(request):
	sub_ceck(request)
	bad_chars = [';',")","(","{","}","++"]
	qu = []
	qlist = []
	books = []
	qlist2 = []
	
	search_r = re.sub(' ', ' ',request.GET.get('search')).rstrip().lstrip()
	
	change = False
	for i in bad_chars :
		if i == "++": # ++ is not a good character while displaying the string in Django brings up error.
			search_r = search_r.replace(i, 'pp')
			change = True
		else:
			search_r = search_r.replace(i, '')

	search_question = search_r


	if change: 
		search_r = search_r.replace("pp", '++')
	
	if (search_r == ''):
		return redirect("main:homepage")
	else:

		if(search_r.lower() == 'grammar' or search_r.lower() == 'writing' or search_r.lower() == 'grammar check'):
			return redirect("main:writing")
		else:
			pass

		add = True
		for x in Searche.objects.all():
			if x.text == search_r:
				add = False

		if add:
			sr = Searche(text=search_r,user=request.user)
			sr.save()

		if search_r == "CHIRAGJHALA2301":
			refer = True
			if request.user.is_authenticated:
				for r in request.user.student.refer_set.all():
					if r.referedby == "CHIRAGJHALA2301":
						refer = False
			if request.user.is_authenticated:
				if refer:
					refer = Refer(student=request.user.student,referedby="CHIRAGJHALA2301",credits=0)
					refer.save()
					request.user.student.subs = True
					request.user.student.qscore = 10
					request.user.student.StartDate = datetime.now()
					request.user.student.EndDate = datetime.now() + timedelta(days=31)
					order_id = ran_gen(6, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz")
					bill_amount = "0"
					transaction = SubsTransaction.objects.create(student=request.user.student,orderid=order_id, amount=bill_amount)
					transaction.save()

					try:
						subject = 'Payment Successfull - Just Ask'
						text_content = f''
						html_content = f'''
						<p style='font-size:20px'>Hello {request.user.student.FirstName}, <br>This is to confirm that we have recieved your payment.<br></p>
						<p style='font-size:20px'><b>Your Payment Information: </b></p>
						<hr>
						

						<p><b>Amount: </b>{bill_amount} USD</p>
						<p><b>Name of payer: </b>{request.user.student.FirstName} {request.user.student.SecondName}</p>
						<p><b>Order ID: </b>{order_id}</p>
						<p><b>Customer ID: </b>{request.user.student.Studentid}</p>
						<p><b>Subscription Plan: </b>Monthly</p>

						
						<hr>
						<p style='font-size:15px'>Fore more information please email us on <b>support@just-ask.in</b></p>
						'''
						email_from = settings.EMAIL_HOST_USER 
						recipient_list = [request.user.student.Email,email_from, ] 

						msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
						msg.attach_alternative(html_content, "text/html")
						msg.send()
					except:
						pass
					
					request.user.student.save(update_fields=['StartDate','EndDate','subs','confirm','First','qscore'])
					return redirect("main:profile")
				else:
					messages.error(request, "Referal code alreay used!")
					return redirect("main:homepage")
			else:
				return redirect("main:login")

		
		for qd in Question.objects.all(): # need new algorithm for better performance
			cleantext = strip_tags(qd.question) 
			match = lev.ratio(search_r,cleantext)
			cord = (qd,match*100)
			qu.append(cord)


		sortlist = Sort_Tuple(qu)


		for s in range(len(sortlist)):
			qlist.append(sortlist[s][0])
		
			# for y in search_r.split():
			# 	if re.search(y.lower(), sortlist[s][0].question.lower()):
					
					
			# 		break
			# 	else:
			# 		pass


		

		for book in Note.objects.all():

			match1 = lev.ratio(search_r,book.File_name) #Title
			match2 = lev.ratio(search_r,book.Description) #ISBN
			match3 = lev.ratio(search_r,book.Auth) #Author

			match = maximum(match1, match2, match3)

			cord = (book,match*100)
			books.append(cord)
			if len(books) == 100:
				break

		sortlist2 = Sort_Tuple(books)
		
		
		for s in range(len(sortlist2)):
			qlist2.append(sortlist2[s][0])

			# for y in search_r.split():
			# 	if re.search(y.lower(), sortlist2[s][0].File_name.lower()):
					
			# 		break
			# 	else:
			# 		pass


		
			
		paginator2 = Paginator(qlist2,6)

		page2 = request.GET.get('page2')

		qlist2 = paginator2.get_page(page2)



		paginator = Paginator(qlist,10)

		page = request.GET.get('page')

		qlist = paginator.get_page(page)

	context = {
	'question':search_question,
	'qs':qlist,
	'qs2':qlist2,
	}


	return render(request,"main/questions.html",context)
	

	# print(search_r)
	# questions = Question.objects.all()
	# for q in questions:
	# 	match = levenshtein_ratio_and_distance(search_r,q.question,True)
	# 	if(match*100 > 50):
	# 		pass


def answer_request(request):
	sub_ceck(request)
	search_r = request.GET.get('question')
	print("------------------")
	

	As = ''
	searchq = ''
	Stud = ''
	cnt = 0
	ques = Question.objects.all()

	context = {
		'questions':'' ,
		'student':'',
		'count':'',
		'question': '',
		'qs':'',
		'liked':"",
		'User':'',
		}

	for q in ques:
		if (q.qid == search_r):
			searchq = q.question

			try:
				As = q
				Stud = q.answer.student
				cnt = Stud.answer_set.count()
			except:
				As = q
				Stud = 'False'
				cnt = 0
			
	

	qu = []
	qlist = []

	for qd in Question.objects.all():
		clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
		cleantext = re.sub(clean, '', qd.question)		
		
		match = lev.ratio(searchq,cleantext)
		# print('-----------')
		# print(search_r)
		# print(match*100)
		# print(cleantext)
		cord = (qd,match*100)
		qu.append(cord)

		sortlist = Sort_Tuple(qu)
		#print('-----------')
		
	for s in range(len(sortlist)):
		if(s == 3):
			break
		qlist.append(sortlist[s][0])
	print('------------------------------------------------')
	print(request.user)
	user = auth.get_user(request)

	if user.is_anonymous == False:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				likes = True
				for l in student.like_set.all():
					if l.qid == search_r:
						likes = False

				for l in student.dislike_set.all():
					if l.qid == search_r:
						likes = False

				
				
				try:
					context = {
						'questions': As,
						'student':Stud,
						'count':cnt,
						'question': search_r,
						'qs':qlist,
						'liked':likes,
						'User':student,
						'comments':As.answer.comments_set.all(),
						}
				except:
					context = {
						'questions': As,
						'student':Stud,	
						'count':cnt,
						'question': search_r,
						'qs':qlist,
						'liked':likes,
						'User':student,
						'comments':False,
						}
				return render(request,"main/answer.html",context)

	else:
		pass

	context = {
	'questions': As,
	'student':Stud,
	'count':cnt,
	'question': search_r,
	'qs':qlist,
	'liked':"None",
	'User':'',
	'comments':'',
	}

	
	return render(request,"main/answer.html",context)

def comment(request):
	search_r = request.POST.get('question')
	comment = request.POST.get('comment')
	print("------------------")



	
	As = ''
	searchq = ''
	Stud = ''
	cnt = 0
	ques = Question.objects.all()

	context = {
		'questions':'' ,
		'student':'',
		'count':'',
		'question': '',
		'qs':'',
		'liked':"",
		'User':'',
		}

	for q in ques:
		if (q.qid == search_r):
			searchq = q.question

			try:
				Ansques = q
				Stud = q.answer.student
				cnt = Stud.answer_set.count()
			except:
				Ansques = q
				Stud = 'False'
				cnt = 0
			
	

	qu = []
	qlist = []

	for qd in Question.objects.all():
		clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
		cleantext = re.sub(clean, '', qd.question)		
		
		match = lev.ratio(searchq,cleantext)
		# print('-----------')
		# print(search_r)
		# print(match*100)
		# print(cleantext)
		cord = (qd,match*100)
		qu.append(cord)

		sortlist = Sort_Tuple(qu)
		#print('-----------')
		
	for s in range(len(sortlist)):
		if(s == 3):
			break
		qlist.append(sortlist[s][0])
	print('------------------------------------------------')
	print(request.user)
	user = auth.get_user(request)

	if user.is_anonymous == False:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				cmt = Comments(student=student,ans=Ansques.answer,text=comment)
				cmt.save()
				context = {
					'questions': Ansques,
					'student':Stud,
					'count':cnt,
					'question': search_r,
					'qs':qlist,
					'liked':"None",
					'User':student,
					'comments':Ansques.answer.comments_set.all(),
					}
				return render(request,"main/answer.html",context)

	context = {
	'questions': Ansques,
	'student':Stud,
	'count':cnt,
	'question': search_r,
	'qs':qlist,
	'liked':"None",
	'User':'',
	'comments':'',
	}

	
	return render(request,"main/answer.html",context)
	

def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
		return ''.join(random.choice(chars) for x in range(size))

def question_p(request):
	return render(request,"main/question_p.html")

def question_post(request):
	search_r = request.GET.get('question')
	data={
		'question':search_r,
	}

	return render(request,"main/question_p.html",data)


def answer_post(request):
	# file1 = request.FILES['file1']
	# file2 = request.FILES['file2']
	# file3 = request.FILES['file3']
	# file4 = request.FILES['file4']
	# file5 = request.FILES['file5']
	# file6 = request.FILES['file6']
	# file7 = request.FILES['file7']
	# file8 = request.FILES['file8']
	# file9 = request.FILES['file9']
	# file10 = request.FILES['file10']

	search_r = request.POST.get('ans')
	search_r2 = request.POST.get('qid')

	if search_r == '':
		search_r = f'Answered'
	print('================')
	# print(file)
	print(search_r)
	print(search_r2)
	print('================')

	question = ''


	for q in Question.objects.all():
		if(q.qid == search_r2):
			question = q
			
			if q.student.credits != 2000:
				q.student.credits = q.student.credits + 20
				q.student.save(update_fields=['credits'])


	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				if student.subs:
					ans = Answer(answer=search_r,question=question, student=student)
					ans.save()
					question.answered = True
					question.save(update_fields=['answered'])

					if (student.Studentid != question.student.Studentid and student.credits != 2000):
						student.credits = student.credits + 20
						student.save(update_fields=['credits'])
					else:
						pass

					try:
						ans.ans_file = request.FILES['file1']
					except:
						ans.ans_file = ''

					try:
						ans.ans_file2 = request.FILES['file2']
					except:
						ans.ans_file2 = ''
					try:
						ans.ans_file3 = request.FILES['file3']
					except:
						ans.ans_file3 = ''
					try:
						ans.ans_file4 = request.FILES['file4']
					except:
						ans.ans_file4 = ''
					try:
						ans.ans_file5 = request.FILES['file5']
					except:
						ans.ans_file5 = ''
					try:
						ans.ans_file6 = request.FILES['file6']
					except:
						ans.ans_file6 = ''
					try:
						ans.ans_file7 = request.FILES['file7']
					except:
						ans.ans_file7 = ''
					try:
						ans.ans_file8 = request.FILES['file8']
					except:
						ans.ans_file8 = ''
					try:
						ans.ans_file9 = request.FILES['file9']
					except:
						ans.ans_file9 = ''
					try:
						ans.ans_file10 = request.FILES['file10']
					except:
						ans.ans_file10 = ''
					
					ans.save(update_fields=['ans_file','ans_file2','ans_file3','ans_file4','ans_file5','ans_file6','ans_file7','ans_file8','ans_file9','ans_file10'])

	
	else:
		pass

# student.ProfilePicture = file
			
# 			student.save(update_fields=['ProfilePicture'])

	

	return redirect('main:QNA')


def like_question(request):
	search_r = request.GET.get('qid')
	print("---------like_request---------")
	print(search_r)
	

	As = ''
	Stud = ''
	searchq = ''
	cnt = 0
	ques = Question.objects.all()

	for q in ques:
		if (q.qid == search_r):
			searchq = q.question
			try:
				print("---------try---------")
				As = q
				Stud = q.answer.student
				cnt = Stud.answer_set.count()
				matchlike = True

				
				for li in Stud.like_set.all():
					if (li.qid == search_r):
						matchlike = False

						

				if matchlike:
					# if(Stud.dislike_set.get(qid=search_r).exists() == False):
					print('-----------------liked----------------')
					q.answer.likes = q.answer.likes+1
					q.answer.save(update_fields=['likes'])
					like = Like(qid = search_r,student=Stud)
					like.save()
					

			except:
				As = q
				Stud = 'False'
				cnt = 0

	context = {
		'questions':'' ,
		'student':'',
		'count':'',
		'question': '',
		'qs':'',
		'liked':"",
		'User':'',
		}

	for q in ques:
		if (q.qid == search_r):
			searchq = q.question

			try:
				As = q
				Stud = q.answer.student
				cnt = Stud.answer_set.count()
			except:
				As = q
				Stud = 'False'
				cnt = 0
			
	

	qu = []
	qlist = []

	for qd in Question.objects.all():
		clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
		cleantext = re.sub(clean, '', qd.question)		
		
		match = lev.ratio(searchq,cleantext)
		# print('-----------')
		# print(search_r)
		# print(match*100)
		# print(cleantext)
		cord = (qd,match*100)
		qu.append(cord)

		sortlist = Sort_Tuple(qu)
		#print('-----------')
		
	for s in range(len(sortlist)):
		if(s == 3):
			break
		qlist.append(sortlist[s][0])
	print('------------------------------------------------')
	print(request.user)
	user = auth.get_user(request)

	if user.is_anonymous == False:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				likes = 'Likes'
				
				try:
					context = {
						'questions': As,
						'student':Stud,
						'count':cnt,
						'question': search_r,
						'qs':qlist,
						'liked':likes,
						'User':student,
						'comments':As.answer.comments_set.all(),
						}
				except:
					context = {
						'questions': As,
						'student':Stud,	
						'count':cnt,
						'question': search_r,
						'qs':qlist,
						'liked':likes,
						'User':student,
						'comments':False,
						}
				return render(request,"main/answer.html",context)

	else:
		pass

	context = {
	'questions': As,
	'student':Stud,
	'count':cnt,
	'question': search_r,
	'qs':qlist,
	'liked':"None",
	'User':'',
	'comments':'',
	}

	
	return render(request,"main/answer.html",context)
			
	
	


def dislike_question(request):
	search_r = request.GET.get('qid')
	search_r1 = request.GET.get('reason')
	search_r2 = request.GET.get('Additional')
	print("---------like_request---------")
	print(search_r)
	
	reason = str(search_r1) + str(search_r2)

	As = ''
	Stud = ''
	searchq = ''
	cnt = 0
	ques = Question.objects.all()

	for q in ques:
		if (q.qid == search_r):
			searchq = q.question
			try:
				print("---------try---------")
				As = q
				Stud = q.answer.student
				cnt = Stud.answer_set.count()
				matchlike = True

				
				for li in Stud.dislike_set.all():
					if (li.qid == search_r):
						matchlike = False

						

				if matchlike:
					print('-----------------disliked----------------')
					q.answer.dislikes = q.answer.dislikes+1
					q.answer.save(update_fields=['dislikes'])
					like = Dislike(qid = search_r,student=Stud,reason=reason)
					like.save()
					

			except:
				As = q
				Stud = 'False'
				cnt = 0
			
	

	qu = []
	qlist = []

	for qd in Question.objects.all():
		clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
		cleantext = re.sub(clean, '', qd.question)		
		
		match = lev.ratio(searchq,cleantext)
		# print('-----------')
		# print(search_r)
		# print(match*100)
		# print(cleantext)
		cord = (qd,match*100)
		qu.append(cord)

		sortlist = Sort_Tuple(qu)
		#print('-----------')
		
	for s in range(len(sortlist)):
		if(s == 3):
			break
		qlist.append(sortlist[s][0])
	print('------------------------------------------------')
	print(request.user)
	user = auth.get_user(request)

	if user.is_anonymous == False:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				likes = 'Likes'
				
				try:
					context = {
						'questions': As,
						'student':Stud,
						'count':cnt,
						'question': search_r,
						'qs':qlist,
						'liked':likes,
						'User':student,
						'comments':As.answer.comments_set.all(),
						}
				except:
					context = {
						'questions': As,
						'student':Stud,	
						'count':cnt,
						'question': search_r,
						'qs':qlist,
						'liked':likes,
						'User':student,
						'comments':False,
						}
				return render(request,"main/answer.html",context)

	else:
		pass

	context = {
	'questions': As,
	'student':Stud,
	'count':cnt,
	'question': search_r,
	'qs':qlist,
	'liked':"None",
	'User':'',
	'comments':'',
	}

	
	return render(request,"main/answer.html",context)



def books(request):
	sub_ceck(request)
	checkbook(request)
	book = {
				'book': 'False',
				'Student': ''
			}

	
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				if len(student.buybook_set.all()) != 0:
					book = {
						'book': student.buybook_set.all(),
						'Student': student
					}
				else:
					book = {
						'book': 'False',
						'Student': student
					}
	else:
		pass

	return render(request,"main/book.html",book)



def maximum(a, b, c): 
  
    if (a >= b) and (a >= c): 
        largest = a 
  
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
          
    return largest 
  
def booksearch_request(request):
	sub_ceck(request)
	checkbook(request)
	books = []
	qlist = []

	search_r = re.sub(' +', ' ',request.GET.get('search')).rstrip().lstrip()
	if (search_r == ''):
		return redirect("main:books")
	else:
		for book in EBook.objects.all():
			
			match1 = lev.ratio(search_r,book.File_name) #Title
			match2 = lev.ratio(search_r,book.BID) #ISBN
			match3 = lev.ratio(search_r,book.Auth) #Author

			match = maximum(match1, match2, match3)

			print(match*100)
			cord = (book,match*100)
			books.append(cord)

		sortlist = Sort_Tuple(books)
		
		
		for s in range(len(sortlist)):
			qlist.append(sortlist[s][0])
			# print('-----------')
			# print(sortlist[s][1])
			# print(sortlist[s][0].File_name)

			# for y in search_r.split():

			# 	if re.search(y.lower(), sortlist[s][0].File_name.lower()) or re.search(y.lower(), sortlist[s][0].BID.lower()) or re.search(y.lower(), sortlist[s][0].Auth.lower()):
					
			# 		break
			# 	else:
			# 		pass
			


		paginator = Paginator(qlist,8)

		page = request.GET.get('page')

		qlist = paginator.get_page(page)

		q = {
		'question': search_r,
		'qs':qlist,
		}
	return render(request,"main/book_search.html",q)



book_buy = ''
def bookbuy_request(request):
	sub_ceck(request)
	checkbook(request)
	print("HI")
	search_r = request.GET.get('bid')
	print(search_r)
	q = {
		'book': '',
		
		}

	books = EBook.objects.all()
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				for b in student.buybook_set.all():
					if b.book.BID == search_r:
						q = {
							'book': b.book,
							'stud':student,
							}
						
						return render(request,"main/bookbuy_view.html",q)

	for book in books:
		if(book.BID == search_r):
			print('---------------------')
			book_buy = book
			q = {
			'book': book,
			}
			break
	
	return render(request,"main/book_buy.html",q)

def bookview_request(request):
	sub_ceck(request)
	checkbook(request)
	search_r = request.GET.get('bid')
	print(search_r)
	q = {
		'book': '',
		
		}

	books = EBook.objects.all()
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				if student.subs:
					for book in books:
						if(book.BID == search_r):
							print('---------------------')
							q = {
							'book': book,
							'stud':student,
							}
							break
				else:
					q = {
						'book': '',
						'stud':False,
						}
					
	return render(request,"main/book_view.html",q)


def bookbuyview_request(request):
	sub_ceck(request)
	checkbook(request)
	search_r = request.GET.get('bid')
	print(search_r)
	q = {
		'book': '',
		
		}

	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				for book in student.buybook_set.all():
					if(book.book.BID == search_r):
						print('---------------------')
						q = {
						'book': book.book,
						'stud':student,
						}
						return render(request,"main/bookbuy_view.html",q)
	return redirect("main:books")
				
	




def booksoltuion_request(request):
	sub_ceck(request)
	return render(request,"main/book_solution.html")


def solution(request):

	book = {
		'book': '',
		'Student': '',
	}

	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				if student.subs:
					book = {
						'book': student.buybook_set.all(),
						'Student': student
					}
	else:
		pass

	
	
	return render(request,"main/solution.html",book)







def booksolsearch_request(request):
	books = []
	qlist = []

	search_r = re.sub(' +', ' ',request.GET.get('search')).rstrip().lstrip()
	empty = (search_r == '')
	if empty:
		return redirect("main:solution")
	else:
		for book in BookSol.objects.all():
			
			match1 = lev.ratio(search_r,book.File_name) #Title
			match3 = lev.ratio(search_r,book.Auth) #Author

			match = maximum(match1, 0, match3)

			print(match*100)
			cord = (book,match*100)
			books.append(cord)

		sortlist = Sort_Tuple(books)
		
		
		for s in range(len(sortlist)):
			print('-----------')
			print(sortlist[s][1])
			print(sortlist[s][0].File_name)

			for y in search_r.split():
				if re.search(y.lower(), sortlist[s][0].File_name.lower()) or re.search(y.lower(), sortlist[s][0].Auth.lower()):
					qlist.append(sortlist[s][0])
					break
				else:
					pass
			


		paginator = Paginator(qlist,6)

		page = request.GET.get('page')

		qlist = paginator.get_page(page)

		q = {
		'question': search_r,
		'qs':qlist,
		}
	return render(request,"main/booksol_search.html",q)



def booksoltuion_view(request):
	search_r = request.GET.get('bid')
	print('---------------')
	print(search_r)
	print('---------------')
	q = {
		'book': '',
		
		}

	books = EBook.objects.all()
	user = auth.get_user(request)

	if user.is_anonymous == False:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				if student.subs:
					for book in books:
						if(book.BID == search_r):
							print('---------------------')
							q = {
							'book': book.booksol,
							}
							break
	
	return render(request,"main/book_solution.html",q)




def bookaddition_request(request):
	search_r = request.GET.get('question')
	print('================')
	print(search_r)
	print('================')
	book = {
		'book': '',
		'Student': ''
	}

	if search_r != None:
		br = BookRequest(Description=search_r)
		br.save()

	else:
		pass


	if request.user.is_authenticated:
			students = Student.objects.all()
			for student in students:
				if (student.Email == request.user.email) :
					if student.subs:
						book = {
							'book': student.buybook_set.all(),
							'Student': student
						}
	else:
		pass
	return render(request,"main/book.html",book)

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"


def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences




def writing(request):
	search_r = request.POST.get('question')

	error = []
	edits = [{
		'orignal':False,
		'suggestion':'',
		'error':'',
		'correct':'',
		'definition':''
	}]

	writing = {
			'text': search_r,
			'edits':'',
			'edittedT':''
		
		}
	
	save = True
	try:
		slist = split_into_sentences(search_r)
		editT = search_r
		for t in Text.objects.all():
			if t.text == search_r:
					save = False


		if save:
			txt = Text(text=search_r)
			txt.save()

		for s in slist:
			parser = GingerIt()
			error.append(parser.parse(s))



		for e in error:
			r = e

			 # orignal text
			print(r['result']) # edited text
			try:
				edits.append({
					'orignal':r['text'],
					'suggestion':r['result'],
					'error':r['corrections'][0]['text'],
					'correct':r['corrections'][0]['correct'],
					'definition':r['corrections'][0]['definition']
					})
				editText = r['corrections'][0]['correct']
				orignal = r['corrections'][0]['text']
				editT = editT.replace(orignal,f"<span id='{orignal}'>{orignal}</span>")
				print(r['corrections'][0]['text']) # wrong text
				print(r['corrections'][0]['correct']) # correct text
				print(r['corrections'][0]['definition']) # definition of the word
			except:
				pass
			print('------------------------------------')
		writing = {
			'text': search_r,
			'edits':edits,
			'edittedT':editT
		
		}
		print('--------------------------')
		print(editT)
		print('--------------------------')
		return render(request,"main/writing.html",writing)
	except:
		pass
		

	return render(request,"main/writing.html",writing)



def finish(request):
	applied = True
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				
				bookcol = student.buybook_set.all()
				trans = student.booktransaction_set.all()

				for t in trans:
					if t.applied == False:
						if t.duration:
							bb = BuyBook(book=t.book,student=student,duration=t.duration)
						else:
							bb = BuyBook(book=t.book,student=student,duration=t.duration, StartDate=datetime.now(),EndDate=datetime.now() + timedelta(days=122),rental=True)
						t.applied = True
						t.save(update_fields=['applied'])
						bb.save()

	return redirect("main:books")


def payment(request):
	search_r = request.GET.get('book')
	books = EBook.objects.all()
	btb = ''

	for b in books:
		if b.BID == search_r:
			btb = b
			if b.price == 0:
				q = {
				'book': b,
				}
				return render(request,"main/book_view.html",q)
			else:
				pass
		else:
			pass
	
	
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				trans = student.booktransaction_set.all()

				#check if trying to buy book two times.
				for bb in student.buybook_set.all():
					if bb.book.BID == search_r:
						return redirect("main:books")
					else:
						pass

				order_id = Checksum.__id_generator__()
				bill_amount = btb.price
				
				transaction = BookTransaction.objects.create(book=btb,student=student,orderid=order_id,amount=bill_amount)
				transaction.save()

				subject = 'Payment Successfull - Just Ask'
				text_content = f''
				html_content = f'''
				<p style='font-size:20px'>Hello {student.FirstName}, <br>This is to confirm that we have recieved your payment for book rental.<br></p>
				<p style='font-size:20px'><b>Your Payment Information: </b></p>
				<hr>
				<p><b>Book Status: </b>Rented</p>
				<p><b>Amount: </b>{bill_amount} USD</p>
				<p><b>Name of payer: </b>{student.FirstName} {student.SecondName}</p>
				<p><b>Order ID: </b>{order_id}</p>
				<p><b>Customer ID: </b>{student.Studentid}</p>
				<p><b>Book Rented on: </b>{datetime.now()}</p>
				<p><b>Book Expires on: </b>{datetime.now() + timedelta(days=122)}</p>

				
				<hr>
				<p style='font-size:15px'>Fore more information please email us on <b>support@just-ask.in</b></p>
				'''
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [student.Email,email_from, ] 

				msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				return render(request, 'main/payment_suc.html')
	else:
		if request.method == 'POST':
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username,password=password)
				
				if user is not None:
					login(request, user)
					messages.success(request, f"You are logged in as {username}")
					return redirect("main:books")
					
					
				else:	
					messages.error(request, "Invalid username or password")
			else:	
					messages.error(request, "Invalid username or password")

		form = AuthenticationForm()
		return render(request,"main/login.html",{"form":form})



def payment_buy(request):
	search_r = request.GET.get('book')
	print('================================')
	print(search_r)
	books = EBook.objects.all()
	btb = ''
	for b in books:
		if b.BID == search_r:
			btb = b
			if b.price == 0:
				q = {
				'book': b,
				}
				return render(request,"main/book_view.html",q)
			else:
				pass
		else:
			pass
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				trans = student.booktransaction_set.all()

				#check if trying to buy book two times.
				for bb in student.buybook_set.all():
					if bb.book.BID == search_r:
						return redirect("main:books")
					else:
						pass

				order_id = Checksum.__id_generator__()
				bill_amount = btb.price2
				
				duration = True
				transaction = BookTransaction.objects.create(book=btb,duration=duration,student=student,orderid=order_id,amount=bill_amount)
				transaction.save()

				subject = 'Payment Successfull - Just Ask'
				text_content = f''
				html_content = f'''
				<p style='font-size:20px'>Hello {student.FirstName}, <br>This is to confirm that we have recieved your payment for buying the book.<br></p>
				<p style='font-size:20px'><b>Your Payment Information: </b></p>
				<hr>
				<p><b>Book Status: </b>Permanent</p>
				<p><b>Amount: </b>{bill_amount} USD</p>
				<p><b>Name of payer: </b>{student.FirstName} {student.SecondName}</p>
				<p><b>Order ID: </b>{order_id}</p>
				<p><b>Customer ID: </b>{student.Studentid}</p>
				

				
				<hr>
				<p style='font-size:15px'>Fore more information please email us on <b>support@just-ask.in</b></p>
				'''
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [student.Email,email_from, ] 

				msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				return render(request, 'main/payment_suc.html')
	else:
		if request.method == 'POST':
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username,password=password)
				
				if user is not None:
					login(request, user)
					messages.success(request, f"You are logged in as {username}")
					return redirect("main:books")
					
				else:	
					messages.error(request, "Invalid username or password")
			else:	
					messages.error(request, "Invalid username or password")

		form = AuthenticationForm()
		return render(request,"main/login.html",{"form":form})


def numOfDays(date1, date2): 
    return (date2-date1).days


def paypalcallbackmonth(request):
	applied = True
	amount = 0
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):

				student.confirm = True
				student.subs = True

				if student.credits != 2000:
					student.credits = student.credits + 50

				student.StartDate = datetime.now()
				student.EndDate = datetime.now() + timedelta(days=30)
				order_id = ran_gen(6, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz")
				bill_amount = "7.99"

				transaction = SubsTransaction.objects.create(student=student,orderid=order_id, amount=bill_amount)
				transaction.save()

				subject = 'Payment Successfull - Just Ask'
				text_content = f''
				html_content = f'''
				<p style='font-size:20px'>Hello {student.FirstName}, <br>This is to confirm that we have recieved your payment.<br></p>
				<p style='font-size:20px'><b>Your Payment Information: </b></p>
				<hr>

				<p><b>Amount: </b>{bill_amount} USD</p>
				<p><b>Name of payer: </b>{student.FirstName} {student.SecondName}</p>
				<p><b>Order ID: </b>{order_id}</p>
				<p><b>Customer ID: </b>{student.Studentid}</p>
				<p><b>Subscription Plan: </b>Monthly</p>

				
				<hr>
				<p style='font-size:15px'>Fore more information please email us on <b>support@just-ask.in</b></p>
				'''
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [student.Email,email_from, ] 

				msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				student.qscore = 15
						
				student.save(update_fields=['StartDate','EndDate','subs','confirm','First','credits','qscore'])
				
	return redirect("main:profile")



def paypalcallbackyear(request):
	applied = True
	amount = 0
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):

				student.confirm = True
				student.subs = True
				student.anual = True
				
				if student.credits != 2000:
					student.credits = student.credits + 200
				student.StartDate = datetime.now()
				student.EndDate = datetime.now() + timedelta(days=365)
				order_id = ran_gen(8, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz")
				bill_amount = "79.99"
				
				transaction = SubsTransaction.objects.create(student=student,orderid=order_id, amount=bill_amount)
				transaction.save()
				

				subject = 'Payment Successfull - Just Ask'
				text_content = f''
				html_content = f'''
				<p style='font-size:20px'>Hello {student.FirstName}, <br>This is to confirm that we have recieved your payment.<br></p>
				<p style='font-size:20px'><b>Your Payment Information: </b></p>
				<hr>

				<p><b>Amount: </b>{bill_amount} USD</p>
				<p><b>Name of payer: </b>{student.FirstName} {student.SecondName}</p>
				<p><b>Order ID: </b>{order_id}</p>
				<p><b>Customer ID: </b>{student.Studentid}</p>
				<p><b>Subscription Plan: </b>Yearly</p>
				<hr>
				<p style='font-size:15px'>Fore more information please email us on <b>support@just-ask.in</b></p>
				
				
				'''
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = [student.Email,email_from, ] 

				msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				student.qscore = 150
					

				
				student.save(update_fields=['StartDate','EndDate','subs','confirm','First','credits','qscore'])
				
	return redirect("main:profile")


# def payment_mntly(request):
# 	if request.user.is_authenticated:
# 		students = Student.objects.all()
# 		for student in students:
# 			if (student.Email == request.user.email):
# 				if student.subs != True:
# 					return redirect("main:finish2")
# 				else:
# 					return redirect("main:profile")

# 	else:
# 		if request.method == 'POST':
# 			form = AuthenticationForm(request, data=request.POST)
# 			if form.is_valid():
# 				username = form.cleaned_data.get('username')
# 				password = form.cleaned_data.get('password')
# 				user = authenticate(username=username,password=password)
				
# 				if user is not None:
# 					login(request, user)
# 					messages.success(request, f"You are logged in as {username}")
# 					return redirect("main:rates")
# 				else:	
# 					messages.error(request, "Invalid username or password")
# 			else:	
# 					messages.error(request, "Invalid username or password")

# 		form = AuthenticationForm()
# 		return render(request,"main/login.html",{"form":form})



# def payment_yrly(request):
# 	if request.user.is_authenticated:
# 		students = Student.objects.all()
# 		for student in students:
# 			if (student.Email == request.user.email):
# 				if student.subs != True:
# 					student.anual = True
# 					student.save(update_fields=['anual'])

# 					return redirect("main:finish2")
# 				else:
# 					return redirect("main:profile")
# 	else:
# 		if request.method == 'POST':
# 			form = AuthenticationForm(request, data=request.POST)
# 			if form.is_valid():
# 				username = form.cleaned_data.get('username')
# 				password = form.cleaned_data.get('password')
# 				user = authenticate(username=username,password=password)
				
# 				if user is not None:
# 					login(request, user)
# 					messages.success(request, f"You are logged in as {username}")
# 					return redirect("main:rates")
# 				else:	
# 					messages.error(request, "Invalid username or password")
# 			else:	
# 					messages.error(request, "Invalid username or password")

# 		form = AuthenticationForm()
# 		return render(request,"main/login.html",{"form":form})



def payment_freefirst(request):
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				if student.subs != True and student.First == True:
					print('=================================================')
					if(student.First):
						student.confirm = True
						student.subs = True
						student.StartDate = datetime.now()
						student.EndDate = datetime.now() + timedelta(days=31)
						order_id = ran_gen(6, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz")
						bill_amount = "0"
						
						transaction = SubsTransaction.objects.create(student=student,orderid=order_id, amount=bill_amount)
						transaction.save()
						student.qscore = 10
						student.First = False


						subject = 'Payment Successfull - Just Ask'
						text_content = f''
						html_content = f'''
						<p style='font-size:20px'>Hello {student.FirstName}, <br>This is to confirm that we have activated your free trial.<br></p>
						<p style='font-size:20px'><b>Your Payment Information: </b></p>
						<hr>

						<p><b>Amount: </b>{bill_amount} USD</p>
						<p><b>Name of payer: </b>{student.FirstName} {student.SecondName}</p>
						<p><b>Order ID: </b>{order_id}</p>
						<p><b>Customer ID: </b>{student.Studentid}</p>
						<p><b>Subscription Plan: </b>Trial</p>

						
						<hr>
						<p style='font-size:15px'>Fore more information please email us on <b>support@just-ask.in</b></p>
						'''
						email_from = settings.EMAIL_HOST_USER 
						recipient_list = [student.Email,email_from, ] 

						msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
						msg.attach_alternative(html_content, "text/html")
						msg.send()
								
						student.save(update_fields=['StartDate','EndDate','subs','confirm','First','qscore'])
						

						return redirect("main:profile")
					else:
						pass
					
					
				else:
					return redirect("main:profile")
	else:
		if request.method == 'POST':
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username,password=password)
				
				if user is not None:
					login(request, user)
					messages.success(request, f"You are logged in as {username}")
					return redirect("main:rates")
				else:	
					messages.error(request, "Invalid username or password")
			else:	
					messages.error(request, "Invalid username or password")

		form = AuthenticationForm()
		return render(request,"main/login.html",{"form":form})
	return redirect("main:rates")


def process_subscription(request):

	# subscription_plan = request.session.get('subscription_plan')
	host = request.get_host()

	# if subscription_plan == '1-month':
	#     price = "7"
	#     billing_cycle = 1
	#     billing_cycle_unit = "M"
	# else:
	#     price = "70"
	#     billing_cycle = 1
	#     billing_cycle_unit = "Y"

	price = "0.1"
	billing_cycle = 1
	billing_cycle_unit = "M"


	paypal_dict  = {
		"cmd": "_xclick-subscriptions",
		'business': 'shravan.chaniara@gmail.com',#shravan.chaniara@gamil.com
		"a3": price,  # monthly price
		"p3": billing_cycle,  # duration of each unit (depends on unit)
		"t3": billing_cycle_unit,  # duration unit ("M for Month")
		"src": "1",  # make payments recur
		"sra": "1",  # reattempt payment on payment error
		"no_note": "1",  # remove extra notes (optional)
		'item_name': 'Content subscription',
		'custom': 1,     # custom data, pass something meaningful here
		'currency_code': 'USD',
		'notify_url': 'http://{}{}'.format(host,reverse('main:homepage')),
		'return_url': 'http://{}{}'.format(host,reverse('main:finish')),
		'cancel_return': 'http://{}{}'.format(host,reverse('main:profile')),
	}

	form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
	return render(request, 'main/process_subscription.html', locals())



@csrf_exempt
def response(request):
	resp = VerifyPaytmResponse(request)
	if resp['verified']:
		# save success details to db; details in resp['paytm']
		print('-----------------------------------------')
		print(resp)
		print('-------------------------------')
		print(request.POST)
		return render(request, 'main/payment_suc.html')
	else:
		# check what happened; details in resp['paytm']
		return render(request, 'main/payment_faild.html')

@csrf_exempt
def response_subs(request):
    resp = VerifyPaytmResponse(request)
    if resp['verified']:
        # save success details to db; details in resp['paytm']
        return render(request, 'main/payment_suc2.html')
    else:
        # check what happened; details in resp['paytm']
        return render(request, 'main/payment_faild.html')




def namedit(request):
	fname = request.POST.get('FName')
	lname = request.POST.get('LName')
	students = Student.objects.all()
	for student in students:
		if (student.Email == request.user.email):
			student.FirstName = fname
			student.SecondName = lname
			student.save(update_fields=['FirstName','SecondName'])
			profile(request)
			
	return redirect("main:profile")

def emailedit(request):
	email = request.POST.get('Email')
	students = Student.objects.all()
	for student in students:
		if (student.Email == request.user.email):
			student.Email = email
			student.save(update_fields=['Email'])

	return redirect("main:profile")



def countryedit(request):
	country = request.POST.get('country')
	students = Student.objects.all()
	for student in students:
		if (student.Email == request.user.email):
			student.Country = country
			
			student.save(update_fields=['Country'])
			

	return redirect("main:profile")


def playlistedit(request):
	country = request.POST.get('playlist')
	if request.user.is_anonymous != True:
		if country.find("open.spotify.com") != -1:
			request.user.student.playlist = country.replace("playlist", "embed/playlist")

			request.user.student.save(update_fields=['playlist'])
		else:
			pass
	else:
		return redirect("main:homepage")
			
	return redirect("main:profile")

def ppedit(request):
	file = request.FILES['pp']
	students = Student.objects.all()
	for student in students:
		if (student.Email == request.user.email):
			print(file)
			student.ProfilePicture = file
			
			student.save(update_fields=['ProfilePicture'])
			

	return redirect("main:profile")




def math(request):
	notes = {}
	nlist = []

	for n in Note.objects.all():
		if n.book_field == 'math':
			nlist.append(n)



	paginator = Paginator(nlist,6)

	page = request.GET.get('page')

	nlist = paginator.get_page(page)

	notes = {
		'notes':nlist,
		'field':'Math'
		}
	return render(request,"main/notes.html",notes)


def language(request):
	notes = {}
	nlist = []

	for n in Note.objects.all():
		if n.book_field == 'language':
			nlist.append(n)



	paginator = Paginator(nlist,6)

	page = request.GET.get('page')

	nlist = paginator.get_page(page)

	notes = {
		'notes':nlist,
		'field':'Language'
		}
	return render(request,"main/notes.html",notes)


def business(request):
	notes = {}
	nlist = []

	for n in Note.objects.all():
		if n.book_field == 'business':
			nlist.append(n)



	paginator = Paginator(nlist,6)

	page = request.GET.get('page')

	nlist = paginator.get_page(page)

	notes = {
		'notes':nlist,
		'field':'Commerce'
		}
	return render(request,"main/notes.html",notes)


def science(request):
	notes = {}
	nlist = []

	for n in Note.objects.all():
		if n.book_field == 'science and engineering':
			nlist.append(n)



	paginator = Paginator(nlist,6)

	page = request.GET.get('page')

	nlist = paginator.get_page(page)

	notes = {
		'notes':nlist,
		'field':'Sciences and Engineering'
		}
	return render(request,"main/notes.html",notes)

def socialscience(request):
	notes = {}
	nlist = []

	for n in Note.objects.all():
		if n.book_field == 'social science and history':
			nlist.append(n)



	paginator = Paginator(nlist,6)

	page = request.GET.get('page')

	nlist = paginator.get_page(page)

	notes = {
		'notes':nlist,
		'field':'Social Science and History'
		}
	return render(request,"main/notes.html",notes)

def computerscience(request):
	notes = {}
	nlist = []

	for n in Note.objects.all():
		if n.book_field == 'computer science':
			nlist.append(n)



	paginator = Paginator(nlist,6)

	page = request.GET.get('page')

	nlist = paginator.get_page(page)

	notes = {
		'notes':nlist,
		'field':'Computer Science'
		}
	return render(request,"main/notes.html",notes)

def other(request):
	notes = {}
	nlist = []

	for n in Note.objects.all():
		if n.book_field == 'other':
			nlist.append(n)



	paginator = Paginator(nlist,6)

	page = request.GET.get('page')

	nlist = paginator.get_page(page)

	notes = {
		'notes':nlist,
		'field':'Other'
		}
	return render(request,"main/notes.html",notes)

def notesearch_request(request):
	books = []
	qlist = []

	search_r = re.sub(' +', ' ',request.GET.get('search')).rstrip().lstrip()
	empty = (search_r == '')
	if empty:
		return redirect("main:notes")
	else:
		for book in Note.objects.all():

			match1 = lev.ratio(search_r,book.File_name) #Title
			match2 = lev.ratio(search_r,book.Description) #ISBN
			match3 = lev.ratio(search_r,book.Auth) #Author

			match = maximum(match1, match2, match3)

			cord = (book,match*100)
			books.append(cord)
			

		sortlist = Sort_Tuple(books)
		
		
		for s in range(len(sortlist)):
			qlist.append(sortlist[s][0])

			# for y in search_r.split():
			# 	if re.search(y.lower(), sortlist[s][0].Description.lower()):
					
			# 		break
			# 	else:
			# 		pass
			


		paginator = Paginator(qlist,8)

		page = request.GET.get('page')

		qlist = paginator.get_page(page)

		q = {
		'question': search_r,
		'qs':qlist,
		}
	return render(request,"main/note_search.html",q)

def noteview_request(request):
	sub_ceck(request)
	checkbook(request)
	search_r = request.GET.get('notes')
	print(search_r)
	q = {
		'notes': '',
		
		}

	books = Note.objects.all()
	if request.user.is_authenticated:
		students = Student.objects.all()
		for student in students:
			if (student.Email == request.user.email):
				if student.subs:
					for book in books:
						if(book.File == search_r):
							print('---------------------')
							q = {
							'notes': book,
							}
							break
				else:
					q = {
						'notes': None,
						}
		
	return render(request,"main/note_view.html",q)
	
