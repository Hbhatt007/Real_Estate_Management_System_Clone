from django.db.models import Q, Count
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
from datetime import datetime, timedelta, time
import random

def index(request):
    properties = Property.objects.all()
    propType = PropertyType.objects.all()
    citiesss = City.objects.all()
    propstatus = Property.objects.order_by().values('status').distinct()

    error=""
    if request.method=="POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']

        cities = City.objects.get(id=cityid)
        proptype = PropertyType.objects.get(id=typeid)
        searchproperty = Property.objects.filter(type=proptype,status=status,city=cities)
        return render(request, 'search.html', locals())
    return render(request, 'index.html', locals())

def search(request):
    properties = Property.objects.all()
    propType = PropertyType.objects.all()
    citiesss = City.objects.all()
    propstatus = Property.objects.order_by().values('status').distinct()

    if request.method == "POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']

        cities = City.objects.get(id=cityid)
        proptype = PropertyType.objects.get(id=typeid)
        searchproperty = Property.objects.filter(type=proptype, status=status, city=cities)
    return render(request, 'search.html', locals())

def about(request):
    return render(request, 'about.html')

def propertygrid(request):
    propertiestype = Property.objects.all()
    propcity = Property.objects.all()
    properties = Property.objects.all()

    propType = PropertyType.objects.all()
    cities = City.objects.all()
    propstatus = Property.objects.order_by().values('status').distinct()

    error = ""
    if request.method == "POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']

        cities = City.objects.get(id=cityid)
        proptype = PropertyType.objects.get(id=typeid)
        searchproperty = Property.objects.filter(type=proptype, status=status, city=cities)
        return render(request, 'propertysearch.html', locals())
    return render(request, 'propertygrid.html', locals())

def propertysearch(request):
    state = State.objects.all()
    city = City.objects.all()
    properties = Property.objects.filter()
    proptype = PropertyType.objects.all()

    getcity = request.GET.get('city', 0)
    gettype = request.GET.get('type', 0)
    getstate = request.GET.get('state', 0)
    getstatus = request.GET.get('status', 0)

    if request.method == "POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']
        # print(cityid, typeid, status)
        properties = properties.filter(Q(type__id=typeid)&Q(status=status)&Q(city__id=cityid))

    getcity = request.GET.get('city', 0)
    gettype = request.GET.get('type', 0)
    # getstate = request.GET.get('state', 0)
    getstatus = request.GET.get('status', 0)

    if getcity:
        properties = properties.filter(city__id=getcity)
    if gettype:
        properties = properties.filter(type__id=gettype)
    # if getstate:
    #     properties = properties.filter(state__id=getcity)
    if getstatus:
        properties = properties.filter(status=getstatus)
    return render(request, 'propertysearch.html', locals())

def contact(request):
    return render(request, 'contact.html')

def propertysingle(request,pid):
    properties = Property.objects.get(id=pid)
    propertyid = properties.id
    propertystatus = properties.status
    similarproperty = Property.objects.filter(~Q(id=propertyid), status=propertystatus)

    error=""
    try:
        if request.method == "POST":
            fullname = request.POST['fullname']
            emailid = request.POST['emailid']
            mobileno = request.POST['mobileno']
            message = request.POST['message']
            enquiryno = str(random.randint(10000000, 99999999))
            try:
                Enquiry.objects.create(property=properties, fullname=fullname, emailid=emailid, mobileno=mobileno, message=message, enquiryno=enquiryno)
                error = "no"
            except:
                error = "yes"
    except:
        if request.method == "POST":
            saleprice = request.POST['saleprice']
            downpayment = request.POST['downpayment']
            term = request.POST['term']
            interestrate = request.POST['interestrate']

            terminmonth = int(term) * 12
            actualprice = int(saleprice) - int(downpayment)
            interest = float(actualprice) * float(interestrate) / 100
            pricewithinterest = float(actualprice) + float(interest)
            emi = float(pricewithinterest)/ float(terminmonth)
        return render(request, 'calculator.html', locals())
    return render(request, 'propertysingle.html', locals())

