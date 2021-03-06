
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions


from .serializers import *
from .permissions import IsActiveUser, IsSuperUser, IsProfileOrReadOnly

from admissions.models import Admission
from appointments.models import Appointment
from counselling_sessions.models import CounsellingSession
from programs.models import Program
from patients.models import Patient, Enrollment
from user.models import CommuniqueUser, Profile



class ProgramViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Program models.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that has created the Program
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class PatientViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Patient models.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that has created the Patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Enrollment models.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(enrolled_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class CommuniqueUserViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD CommuniqueUser models.

    Only superusers can access it.
    """
    queryset = CommuniqueUser.objects.all()
    serializer_class = CommuniqueUserSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser, IsSuperUser,)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Profile models.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser, IsProfileOrReadOnly,)


class ProfileLoginView(generics.RetrieveAPIView):
    """
    This endpoint retrieves a user's profile on successful login.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    permission_classes = (permissions.IsAuthenticated,)


class CounsellingSessionViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD CounsellingSession models.
    """
    queryset = CounsellingSession.objects.all()
    serializer_class = CounsellingSessionSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class CounsellingSessionTypeViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD CounsellingSessionType models.
    """
    queryset = CounsellingSessionType.objects.all()
    serializer_class = CounsellingSessionTypeSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Appointment models.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class AdmissionsViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Admissions models.
    """
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)
