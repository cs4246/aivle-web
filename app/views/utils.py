from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from rules.contrib.views import PermissionRequiredMixin
from typing import Optional
from app.models import Course, Task, Submission

import re


class AutoSetupMixin:
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        if "course_pk" in self.kwargs:
            self.course = get_object_or_404(Course, pk=self.kwargs["course_pk"])
        if "task_pk" in self.kwargs:
            self.task = get_object_or_404(Task, pk=self.kwargs["task_pk"])
        if "submission_pk" in self.kwargs:
            self.submission = get_object_or_404(Submission, pk=self.kwargs["submission_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self, "course"):
            context["course"] = self.course
        if hasattr(self, "task"):
            context["task"] = self.task
        if hasattr(self, "submission"):
            context["submission"] = self.submission
        return context


class SuccessMessageMixin:
    def form_valid(self, form):
        response = super().form_valid(form)
        if hasattr(self, "success_message"):
            messages.success(self.request, eval(f"f'{self.success_message}'"))
        return response


class NeverCacheMixin:
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class StatusResponseMixin:
    def get_status(self) -> Optional[int]:
        return None

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("content_type", self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            status=self.get_status(),
            **response_kwargs,
        )


class AutoPermissionRequiredMixin(PermissionRequiredMixin):
    def get_permission_required(self):
        permission_required = ".".join(re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', self.__class__.__name__).lower().split()[:-1])
        return [permission_required]


class CoursePermissionMixin:
    def get_permission_object(self):
        return getattr(self, "course", None)


class SubmissionPermissionMixin:
    def get_permission_object(self):
        return getattr(self, "submission", None)


class TaskPermissionMixin:
    def get_permission_object(self):
        return getattr(self, "task", None)
