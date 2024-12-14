from django.contrib import admin
from django.urls import path
from estate.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('propertygrid', propertygrid, name='propertygrid'),
    path('propertysearch/', propertysearch, name='propertysearch'),
    path('propertysingle/<int:pid>', propertysingle, name='propertysingle'),
    path('contact/', contact, name='contact'),
    path('signup', signup, name='signup'),
    path('login/', Login, name='login'),
    path('search', search, name='search'),

    # ============================== Owner URL =====================================
    path('owner_login', owner_login, name='owner_login'),
    path('ownerDashboard', ownerDashboard, name='ownerDashboard'),
    path('ownerAbout', ownerAbout, name='ownerAbout'),
    path('ownerPropertygrid', ownerPropertygrid, name='ownerPropertygrid'),
    path('ownerContact', ownerContact, name='ownerContact'),
    path('ownerviewProfile', ownerviewProfile, name='ownerviewProfile'),
    path('owneraddProperty', owneraddProperty, name='owneraddProperty'),
    path('ownermanageProperty', ownermanageProperty, name='ownermanageProperty'),
    path('ownerpropertysearch', ownerpropertysearch, name='ownerpropertysearch'),
    path('ownerpropertysearch/', ownerpropertysearch, name='ownerpropertysearch'),
    path('ownereditProperty/<int:pid>', ownereditProperty, name='ownereditProperty'),
    path('viewPropertyDtls/<int:pid>', viewPropertyDtls, name='viewPropertyDtls'),
    path('ownerreceivedEnquiry', ownerreceivedEnquiry, name='ownerreceivedEnquiry'),
    path('owneranswerEnquiry', owneranswerEnquiry, name='owneranswerEnquiry'),
    path('ownerchangePass', ownerchangePass, name='ownerchangePass'),
    path('load_city',load_city, name="ajax_load_city"),
    path('viewEnquiry/<int:pid>', viewEnquiry, name='viewEnquiry'),



    # ============================== User URL =====================================
    path('user_login', user_login, name='user_login'),
    path('userDashboard', userDashboard, name='userDashboard'),
    path('userabout', userabout, name='userabout'),
    path('userpropertygrid', userpropertygrid, name='userpropertygrid'),
    path('userpropertysearch', userpropertysearch, name='userpropertysearch'),
path('userpropertysearch/', userpropertysearch, name='userpropertysearch'),
    path('userpropertysingle/<int:pid>', userpropertysingle, name='userpropertysingle'),
    path('usercontact', usercontact, name='usercontact'),
    path('viewProfile', viewProfile, name='viewProfile'),
    path('enquiryStatus', enquiryStatus, name='enquiryStatus'),
    path('userviewEnquiry/<int:pid>', userviewEnquiry, name='userviewEnquiry'),
    path('userChangePass', userChangePass, name='userChangePass'),

    # ============================== Admin URL ====================================

    path('admin_login',admin_login,name='admin_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('addProperty', addProperty, name='addProperty'),
    path('manageProperty', manageProperty, name='manageProperty'),
    path('editProperty/<int:pid>', editProperty, name='editProperty'),
    path('deleteProperty/<int:pid>', deleteProperty, name='deleteProperty'),
    path('addState', addState, name='addState'),
    path('manageState', manageState, name='manageState'),
    path('editState/<int:pid>', editState, name='editState'),
    path('deleteState/<int:pid>', deleteState, name='deleteState'),
    path('addCity', addCity, name='addCity'),
    path('manageCity', manageCity, name='manageCity'),
    path('editCity/<int:pid>', editCity, name='editCity'),
    path('deleteCity/<int:pid>', deleteCity, name='deleteCity'),
    path('ownerList', ownerList, name='ownerList'),
    path('deleteOwner/<int:pid>', deleteOwner, name='deleteOwner'),
    path('agentsList', agentsList, name='agentsList'),
    path('deleteAgent/<int:pid>', deleteAgent, name='deleteAgent'),
    path('userList', userList, name='userList'),
    path('deleteUser/<int:pid>', deleteUser, name='deleteUser'),
    path('propertyList', propertyList, name='propertyList'),
    path('viewPropertyDetails/<int:pid>', viewPropertyDetails, name='viewPropertyDetails'),
    path('newReview', newReview, name='newReview'),
    path('approvedReview', approvedReview, name='approvedReview'),
    path('unapprovedReview', unapprovedReview, name='unapprovedReview'),
    path('viewFeedback/<int:pid>', viewFeedback, name='viewFeedback'),
    path('searchProperty', searchProperty, name='searchProperty'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout/', Logout, name='logout')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
