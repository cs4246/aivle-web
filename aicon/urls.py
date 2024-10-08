"""aicon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from app import views, apis

urlpatterns = [
    path('', views.courses, name='home'),

    path('courses/', views.courses, name='courses'),
    path('courses/new/', views.course_add, name='course_add'),
    path('courses/<int:course_pk>/', views.course, name='course'),
    path('courses/<int:course_pk>/delete/', views.course_delete, name='course_delete'),
    path('courses/<int:course_pk>/join/', views.course_join, name='course_join'),

    path('courses/<int:course_pk>/tasks/new/package', views.task_edit_package, name='task_new_package'),
    path('courses/<int:course_pk>/tasks/new/code', views.task_edit_code, name='task_new_code'),
    path('courses/<int:course_pk>/tasks/<int:task_pk>/edit/package', views.task_edit_package, name='task_edit_package'),
    path('courses/<int:course_pk>/tasks/<int:task_pk>/edit/code', views.task_edit_code, name='task_edit_code'),
    path('courses/<int:course_pk>/tasks/<int:task_pk>/delete/', views.task_delete, name='task_delete'),
    path('courses/<int:course_pk>/tasks/<int:task_pk>/leaderboard/', views.leaderboard, name='leaderboard'),
    path('courses/<int:course_pk>/tasks/<int:task_pk>/stats/', views.stats, name='stats'),
    path('courses/<int:course_pk>/tasks/<int:task_pk>/similarities/', views.similarities, name='similarities'),

    path('courses/<int:course_pk>/tasks/<int:task_pk>/submissions/', views.submissions, name='submissions'),
    path('courses/<int:course_pk>/tasks/<int:task_pk>/submissions/new/package/', views.submission_new_package, name='submission_new_package'),
    path('courses/<int:course_pk>/tasks/<int:task_pk>/submissions/new/code/', views.submission_new_code, name='submission_new_code'),
    path('courses/<int:course_pk>/tasks/<int:task_pk>/submissions/<int:submission_pk>/new/code/', views.submission_clone_code, name='submission_clone_code'),

    path('partial/courses/<int:course_pk>/tasks/<int:task_pk>/submissions/', views.partial_submissions, name='partial_submissions'),
    path('partial/submissions/<int:pk>/', views.partial_submission, name='partial_submission'),

    path('tasks/<int:pk>/download/', views.task_download, name='task_download'),
    path('tasks/<int:pk>/template/', views.template_download, name='template_download'),
    path('submissions/<int:pk>/download/', views.submission_download, name='submission_download'),
    path('submissions/action/', views.submissions_action, name='submissions_action'),

    path('api/v1/', include(apis.router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('signup/', views.signup, name='signup'),
]
