# Django
from django.urls import include, path
# local Django
from .views import classroom, students, teachers

"""
Setting the urls of the classroom file, which connect with the views
"""
urlpatterns = [
    path('', classroom.home, name='home'),

    path('students/', include(([
        #path('', students.ProductListView.as_view(), name='students'),
        path('search/', students.ProductSearchListView.as_view(), name='students'),
        path('search/', students.ProductSearchListView.as_view(), name='search'),
        path('search/<slug:slug>/', students.detailView, name='product'),
        path('quiz/', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'classroom'), namespace='students')),

     path('teachers/', include(([
        path('', teachers.homepage, name='teachers'),
        
        path('quiz/', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('<slug:slug>/', teachers.profile, name='profile'),
        path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='teachers')),
]

