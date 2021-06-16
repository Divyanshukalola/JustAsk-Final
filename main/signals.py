# Signals that fires when a user logs in and logs out

from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from main.models import LoggedInUser
from . models import SubsTransaction

from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from datetime import datetime

from django.shortcuts import render, redirect


import random 
import string 

def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
	return ''.join(random.choice(chars) for x in range(size))

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user')) 


@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()


@receiver(valid_ipn_received)
def ipn_receiver(sender, **kwargs):
	ipn_obj = sender

	# check for Buy Now IPN
	if ipn_obj.txn_type == 'web_accept':

		if ipn_obj.payment_status == ST_PP_COMPLETED:
			# payment was successful
			print('great!')
			order = get_object_or_404(Order, id=ipn_obj.invoice)

			if order.get_total_cost() == ipn_obj.mc_gross:
				# mark the order as paid
				order.paid = True
				order.save()


	# check for subscription signup IPN
	elif ipn_obj.txn_type == "subscr_signup":
		# get user id and activate the account
		id = ipn_obj.custom
		user = User.objects.get(id=id)
		user.active = True
		user.save()

	# check for subscription payment IPN
	elif ipn_obj.txn_type == "subscr_payment":

		# get user id and extend the subsscription
		id = ipn_obj.custom
		user = User.objects.get(id=id)
		# user.extend()  # extend the subscription

		if request.user.is_authenticated:
			for stud in Student.objects.all():
				if stud.Email == request.user.email:
					order_id = ran_gen(6, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz")

					bill_amount = ipn_obj.payment_gross
					
					subject = 'Subscription Renewal Successfull - Just Ask'
					text_content = f''
					html_content = f'''
					<p style='font-size:17px'>Hello {stud.FirstName}, <br>This is to inform that we have recieved your payment. You subscription in Just Ask is successfully renewed.<br></p>
					
					<hr>
					<p><b>Amount: </b>{bill_amount} USD</p>
					<p><b>Name of payer: </b>{stud.FirstName} {stud.SecondName}</p>
					<p><b>Order ID: </b>{order_id}</p>
					<p><b>Customer ID: </b>{stud.Studentid}</p>
					<p style='font-size:15px'>Fore more information please email us on <b>support@just-ask.in</b></p>
					'''
					email_from = settings.EMAIL_HOST_USER 
					recipient_list = [stud.Email, ] 

					msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
					msg.attach_alternative(html_content, "text/html")
					msg.send()

					
					transaction = SubsTransaction.objects.create(student=request.user.student,orderid=order_id, amount=bill_amount)
					transaction.save()

	# check for failed subscription payment IPN
	elif ipn_obj.txn_type == "subscr_failed":
		pass

	# check for subscription cancellation IPN
	elif ipn_obj.txn_type == "subscr_cancel":
		pass



