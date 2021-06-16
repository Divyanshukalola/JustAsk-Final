from django.contrib import admin


from . models import Student,Question,Answer,EBook,Note,Paper,Like,Dislike,BuyBook,BookSol,BookRequest,BookTransaction,SubsTransaction,Message,Text,Comments,CreditTransaction
from . models import Refer,Choice,QuizeQuestion,Searche,Feedback
from tinymce.widgets import TinyMCE
from django.db import models

from django.contrib import admin

from .actions import export_as_csv_action

from django.contrib.admin.models import LogEntry, DELETION

from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags


    



# Register your models here.
# class DesignAdmin(admin.ModelAdmin):
# 	fields = ["design_title",
# 			  "design_description",
# 			  "design_cover",
# 			  "design_published"]

class ReferAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Details",{"fields":["student","madeon","referedby","credits"]}),
		]

	readonly_fields = ["student","madeon","referedby","credits"]

	search_fields = ['student__FirstName', 'student__SecondName', 'student__Email','student__Studentid', 'referedby','madeon']

	actions = [export_as_csv_action("CSV Export", fields=["student","madeon","referedby","credits"])]


class FeedBackAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Details",{"fields":["user","where","concern","suggestions"]}),
		]

	actions = [export_as_csv_action("CSV Export", fields=["user","where","concern","suggestions"])]

class CreditTransactionAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Details",{"fields":["student","madeon","credits","orderid","checksum","applied"]}),
		]

	readonly_fields = ["madeon","credits","orderid","checksum"]

	search_fields = ['student__FirstName', 'student__SecondName', 'student__Email','student__Studentid', 'orderid']

	actions = [export_as_csv_action("CSV Export", fields=["student","madeon","credits","orderid","checksum","applied"])]


class TransactionAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Details",{"fields":["student","book","duration","madeon","amount","orderid","checksum","applied"]}),
		]

	readonly_fields = ["madeon","amount","orderid","checksum"]

	search_fields = ['student__FirstName', 'student__SecondName', 'student__Email','student__Studentid', 'orderid','madeon']

	actions = [export_as_csv_action("CSV Export", fields=["student","book","duration","madeon","amount","orderid","checksum","applied"])]

class MessageAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Details",{"fields":["name","email","subject","message"]}),
		]

	search_fields = ['name', 'email', 'subject', 'message']

	actions = [export_as_csv_action("CSV Export", fields=["name","email","subject","message"])]


class CommentAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Details",{"fields":["student","ans","text"]}),
		]

	search_fields = ['student__FirstName', 'student__SecondName', 'student__Email','student__Studentid', 'text']

	actions = [export_as_csv_action("CSV Export", fields=["student","ans","text"])]



class SubTransactionAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Details",{"fields":["student","madeon","amount","orderid","checksum","applied"]}),
		]

	readonly_fields = ["madeon","orderid","checksum"]

	search_fields = ['student__FirstName', 'student__SecondName', 'student__Email','student__Studentid', 'amount', 'orderid', 'checksum','madeon']


	actions = [export_as_csv_action("CSV Export", fields=["student","madeon","amount","orderid","checksum","applied"])]

class TextAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("text",{"fields":["text"]}),
		]

	readonly_fields = ["text"]

	search_fields = ['text',]

	actions = [export_as_csv_action("CSV Export", fields=["text"])]


class LikeAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Likes",{"fields":["qid","student"]}),
		]

	readonly_fields = ["qid","student"]

	search_fields = ['qid', 'student__FirstName', 'student__SecondName', 'student__Email','student__Studentid',]

	actions = [export_as_csv_action("CSV Export", fields=["qid","student"])]


class SearcheAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Likes",{"fields":["text","user","date"]}),
		]

	actions = [export_as_csv_action("CSV Export", fields=["text","user","date"])]

class BookAddAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("Details",{"fields":["Description"]}),
		]

	readonly_fields = ["Description"]

	search_fields = ['Description',]

	actions = [export_as_csv_action("CSV Export", fields=["Description"])]



class DisLikeAdmin(admin.ModelAdmin):
	
	fieldsets = [
		("DisLikes",{"fields":["qid","student","reason"]}),
		]

	readonly_fields = ["qid","student","reason"]

	search_fields = ['qid', 'student__FirstName', 'student__SecondName', 'student__Email','student__Studentid',"reason"]

	actions = [export_as_csv_action("CSV Export", fields=["qid","student","reason"])]
		
class EBookAdmin(admin.ModelAdmin):
	fieldsets = [
		("Details",{"fields":["File_name","book_field","File","Edition","Bcover","Auth","BID","Description","price","price2","Email","Uploaded"]}),
		]

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
	
	search_fields = ['File_name', 'Auth', 'BID', 'Description','Uploaded']

	list_display = ("File_name", 'BID', "book_field", "Email",)
	list_filter = ('Uploaded',)

	actions = [export_as_csv_action("CSV Export", fields=["File_name","book_field","File","Edition","Bcover","Auth","BID","Description","price","price2","email","Uploaded"])]

		
class BookSolAdmin(admin.ModelAdmin):
	fieldsets = [
		("Details",{"fields":["Ebook","File_name","book_field","File","Edition","Bcover","Auth","Description"]}),
		]

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
	
	search_fields = ['Ebook', 'File_name', 'Edition', 'Auth']

	actions = [export_as_csv_action("CSV Export", fields=["Ebook","File_name","book_field","File","Edition","Bcover","Auth","Description"])]

