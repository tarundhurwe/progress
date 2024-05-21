from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("problems/<int:id>", views.ProblemView.as_view(), name="problem list"),
    path(
        "problems/<int:id>/<int:problem_id>",
        views.CreateNoteView.as_view(),
        name="create note",
    ),
    path(
        "problems/marked/<int:problem_set_id>",
        views.UserMarkedProblemsView.as_view(),
        name="marked problems",
    ),
    path(
        "problems/mark/<int:problem_set_id>/<int:problem_id>",
        views.UpdateStatusView.as_view(),
        name="mark",
    ),
]