def signup(request):
    error = ""
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        emailid = request.POST['emailid']
        password = request.POST['password']
        type = request.POST['type']

        try:
            user = User.objects.create_user(username=emailid, password=password, first_name=firstName, last_name=lastName)
            UserType.objects.create(user=user, type=type)
            error = "no"
        except:
            error = "yes"
    return render(request, 'signup.html', locals())

def Login(request):
    return render(request, 'login.html')

# =============================== Owner View ==========================================
def owner_login(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=e, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'owner_login.html', locals())

def ownerDashboard(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    properties = Property.objects.all()
    propType = PropertyType.objects.all()
    citiesss = City.objects.all()
    propstatus = Property.objects.order_by().values('status').distinct()

    error = ""
    if request.method == "POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']

        cities = City.objects.get(id=cityid)
        proptype = PropertyType.objects.get(id=typeid)
        searchproperty = Property.objects.filter(type=proptype, status=status, city=cities)
        return render(request, 'owner/ownersearch.html', locals())
    return render(request, 'owner/ownerDashboard.html', locals())

def ownerAbout(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')

    return render(request, 'owner/ownerAbout.html')

def ownerPropertygrid(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    properties = Property.objects.all()
    propType = PropertyType.objects.all()
    citiesss = City.objects.all()
    propstatus = Property.objects.order_by().values('status').distinct()

    error = ""
    if request.method == "POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']

        cities = City.objects.get(id=cityid)
        proptype = PropertyType.objects.get(id=typeid)
        searchproperty = Property.objects.filter(type=proptype, status=status, city=cities)
        return render(request, 'owner/ownerpropertysearch.html', locals())
    return render(request, 'owner/ownerPropertygrid.html', locals())


def ownerpropertysearch(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    state = State.objects.all()
    city = City.objects.all()
    properties = Property.objects.filter()
    proptype = PropertyType.objects.all()

    getcity = request.GET.get('city', 0)
    gettype = request.GET.get('type', 0)
    getstate = request.GET.get('state', 0)
    getstatus = request.GET.get('status', 0)

    if request.method == "POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']
        # print(cityid, typeid, status)
        properties = properties.filter(Q(type__id=typeid) & Q(status=status) & Q(city__id=cityid))
    else:
        getcity = request.GET.get('city', 0)
        gettype = request.GET.get('type', 0)
        # getstate = request.GET.get('state', 0)
        getstatus = request.GET.get('status', 0)

        if getcity:
            properties = properties.filter(city__id=getcity)
        if gettype:
            properties = properties.filter(type__id=gettype)
        # if getstate:
        #     properties = properties.filter(state__id=getcity)
        if getstatus:
            properties = properties.filter(status=getstatus)
    return render(request, 'owner/ownerpropertysearch.html', locals())

def ownerContact(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    return render(request, 'owner/ownerContact.html')

def ownerviewProfile(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    user = User.objects.get(id=request.user.id)
    userType = UserType.objects.get(user=user)

    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']

        userType.user.first_name = firstName
        userType.user.last_name = lastName

        try:
            userType.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'owner/ownerviewProfile.html', locals())

def owneraddProperty(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    propertyType = PropertyType.objects.all()
    state = State.objects.all()
    city = City.objects.all()

    user = request.user
    userType = UserType.objects.get(user=user)
    if request.method == "POST":
        proid = request.POST['type']
        typeid = PropertyType.objects.get(id=proid)
        cid = request.POST['city']
        cityid = City.objects.get(id=cid)

        propertytitle = request.POST['propertytitle']
        propertydescription = request.POST['propertydescription']
        status = request.POST['status']
        location = request.POST['location']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        floors = request.POST['floors']
        garages = request.POST['garages']
        area = request.POST['area']
        size = request.POST['size']
        rentorsaleprice = request.POST['rentorsaleprice']
        beforepricelabel = request.POST['beforepricelabel']
        afterpricelabel = request.POST['afterpricelabel']
        propertyid = str(random.randint(10000000, 99999999))

        if 'centercooling' in request.POST:
            centercooling = request.POST['centercooling']
        else:
            centercooling = "no"

        if 'balcony' in request.POST:
            balcony = request.POST['balcony']
        else:
            balcony = "no"

        if 'petfriendly' in request.POST:
            petfriendly = request.POST['petfriendly']
        else:
            petfriendly = "no"

        if 'barbeque' in request.POST:
            barbeque = request.POST['barbeque']
        else:
            barbeque = "no"

        if 'firealarm' in request.POST:
            firealarm = request.POST['firealarm']
        else:
            firealarm = "no"

        if 'modernkitchen' in request.POST:
            modernkitchen = request.POST['modernkitchen']
        else:
            modernkitchen = "no"

        if 'storage' in request.POST:
            storage = request.POST['storage']
        else:
            storage = "no"

        if 'dryer' in request.POST:
            dryer = request.POST['dryer']
        else:
            dryer = "no"

        if 'heating' in request.POST:
            heating = request.POST['heating']
        else:
            heating = "no"

        if 'pool' in request.POST:
            pool = request.POST['pool']
        else:
            pool = "no"

        if 'laundry' in request.POST:
            laundry = request.POST['laundry']
        else:
            laundry = "no"

        if 'sauna' in request.POST:
            sauna = request.POST['sauna']
        else:
            sauna = "no"

        if 'gym' in request.POST:
            gym = request.POST['gym']
        else:
            gym = "no"

        if 'elevator' in request.POST:
            elevator = request.POST['elevator']
        else:
            elevator = "no"

        if 'dishwasher' in request.POST:
            dishwasher = request.POST['dishwasher']
        else:
            dishwasher = "no"

        if 'emergencyexit' in request.POST:
            emergencyexit = request.POST['emergencyexit']
        else:
            emergencyexit = "no"

        featuredimage = request.FILES['featuredimage']
        galleryimage1 = request.FILES['galleryimage1']
        galleryimage2 = request.FILES['galleryimage2']
        galleryimage3 = request.FILES['galleryimage3']
        galleryimage4 = request.FILES['galleryimage4']
        galleryimage5 = request.FILES['galleryimage5']
        address = request.POST['address']
        zipcode = request.POST['zipcode']
        neighborhood = request.POST['neighborhood']

        try:
            Property.objects.create(user=userType, type=typeid, city=cityid, propertytitle=propertytitle, propertydescription=propertydescription, status=status,
                                    location=location, bedrooms=bedrooms, bathrooms=bathrooms, floors=floors, garages=garages, area=area, size=size,
                                    rentorsaleprice=rentorsaleprice, beforepricelabel=beforepricelabel, afterpricelabel=afterpricelabel, propertyid=propertyid, centercooling=centercooling,
                                    balcony=balcony, petfriendly=petfriendly, barbeque=barbeque, firealarm=firealarm, modernkitchen=modernkitchen, storage=storage, dryer=dryer,
                                    heating=heating, pool=pool, laundry=laundry, sauna=sauna, gym=gym, elevator=elevator, dishwasher=dishwasher, emergencyexit=emergencyexit,
                                    featuredimage=featuredimage, galleryimage1=galleryimage1, galleryimage2=galleryimage2, galleryimage3=galleryimage3, galleryimage4=galleryimage4,
                                    galleryimage5=galleryimage5, address=address, zipcode=zipcode, neighborhood=neighborhood)
            error = "no"
        except:
            error = "yes"
    return render(request, 'owner/owneraddProperty.html', locals())

def load_city(request):
    stateid = request.GET.get('state')
    city = City.objects.filter(state=stateid).order_by('cityname')
    return render(request, 'owner/city_dropdown_list_options.html', locals())

def ownermanageProperty(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    user = request.user
    userType = UserType.objects.get(user=user)
    properties = Property.objects.filter(user=userType)
    return render(request, 'owner/ownermanageProperty.html', locals())

def ownereditProperty(request,pid):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    propertyType = PropertyType.objects.all()
    state = State.objects.all()
    city = City.objects.all()

    user = request.user
    userType = UserType.objects.get(user=user)

    properties = Property.objects.get(id=pid)

    if request.method == "POST":
        proid = request.POST['type']
        typeid = PropertyType.objects.get(id=proid)
        cid = request.POST['city']
        cityid = City.objects.get(id=cid)

        propertytitle = request.POST['propertytitle']
        propertydescription = request.POST['propertydescription']
        status = request.POST['status']
        location = request.POST['location']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        floors = request.POST['floors']
        garages = request.POST['garages']
        area = request.POST['area']
        size = request.POST['size']
        rentorsaleprice = request.POST['rentorsaleprice']
        beforepricelabel = request.POST['beforepricelabel']
        afterpricelabel = request.POST['afterpricelabel']

        if 'centercooling' in request.POST:
            centercooling = request.POST['centercooling']
        else:
            centercooling = "no"

        if 'balcony' in request.POST:
            balcony = request.POST['balcony']
        else:
            balcony = "no"

        if 'petfriendly' in request.POST:
            petfriendly = request.POST['petfriendly']
        else:
            petfriendly = "no"

        if 'barbeque' in request.POST:
            barbeque = request.POST['barbeque']
        else:
            barbeque = "no"

        if 'firealarm' in request.POST:
            firealarm = request.POST['firealarm']
        else:
            firealarm = "no"

        if 'modernkitchen' in request.POST:
            modernkitchen = request.POST['modernkitchen']
        else:
            modernkitchen = "no"

        if 'storage' in request.POST:
            storage = request.POST['storage']
        else:
            storage = "no"

        if 'dryer' in request.POST:
            dryer = request.POST['dryer']
        else:
            dryer = "no"

        if 'heating' in request.POST:
            heating = request.POST['heating']
        else:
            heating = "no"

        if 'pool' in request.POST:
            pool = request.POST['pool']
        else:
            pool = "no"

        if 'laundry' in request.POST:
            laundry = request.POST['laundry']
        else:
            laundry = "no"

        if 'sauna' in request.POST:
            sauna = request.POST['sauna']
        else:
            sauna = "no"

        if 'gym' in request.POST:
            gym = request.POST['gym']
        else:
            gym = "no"

        if 'elevator' in request.POST:
            elevator = request.POST['elevator']
        else:
            elevator = "no"

        if 'dishwasher' in request.POST:
            dishwasher = request.POST['dishwasher']
        else:
            dishwasher = "no"

        if 'emergencyexit' in request.POST:
            emergencyexit = request.POST['emergencyexit']
        else:
            emergencyexit = "no"

        properties.type = typeid
        properties.city = cityid
        properties.propertytitle = propertytitle
        properties.propertydescription = propertydescription
        properties.status = status
        properties.location = location
        properties.bedrooms = bedrooms
        properties.bathrooms = bathrooms
        properties.floors = floors
        properties.garages = garages
        properties.area = area
        properties.size = size
        properties.rentorsaleprice = rentorsaleprice
        properties.beforepricelabel = beforepricelabel
        properties.afterpricelabel = afterpricelabel
        properties.centercooling = centercooling
        properties.balcony = balcony
        properties.petfriendly = petfriendly
        properties.barbeque = barbeque
        properties.firealarm = firealarm
        properties.modernkitchen = modernkitchen
        properties.storage = storage
        properties.dryer = dryer
        properties.heating = heating
        properties.pool = pool
        properties.laundry = laundry
        properties.sauna = sauna
        properties.gym = gym
        properties.elevator = elevator
        properties.dishwasher = dishwasher
        properties.emergencyexit = emergencyexit

        try:
            properties.save()
            error = "no"
        except:
            error = "yes"

        try:
            featuredimage = request.FILES['featuredimage']
            properties.featuredimage = featuredimage
            properties.save()
        except:
            pass

        try:
            galleryimage1 = request.FILES['galleryimage1']
            properties.galleryimage1 = galleryimage1
            properties.save()
        except:
            pass

        try:
            galleryimage2 = request.FILES['galleryimage2']
            properties.galleryimage2 = galleryimage2
            properties.save()
        except:
            pass

        try:
            galleryimage3 = request.FILES['galleryimage3']
            properties.galleryimage3 = galleryimage3
            properties.save()
        except:
            pass

        try:
            galleryimage4 = request.FILES['galleryimage4']
            properties.galleryimage4 = galleryimage4
            properties.save()
        except:
            pass

        try:
            galleryimage5 = request.FILES['galleryimage5']
            properties.galleryimage5 = galleryimage5
            properties.save()
        except:
            pass
    return render(request, 'owner/ownereditProperty.html', locals())

def viewPropertyDtls(request, pid):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    properties = Property.objects.get(id=pid)

    propertyid = properties.id
    propertystatus = properties.status
    similarproperty = Property.objects.filter(~Q(id=propertyid), status=propertystatus)

    error = ""
    try:
        if request.method == "POST":
            fullname = request.POST['fullname']
            emailid = request.POST['emailid']
            mobileno = request.POST['mobileno']
            message = request.POST['message']
            enquiryno = str(random.randint(10000000, 99999999))
            try:
                Enquiry.objects.create(property=properties, fullname=fullname, emailid=emailid, mobileno=mobileno,
                                       message=message, enquiryno=enquiryno)
                error = "no"
            except:
                error = "yes"
    except:
        if request.method == "POST":
            saleprice = request.POST['saleprice']
            downpayment = request.POST['downpayment']
            term = request.POST['term']
            interestrate = request.POST['interestrate']

            terminmonth = int(term) * 12
            actualprice = int(saleprice) - int(downpayment)
            interest = float(actualprice) * float(interestrate) / 100
            pricewithinterest = float(actualprice) + float(interest)
            emi = float(pricewithinterest) / float(terminmonth)
        return render(request, 'owner/calculator.html', locals())
    return render(request, 'owner/viewPropertyDtls.html', locals())

def ownerreceivedEnquiry(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    user = User.objects.get(id=request.user.id)
    userType = UserType.objects.get(user=user)

    properties = Property.objects.filter(user=userType)
    propenquiry = Enquiry.objects.filter(property__in=properties, status__isnull=True)
    return render(request, 'owner/ownerreceivedEnquiry.html', locals())

def owneranswerEnquiry(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    user = User.objects.get(id=request.user.id)
    userType = UserType.objects.get(user=user)

    properties = Property.objects.filter(user=userType)
    propenquiry = Enquiry.objects.filter(property__in=properties, status='Answer')
    return render(request, 'owner/owneranswerEnquiry.html', locals())

def viewEnquiry(request,pid):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    enquiry = Enquiry.objects.get(id=pid)

    error = ""
    if request.method == "POST":
        remark = request.POST['remark']

        enquiry.remark = remark
        enquiry.status = "Answer"
        enquiry.remarkdate = date.today()

        try:
            enquiry.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'owner/viewEnquiry.html', locals())

def ownerchangePass(request):
    if not request.user.is_authenticated:
        return redirect('owner_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'owner/ownerchangePass.html', locals())



# =============================== User View ==========================================

def user_login(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=e, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'user_login.html', locals())

def userDashboard(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    properties = Property.objects.all()
    propType = PropertyType.objects.all()
    citiesss = City.objects.all()
    propstatus = Property.objects.order_by().values('status').distinct()

    error = ""
    if request.method == "POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']

        cities = City.objects.get(id=cityid)
        proptype = PropertyType.objects.get(id=typeid)
        searchproperty = Property.objects.filter(type=proptype, status=status, city=cities)
        return render(request, 'user/usersearch.html', locals())
    return render(request, 'user/userDashboard.html', locals())

def userabout(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user/userabout.html')

def userpropertygrid(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    properties = Property.objects.all()
    propType = PropertyType.objects.all()
    citiesss = City.objects.all()
    propstatus = Property.objects.order_by().values('status').distinct()

    error = ""
    if request.method == "POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']

        cities = City.objects.get(id=cityid)
        proptype = PropertyType.objects.get(id=typeid)
        searchproperty = Property.objects.filter(type=proptype, status=status, city=cities)
        return render(request, 'user/userpropertysearch.html', locals())
    return render(request, 'user/userpropertygrid.html', locals())

def userpropertysearch(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    state = State.objects.all()
    city = City.objects.all()
    properties = Property.objects.filter()
    proptype = PropertyType.objects.all()

    getcity = request.GET.get('city', 0)
    gettype = request.GET.get('type', 0)
    getstate = request.GET.get('state', 0)
    getstatus = request.GET.get('status', 0)

    if request.method == "POST":
        cityid = request.POST['city']
        typeid = request.POST['type']
        status = request.POST['status']
        # print(cityid, typeid, status)
        properties = properties.filter(Q(type__id=typeid) & Q(status=status) & Q(city__id=cityid))
    else:
        getcity = request.GET.get('city', 0)
        gettype = request.GET.get('type', 0)
        # getstate = request.GET.get('state', 0)
        getstatus = request.GET.get('status', 0)

        if getcity:
            properties = properties.filter(city__id=getcity)
        if gettype:
            properties = properties.filter(type__id=gettype)
        # if getstate:
        #     properties = properties.filter(state__id=getcity)
        if getstatus:
            properties = properties.filter(status=getstatus)
    return render(request, 'user/userpropertysearch.html', locals())

def userpropertysingle(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    userType = UserType.objects.get(user=user)

    properties = Property.objects.get(id=pid)

    error = ""
    try:
        if request.method == "POST":
            fullname = request.POST['fullname']
            emailid = request.POST['emailid']
            mobileno = request.POST['mobileno']
            message = request.POST['message']
            enquiryno = str(random.randint(10000000, 99999999))
            try:
                Enquiry.objects.create(property=properties, fullname=fullname, emailid=emailid, mobileno=mobileno,
                                       message=message, enquiryno=enquiryno)
                error = "no"
            except:
                error = "yes"
    except:
        try:
            if request.method == "POST":
                saleprice = request.POST['saleprice']
                downpayment = request.POST['downpayment']
                term = request.POST['term']
                interestrate = request.POST['interestrate']

                terminmonth = int(term) * 12
                actualprice = int(saleprice) - int(downpayment)
                interest = float(actualprice) * float(interestrate) / 100
                pricewithinterest = float(actualprice) + float(interest)
                emi = float(pricewithinterest) / float(terminmonth)
            return render(request, 'user/usercalculator.html', locals())
        except:
            if request.method == "POST":
                userremark = request.POST['userremark']

                try:
                    Feedback.objects.create(user=userType, property=properties, userremark=userremark)
                    error1 = "no"
                except:
                    error1 = "yes"
    return render(request, 'user/userpropertysingle.html', locals())

def usercontact(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user/usercontact.html')

def viewProfile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    userType = UserType.objects.get(user=user)

    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']

        userType.user.first_name = firstName
        userType.user.last_name = lastName

        try:
            userType.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'user/viewProfile.html', locals())

def enquiryStatus(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    userType = UserType.objects.get(user=user)
    useremail = user.username
    enquiry = Enquiry.objects.filter(status__isnull=True,emailid=useremail)
    return render(request, 'user/enquiryStatus.html', locals())

def userviewEnquiry(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    enquiry = Enquiry.objects.get(id=pid)
    return render(request, 'user/userviewEnquiry.html', locals())

def userChangePass(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'user/userChangePass.html', locals())


# =============================== Admin View ==========================================
def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html',locals())

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    allproperty = PropertyType.objects.all().count()
    allstate = State.objects.all().count()
    allcity = City.objects.all().count()
    allproperty = Property.objects.all().count()
    alluser = UserType.objects.filter(type='User').count()
    allowner = UserType.objects.filter(type='Owner').count()
    allbroker = UserType.objects.filter(type='Broker').count()
    return render(request, 'admin/dashboard.html', locals())

def addProperty(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        typename = request.POST['typename']

        try:
            propertyType = PropertyType.objects.create(typename=typename)
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/addProperty.html', locals())

def manageProperty(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    propertyType = PropertyType.objects.all()
    return render(request, 'admin/manageProperty.html', locals())

def editProperty(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    propertyType = PropertyType.objects.get(id=pid)
    if request.method == "POST":
        typename = request.POST['typename']

        propertyType.typename = typename

        try:
            propertyType.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/editProperty.html', locals())

def deleteProperty(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    propertyType = PropertyType.objects.get(id=pid)
    propertyType.delete()
    return redirect('manageProperty')


def addState(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        statename = request.POST['statename']

        try:
            state = State.objects.create(statename=statename)
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/addState.html', locals())

def manageState(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    state = State.objects.all()
    return render(request, 'admin/manageState.html', locals())

def editState(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    state = State.objects.get(id=pid)
    if request.method == "POST":
        statename = request.POST['statename']

        state.statename = statename

        try:
            state.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/editState.html', locals())

def deleteState(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    state = State.objects.get(id=pid)
    state.delete()
    return redirect('manageState')

def addCity(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    state = State.objects.all()
    if request.method == "POST":
        sid = request.POST['state']
        stateid = State.objects.get(id=sid)
        cityname = request.POST['cityname']

        try:
            City.objects.create(state=stateid, cityname=cityname)
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/addCity.html', locals())

def manageCity(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    city = City.objects.all()
    return render(request, 'admin/manageCity.html', locals())

def editCity(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    state = State.objects.all()
    city = City.objects.get(id=pid)
    if request.method == "POST":
        sid = request.POST['state']
        state1 = State.objects.get(id=sid)
        cityname = request.POST['cityname']

        city.state = state1
        city.cityname = cityname

        try:
            city.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/editCity.html', locals())

def deleteCity(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    city = City.objects.get(id=pid)
    city.delete()
    return redirect('manageCity')

def ownerList(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userType = UserType.objects.filter(type="Owner")
    return render(request, 'admin/ownerList.html', locals())

def deleteOwner(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    User.objects.get(id=pid).delete()
    return redirect('ownerList')

def agentsList(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userType = UserType.objects.filter(type="Broker")
    return render(request, 'admin/agentsList.html', locals())

def deleteAgent(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    User.objects.get(id=pid).delete()
    return redirect('agentsList')

def userList(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userType = UserType.objects.filter(type="User")
    return render(request, 'admin/userList.html', locals())

def deleteUser(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    User.objects.get(id=pid).delete()
    return redirect('userList')

def propertyList(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    property = Property.objects.all()
    return render(request, 'admin/propertyList.html', locals())

def viewPropertyDetails(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    property = Property.objects.get(id=pid)
    return render(request, 'admin/viewPropertyDetails.html', locals())


def newReview(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    feedback = Feedback.objects.filter(ispublish__isnull=True)
    return render(request, 'admin/newReview.html', locals())

def approvedReview(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    feedback = Feedback.objects.filter(ispublish='Approved')
    return render(request, 'admin/approvedReview.html', locals())

def unapprovedReview(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    feedback = Feedback.objects.filter(ispublish='Unapproved')
    return render(request, 'admin/unapprovedReview.html', locals())

def viewFeedback(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    feedback = Feedback.objects.get(id=pid)

    if request.method == "POST":
        ispublish = request.POST['ispublish']

        feedback.ispublish = ispublish

        try:
            feedback.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/viewFeedback.html', locals())

def searchProperty(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        try:
            users = [i.id for i in User.objects.filter(Q(first_name__icontains=sd) | Q(last_name__icontains=sd))]
            user1 = UserType.objects.filter(Q(user__in=users))
            properties = Property.objects.filter(Q(user__in=user1) | Q(propertyid=sd))
        except:
            properties = ""

    return render(request, 'admin/searchProperty.html', locals())

def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'admin/changePassword.html', locals())

def Logout(request):
    logout(request)
    return redirect('index')

