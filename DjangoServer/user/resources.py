from tastypie.resources import ModelResource
from tastypie import fields
from .models import Profile

class ProfileResource(ModelResource):
	test = fields.CharField()
	class Meta:
		queryset = Profile.objects.all()
		excludes = ['email','password','is_ssuperuser']

		resources_name = 'Profile'