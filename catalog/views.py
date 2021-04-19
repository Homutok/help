from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from .models import Category,Answer,Questions,Comment
from django.contrib.auth.models import User
from django.http import Http404
def index(request):
    num_comment=Comment.objects.count()
    num_answers=Answer.objects.count()
    num_questions=Questions.objects.count()
    num_users=User.objects.count()
    questions_detail=Questions.category
    context = {
    'num_users': num_users,
    'num_comment':num_comment,
    'num_answers':num_answers,
    'num_questions':num_questions,
    'questions_detail':questions_detail
    }
    return render(request, 'index.html',context=context)
class QuestionsListView(generic.ListView):
    model = Questions
    context_object_name = 'my_guide_list'
    template_name = 'guide/questions_list.html'
class QuestionsDetailView(generic.DetailView):
    model = Questions
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_data'] = Comment.objects.filter(questions=self.object)
        print(context)
        return context
    def guide_detail_view(request, pk):
        try:
            guide_id = Questions.objects.get(pk=pk)
        except Questions.DoesNotExist:
            raise Http404("Записи не сщуествет ¯\_(ツ)_/¯ ")
        return render(
            request,
            'catalog/questions_detail.html',
            context={'guide': guide_id, }
        )

# Create your views here.
