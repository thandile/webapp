from django.core.urlresolvers import reverse_lazy

from communique.views import (CommuniqueCreateView, CommuniqueDetailView, CommuniqueDeleteView, CommuniqueListView,
                              CommuniqueUpdateView)
from .models import Admission
from .forms import AdmissionUpdateForm, AdmissionCreateForm


class AdmissionCreateView(CommuniqueCreateView):
    """
    A view that handles creation of an admission.
    """
    model = Admission
    form_class = AdmissionCreateForm
    template_name = 'admissions/admission_form.html'

    def form_valid(self, form):
        # the creator and modified by fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        return super(AdmissionCreateView, self).form_valid(form)


class AdmissionDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of an admission.
    """
    model = Admission
    template_name = 'admissions/admission_view.html'
    context_object_name = 'admission'


class AdmissionUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating of an admission.
    """
    model = Admission
    form_class = AdmissionUpdateForm
    template_name = 'admissions/admission_update_form.html'
    context_object_name = 'admission'

    def form_valid(self, form):
        # update the last modified by field
        form.instance.last_modified_by = self.request.user

        return super(AdmissionUpdateView, self).form_valid(form)


class AdmissionListView(CommuniqueListView):
    """
    A view that lists the existing admissions.
    """
    model = Admission
    template_name = 'admissions/admission_list.html'
    context_object_name = 'admission_list'


class AdmissionDeleteView(CommuniqueDeleteView):
    """
    A view that handles deletion of an admission.
    """
    model = Admission
    success_url = reverse_lazy('admissions_admission_list')
    context_object_name = 'admission'
    template_name = 'admissions/admission_confirm_delete.html'
