from django.urls import path
from kb import views

urlpatterns = [
    path('problems', views.Problems.as_view(), name='problems'),
    path('problems/<int:pk>', views.Problem.as_view(), name='problem_one'),
    path('solutions', views.Solutions.as_view(), name='solutions'),
    path('solutions/<int:pk>', views.Solution.as_view(), name='solution_one'),
    path('sample_problem', views.SampleProblem.as_view(), name='sample_problem'),
]
