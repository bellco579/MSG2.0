from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.validation import Validation
# from .models import Profile
from authentication.forms import login_form
class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resources_name = 'auth/user'
		excludes = ['email','password','is_ssuperuser']
		# authentication = BasicAuthentication()
		validation = Validation(form_class = login_form)
	# def obj_create(self,bundle, request = None):
	# 	print(bundle)
# class testResource(object):
# 	class Meta:
# 		