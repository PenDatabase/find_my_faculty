from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from django.db.models import Q
from django.apps import apps
from django.utils.text import capfirst
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import LecturerUpdateForm

from .models import (
    Lecturer,
    Department,
    College,
    Office,
    HODLecturer,
    SecretaryLecturer,
)

def home(request):
    return render(request, 'find_my_lecturer_app/home.html')



@login_required
def lecturer_dashboard(request):
    return render(request, "find_my_lecturer_app/lecturer/dashboard.html")




class LecturerListView(ListView):
    model = Lecturer
    template_name = "find_my_lecturer_app/lecturer_listing.html"
    context_object_name = "lecturers"
    paginate_by = 25

    def get_queryset(self):
        qs = Lecturer.objects.select_related("department", "office", "department__college")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(
                Q(full_name__icontains=q)
                | Q(department__name__icontains=q)
                | Q(department__college__name__icontains=q)
                | Q(office__office_number__icontains=q)
                | Q(office__location__icontains=q)
            )
        return qs.order_by("full_name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "").strip()
        context["colleges"] = College.objects.all().only("college_id", "name")
        context["departments"] = Department.objects.select_related("college").only("department_id", "name", "college__name")
        return context


class LecturerDetailView(DetailView):
    model = Lecturer
    template_name = "find_my_lecturer_app/lecturer_detail.html"
    context_object_name = "lecturer"
    pk_url_kwarg = "lecturer_id"

    def get_queryset(self):
        return super().get_queryset().select_related("office", "department", "department__college")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lecturer = self.object
        context["office"] = lecturer.office
        context["department"] = lecturer.department
        context["college"] = lecturer.department.college if lecturer.department else None

        # For HOD/Secretary roles, fetch from related link tables (if exists)
        try:
            context["is_hod"] = hasattr(lecturer, "hod_record")
            context["hod_id"] = lecturer.hod_record.hod_id if context["is_hod"] else None
        except:
            context["is_hod"] = False

        try:
            context["is_secretary"] = hasattr(lecturer, "secretary_record")
            context["secretary_id"] = lecturer.secretary_record.secretary_id if context["is_secretary"] else None
        except:
            context["is_secretary"] = False

        return context


class ModelsOverviewView(TemplateView):
    template_name = "find_my_lecturer_app/models_overview.html"
    model_set = [College, Department, Office, Lecturer, HODLecturer, SecretaryLecturer]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        models_info = []
        for mdl in self.model_set:
            meta = mdl._meta
            field_info = []
            for field in meta.get_fields():
                if not getattr(field, "concrete", False):
                    continue

                if field.is_relation and field.related_model:
                    f_type = f"{capfirst(field.get_internal_type())} ➔ {field.related_model.__name__}"
                else:
                    f_type = field.get_internal_type()

                field_info.append({
                    "name": field.name,
                    "type": f_type,
                    "null": getattr(field, "null", False),
                    "pk": field.primary_key,
                    "choices": field.choices if field.choices else None,
                })

            sample_rows = mdl.objects.all()[:5]

            models_info.append({
                "model_name": mdl.__name__,
                "db_table": meta.db_table,
                "fields": field_info,
                "samples": sample_rows,
            })

        context["models_info"] = models_info
        return context
    


class LecturerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "find_my_lecturer_app/lecturer_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lecturer = Lecturer.objects.select_related("department", "office").filter(user=self.request.user).first()
        if not lecturer:
            raise Http404("No lecturer profile is linked to this user.")
        context["lecturer"] = lecturer
        return context








class LecturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Lecturer
    form_class = LecturerUpdateForm
    template_name = "find_my_lecturer_app/lecturer_edit.html"

    def get_queryset(self):
        return Lecturer.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('find_my_lecturer_app:lecturer-dashboard')
