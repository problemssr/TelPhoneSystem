"""TelPhoneSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from api import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('phone/list/', views.phone_list),
    path('phone/<int:nid>/detail/', views.phone_detail),
    path('phone/instructions/', views.phone_instructions),
    path('phone/monthList/', views.one_month_list),
    path('phone/select/', views.select_list),
    path('phone/<int:flag>/download/', views.download),

    path('login/', views.login),
    path('logout/', views.logout),
    path('admin/list/', views.admin_list),

    path('admin/borrow/', views.admin_borrow),
    path('admin/borrow/<int:nid>/detail/', views.admin_borrow_detail),

    path('admin/restore/', views.admin_restore),
    path('admin/restore/<int:nid>/detail/', views.admin_restore_detail),
    path('admin/restore/<int:nid>/delete/', views.delete_restore_detail),

    path('admin/add/', views.admin_add),
    path('admin/edit/', views.admin_edit),
    path('admin/edit/<int:nid>/detail/', views.admin_edit_detail),

    path('admin/histroy/', views.admin_histroy),
    path('admin/manage/', views.admin_manage),
    path('phone/delete/', views.admin_delete),
    path('upload/file/', views.admin_delete),

    path('', views.to_index)
]