class NotesAdmin(admin.ModelAdmin):
	fieldsets = [
		("Details",{"fields":["File_name","book_field","File","Auth","Description","Email","Uploaded"]}),
		]

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

	search_fields = ['File_name', 'Auth', 'Description','Uploaded']

	list_display = ("File_name", "book_field", "Email",)
	list_filter = ('Uploaded',)



	actions = [export_as_csv_action("CSV Export", fields=["File_name","book_field","File","Auth","Description","Email","Uploaded"])]

class PaperAdmin(admin.ModelAdmin):
	fieldsets = [
		("Details",{"fields":["File_name","book_field","File","Description","Date"]}),
		]

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

class StudentAdmin(admin.ModelAdmin):

	fieldsets = [
		("Details",{"fields":["FirstName","SecondName","Email","Cuser","playlist","expert","Studentid","Country","ProfilePicture","First","subs","anual","StartDate","EndDate","credits","quiz","QuizDate","testscore","fieldofexpertise","qscore","QuizScoreCard"]}),
		]

	search_fields = ['FirstName', 'Studentid', 'Email', 'Country',"testscore","QuizScoreCard","PayPalSub"]

	list_display = ("FirstName", 'SecondName','Studentid', "Email", "Cuser","Country","expert")
	list_filter = ('Country','First','subs','anual','confirm',"expert")

	actions = [export_as_csv_action("CSV Export", fields=["FirstName","SecondName","Email","Studentid","playlist","Country","ProfilePicture","First","subs","anual","StartDate","EndDate","credits","confirm","expert","Cuser","quiz","QuizDate","testscore","fieldofexpertise","qscore","QuizScoreCard"])]

class QuestionAdmin(admin.ModelAdmin):

	fieldsets = [
		("Details",{"fields":["student","question","qid","question_field","question_cover","answered"]}),
		]

	list_display = ("question_str", 'student','qid', "question_field", "answered")
	list_filter = ('answered','question_field')
	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

	search_fields = ('student__FirstName', 'student__SecondName', 'student__Email','student__Studentid', 'question', 'qid', 'question_field',)

	actions = [export_as_csv_action("CSV Export", fields=["student","question","qid","question_field","question_cover","answered"])]

	

class AnswerAdmin(admin.ModelAdmin):

	fieldsets = [
		("Details",{"fields":["question","answer","ans_file","ans_file2","ans_file3","ans_file4","ans_file5","ans_file6","ans_file7","ans_file8","ans_file9","ans_file10","student","likes","dislikes"]}),
		]


	list_display = ("answer_", 'qid', 'student')

	# def answer(self, obj):
 #        return (obj.answer)
	
	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

	search_fields = ['question__question', 'answer', 'student__FirstName', 'student__SecondName', 'student__Email','student__Studentid',]
	list_filter = ('likes','dislikes')

	actions = [export_as_csv_action("CSV Export", fields=["question","answer","ans_file","ans_file2","ans_file3","ans_file4","ans_file5","ans_file6","ans_file7","ans_file8","ans_file9","ans_file10","student","likes","dislikes"])]



class BookBuyAdmin(admin.ModelAdmin):

	fieldsets = [
		("Details",{"fields":["book","student","StartDate","EndDate","rental"]}),
		]

	search_fields = ['book', 'student__FirstName', 'student__SecondName', 'student__Email','student__Studentid',"StartDate","EndDate","rental"]

	actions = [export_as_csv_action("CSV Export", fields=["book","student","StartDate","EndDate","rental"])]



class QuizeQuestionAdmin(admin.ModelAdmin):

	fieldsets = [
		("Details",{"fields":["question","question_field","question_cover","style"]}),
		]

	search_fields = ['question']
	list_display = ("question","question_field")

	actions = [export_as_csv_action("CSV Export", fields=["question","get_answers"])]


	
	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


class QuizeChoiceAdmin(admin.ModelAdmin):

	fieldsets = [
		("Details",{"fields":["question","choice","is_answer","answer_cover"]}),
		]

	list_display = ("question","choice","is_answer")

	search_fields = ["question__question","choice","is_answer","question__question_field"]

	actions = [export_as_csv_action("CSV Export", fields=["question","choice","is_answer","answer_cover"])]


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
    ]

    actions = [export_as_csv_action("CSV Export", fields=["action_time","user","content_type","object_link","action_flag"])]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"







admin.site.register(EBook, EBookAdmin)
admin.site.register(Note, NotesAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Dislike, DisLikeAdmin)
admin.site.register(BuyBook, BookBuyAdmin)
admin.site.register(BookSol, BookSolAdmin)
admin.site.register(BookRequest, BookAddAdmin)
admin.site.register(BookTransaction, TransactionAdmin)
admin.site.register(SubsTransaction, SubTransactionAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(CreditTransaction, CreditTransactionAdmin)
admin.site.register(Refer, ReferAdmin)
admin.site.register(QuizeQuestion, QuizeQuestionAdmin)
admin.site.register(Choice, QuizeChoiceAdmin)
admin.site.register(Searche, SearcheAdmin)
admin.site.register(Feedback, FeedBackAdmin)