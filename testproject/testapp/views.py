from django.shortcuts import render
from .models import Tenant
from django.shortcuts import render, get_object_or_404

def testapp(request):
    tenants = Tenant.objects.all()
    return render(request , "testapp/testapp.html",{'tenants': tenants})

def tenant_details(request, tenant_id):
  tenant = get_object_or_404(Tenant, pk=tenant_id)
  return render(request, 'testapp/Tenant_detail.html', {'tenant': tenant})