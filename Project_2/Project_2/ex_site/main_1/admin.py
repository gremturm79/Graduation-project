from django.contrib import admin
from .models import PhotoOfWorks, TypeOfServices, CalculateTableEx, ListOfWorks,\
    ContactOfOrganization,ProfileUser, Review, Company, SummOfWorks, PricingAndSummWorks


admin.site.register(PhotoOfWorks)
admin.site.register(TypeOfServices)
admin.site.register(CalculateTableEx)
admin.site.register(ListOfWorks)
admin.site.register(ContactOfOrganization)
admin.site.register(ProfileUser)
admin.site.register(Review)
admin.site.register(Company)
admin.site.register(SummOfWorks)
admin.site.register(PricingAndSummWorks)
