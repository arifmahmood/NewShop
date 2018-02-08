"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from WebApp import LoginManagementViews, ItemManagementViews, Ajax, SupplierAndCustomerManagementView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # -----------------alax-----------
    url(r'^ajax/getcurrentitem/$', Ajax.getItem, name='ajax_item'),
    url(r'^ajax/getSC/$', Ajax.getSC, name='ajax_sc'),

    # ------------default  and logout ------------
    url(r'^$', LoginManagementViews.showHomePage, name='login'),
    url(r'^logout/$', LoginManagementViews.logoutView, name='logout'),

    # ----------------- login ----------------------
    url(r'^login/$', LoginManagementViews.showLoginPage, name='login'),
    url(r'^login/auth/$', LoginManagementViews.authenticationMethod, name='auth'),
    url(r'^home/$', LoginManagementViews.showHomePage, name='home'),

    #----------------- item-----------------
    url(r'^item/$',ItemManagementViews.showItemPage,name='item_page'),
    url(r'^item/add/$',ItemManagementViews.showItemAddPage,name='item_add_page'),
    url(r'^item/delete/$',ItemManagementViews.showItemDeletePage,name='item_delete_page'),
    url(r'^item/edit/$',ItemManagementViews.showItemEditPage,name='item_edit_page'),

#-------------------supplier and customer ------------
    url(r'^sc/$', SupplierAndCustomerManagementView.showScPage, name='sc_page'),
    url(r'^sc/add/$', SupplierAndCustomerManagementView.showScAddPage, name='sc_add_page'),
    url(r'^sc/delete/$', SupplierAndCustomerManagementView.showScDeletePage, name='sc_delete_page'),
    url(r'^sc/edit/$',SupplierAndCustomerManagementView.showScEditPage,name='sc_edit_page'),




]
