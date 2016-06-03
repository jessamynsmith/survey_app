from django.shortcuts import render

from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView, TemplateResponseMixin,ContextMixin

from .models import Survey

# Create your views here.

# class SurveyCreateView(CreateView):
#     # model = Book
#     template_name="forms.html"
#     # fields = ['title','description']
#     form_class = SurveyForm
#     # def get_success_url(self):
#     #     return reverse("book_list")
    
#     def form_valid(self, form):
#         print(form.instance)
#         form.instance.added_by = self.request.user
#         form.instance.last_edited_by = self.request.user
#         return super(BookCreateView,self).form_valid(form)