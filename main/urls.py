"""MACK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include


app_name = "main"

urlpatterns = [
	path("", views.homepage, name="homepage"),
    path('tinymce/', include('tinymce.urls')),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("search_request/", views.search_request, name="search_request"),
    path("answer_request/", views.answer_request, name="answer_request"),
    path("question_post/", views.question_post, name="question_post"),
    path("question_p/", views.question_p, name="question_p"),
    path("answer_post/", views.answer_post, name="answer_post"),
    path("like_question/", views.like_question, name="like_question"),
    path("dislike_question/", views.dislike_question, name="dislike_question"),
    path("books/", views.books, name="books"),
    path("booksearch_request/", views.booksearch_request, name="booksearch_request"),
    path("bookbuy_request/", views.bookbuy_request, name="bookbuy_request"),
    path("bookview_request/", views.bookview_request, name="bookview_request"),
    path("booksoltuion_request/", views.booksoltuion_request, name="booksoltuion_request"),
    path("solution/", views.solution, name="solution"),
    path("booksolsearch_request/", views.booksolsearch_request, name="booksolsearch_request"), # not in service
    path("booksoltuion_view/", views.booksoltuion_view, name="booksoltuion_view"),
    path("bookaddition_request/", views.bookaddition_request, name="bookaddition_request"),
    path("writing/", views.writing, name="writing"),
    path('payment/', views.payment,name="payment"),
    path('payment_buy/', views.payment_buy,name="payment_buy"),
    path('feedback/', views.feedback,name="feedback"),
    # path('payment_mntly/', views.payment_mntly,name="payment_mntly"),
    # path('payment_yrly/', views.payment_yrly,name="payment_yrly"),

    path('response/', views.response,name="response"), # not in service
    path('response_subs/', views.response_subs,name="response_subs"), # not in service

    path("contrib/", views.contrib, name="contrib"),
    path('rates/', views.rates,name="rates"),
    path('finish/', views.finish,name="finish"),
    path('paypalcallbackmonth/', views.paypalcallbackmonth,name="paypalcallbackmonth"),
    path('paypalcallbackyear/', views.paypalcallbackyear,name="paypalcallbackyear"),
    path('profile/', views.profile,name="profile"),
    path('cancel/', views.Cancel,name="cancel"),

    path("namedit/", views.namedit, name="namedit"),
    path("emailedit/", views.emailedit, name="emailedit"), # not in service
    path("countryedit/", views.countryedit, name="countryedit"),
    path("playlistedit/", views.playlistedit, name="playlistedit"),
    path("ppedit/", views.ppedit, name="ppedit"),
    path("QNA/", views.QNA, name="QNA"),
    path("customer_service/", views.customer_service, name="customer_service"),
    path("inquire/", views.inquire, name="inquire"),
    path("notes/", views.notes, name="notes"),
    path("payment_freefirst/", views.payment_freefirst, name="payment_freefirst"),
    # path("password_reset/", views.password_reset, name="password_reset"),
    path("notesearch_request/", views.notesearch_request, name="notesearch_request"),
    path("noteview_request/", views.noteview_request, name="noteview_request"),
    path("math/", views.math, name="math"),
    path("language/", views.language, name="language"),
    path("business/", views.business, name="business"),
    path("science/", views.science, name="science"),
    path("socialscience/", views.socialscience, name="socialscience"),
    path("computerscience/", views.computerscience, name="computerscience"),
    path("other/", views.other, name="other"), # notes field


    path("note_contrib/", views.note_contrib, name="note_contrib"),
    path("book_contrib/", views.book_contrib, name="book_contrib"), # not in service
    path("questionpost/", views.questionpost, name="questionpost"),
    path("already_sub/", views.already_sub, name="already_sub"),
    path("bookbuyview_request/", views.bookbuyview_request, name="bookbuyview_request"),
    path("comment/", views.comment, name="comment"),
    path("terms/", views.terms, name="terms"),
    # path("ReferFriend/", views.ReferFriend, name="ReferFriend"),
    path("RedeemCredts/", views.RedeemCredts, name="RedeemCredts"),
    path("CSV/", views.CSV, name="CSV"),
    path("csvImport/", views.csvImport, name="csvImport"),
    path("unanswered/", views.unanswered, name="unanswered"),
    path("qsearch_request/", views.qsearch_request, name="qsearch_request"),
    path("expert_apply/", views.expert_apply, name="expert_apply"),
    path("quiz/", views.quiz, name="quiz"),

    path("QuizCheck/", views.QuizCheck, name="QuizCheck"),
    # path("home/", views.home, name="home"),
    path("TYDONATE/", views.TYDONATE, name="TYDONATE"),
    path("process_subscription/", views.process_subscription, name="process_subscription"),



    # path(
    #     "ads.txt",
    #     RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    # ),



]




if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 

