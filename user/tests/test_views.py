"""
Contains test cases for the views of the user app.
"""
from django.test import TestCase
from django.core.urlresolvers import reverse

from user.models import CommuniqueUser

class CommuniqueUserViewsTestCase(TestCase):
    def setUp(self):
        """
        Creates a super user and regular user to be used throughout testing.
        """
        CommuniqueUser.objects.create_user('regular_user',
            'regularuser@gmail.com', 'p@55words')
        CommuniqueUser.objects.create_superuser('super_user',
            'superuser@gmail.com', 'p@55words')

    def template_test(self, view_url, template_name):
        """
        Tests that the right template is used to the view.
        """
        self.client.login(username='super_user', password='p@55words')
        response = self.client.get(view_url)
        self.assertTemplateUsed(response, template_name)

    def context_object_test(self, view_url, context_object_name):
        """
        Tests that the context object with the provided name is generated by the
        view.
        """
        self.client.login(username='super_user', password='p@55words')
        response = self.client.get(view_url)
        self.assertTrue(response.context[context_object_name])

    def only_superuser_access_test(self, view_url, template_name):
        """
        Tests that only a superuser can access the view.

        If the user is not a superuser, he or she is redirected to the login
        page.
        """
        super_user = CommuniqueUser.objects.get(username='super_user')
        self.assertTrue(super_user.is_superuser)
        self.client.force_login(super_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, template_name)
        self.client.logout()

        regular_user = CommuniqueUser.objects.get(username='regular_user')
        self.assertFalse(regular_user.is_superuser)
        self.client.force_login(regular_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, 'user/login.html')


class CommuniqueUserSearchListViewTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the user search view.
    """
    def test_template(self):
        view_url = reverse('user_communique_user_list_search')
        template_name = 'user/communique_user_list_search.html'
        self.template_test(view_url, template_name)

    def test_context_object(self):
        view_url = reverse('user_communique_user_list_search')
        view_url = view_url + '?q=super'
        context_object_name = 'communique_user_list'
        self.context_object_test(view_url, context_object_name)

    def test_only_superuser_access(self):
        view_url = reverse('user_communique_user_list_search')
        template_name = 'user/communique_user_list_search.html'
        self.only_superuser_access_test(view_url, template_name)

class CommuniqueUserAccessViewsTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the login and logout views.
    """

    def test_login(self):
        """
        Test that login occurs on providing the right credentials.
        """
        self.assertFalse(self.client.login(username='dumb', password='secret'))
        self.assertTrue(self.client.login(username='super_user',
            password='p@55words'))

    def test_login_view_template(self):
        view_url = reverse('user_login')
        template_name = 'user/login.html'
        self.template_test(view_url, template_name)

    def test_logout_view_template(self):
        view_url = reverse('user_logout')
        template_name = 'user/logout.html'
        self.template_test(view_url, template_name)

class CommuniqueUserListViewTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the user list view.
    """

    def test_template(self):
        view_url = reverse('user_communique_user_list')
        template_name = 'user/communique_user_list.html'
        self.template_test(view_url, template_name)

    def test_only_superuser_access(self):
        view_url = reverse('user_communique_user_list')
        template_name = 'user/communique_user_list.html'
        self.only_superuser_access_test(view_url, template_name)

    def test_context_object(self):
        view_url = reverse('user_communique_user_list')
        context_object_name = 'communique_user_list'
        self.context_object_test(view_url, context_object_name)

class CommuniqueUserCreateViewTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the view to create users.
    """

    def test_template(self):
        """
        Tests that the right template is used to render the account create page.
        """
        view_url = reverse('user_communique_user_create')
        template_name = 'user/communique_user_form.html'
        self.template_test(view_url, template_name)

    def test_only_superuser_access(self):
        view_url = reverse('user_communique_user_create')
        template_name = 'user/communique_user_form.html'
        self.only_superuser_access_test(view_url, template_name)

class CommuniqueUserDetailViewTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the view to see user details.
    """

    def test_template(self):
        view_url = reverse('user_communique_user_detail', kwargs={'pk':1})
        template_name = 'user/communique_user_view.html'
        self.template_test(view_url, template_name)

    def test_only_superuser_access(self):
        view_url = reverse('user_communique_user_detail', kwargs={'pk':1})
        template_name = 'user/communique_user_view.html'
        self.only_superuser_access_test(view_url, template_name)

    def test_context_object(self):
        view_url = reverse('user_communique_user_detail', kwargs={'pk':1})
        context_object_name = 'communique_user'
        self.context_object_test(view_url, context_object_name)

class CommuniqueUserUpdateViewTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the view to update user active and superuser status.
    """

    def test_template(self):
        view_url = reverse('user_communique_user_update', kwargs={'pk':1})
        template_name = 'user/communique_user_update_form.html'
        self.template_test(view_url, template_name)

    def test_context_object(self):
        view_url = reverse('user_communique_user_update', kwargs={'pk':1})
        context_object_name = 'communique_user'
        self.context_object_test(view_url, context_object_name)

    def test_only_superuser_access(self):
        view_url = reverse('user_communique_user_update', kwargs={'pk':1})
        template_name = 'user/communique_user_update_form.html'
        self.only_superuser_access_test(view_url, template_name)
