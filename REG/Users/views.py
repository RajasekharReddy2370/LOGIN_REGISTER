from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
print("raja")

from .models import Details
from .serializer import Detailsserializer
def Home(request):
    # return HttpResponse("You are at project index")
    # return render(request,'Home.html',{})
    return render(request,'Homeprac.html',{})

class ALLUSERS(APIView):
    def get(self,request):
        d = Details.objects.all().values()
        ser = Detailsserializer(d,many=True)
        return Response(ser.data)

class users(APIView):
    def get(self, request):
        d = Details.objects.all().values()
        template = loader.get_template('all.html')
        context = {
            "data" :d,
        }
        return HttpResponse(template.render(context,request))


class ONEUSER(APIView):
    def get(self,request,id):
        d = Details.objects.get(id = id)
        ser = Detailsserializer(d)
        return Response(ser.data)
class NEWUSER(APIView):
    def post(self,request):
        ser = Detailsserializer(data = request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

# PATCH for only some fields in the row
# PUT for all the fields in entire row

class UPDATEUSER(APIView):
    def put(self,request,id):
        d = Details.objects.filter(id = id)
        ser = Detailsserializer(instance=d,data = request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

class DELETEUSER(APIView):
    def delete(self,request,id):
        d = Details.objects.filter(id = id)
        d.delete()
        return Response(id,"Deleted Successfully")

class REGISTER(APIView):
    def get(self,request):
        # return redirect('/reg/')
        return render(request,'signup.html',{})
    def post(self,request):
        name = request.data['name']
        email = request.data['email']
        number = request.data['number']
        password = request.data['password']

        if not (name and email and number and password):
            messages.error(request,"ALL THE FIELDS ARE MANDATORY")
            # return Response("All the fields are mandatory")
            return redirect('/reg/')

        if Details.objects.filter(email = email).exists():
            # return Response("Email address already exists")
            messages.error(request,"Email address already exists try another email or go to login ")
            return redirect('/reg/')

        user = Details.objects.create(
            name = name,
            email = email,
            number = number,
            password = password
        )

        user.set_password(password)
        user.save()
        # return user
        # return HttpResponse("User created successfully")
        messages.success(request,"USER CREATED SUCCESSFULLY")
        return redirect('/log/')

class LOGIN(APIView):
    def get(self,request):
        return render(request,'signin.html',{})
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        if not (email and password):
            # return Response("All the fields are mandatory")
            messages.error(request,"ALL THE FIELDS ARE MANDATORY")
            return redirect('/log/')


        user = Details.objects.filter(email = email).first()

        if user is None:
            # return Response("Email address does not exists or incorrect email address")
            messages.error(request,"Email address does not exists try to enter valid email or click register")
            return redirect('/log/')

        if not user.check_password(password):
            # return Response("Invalid password")
            messages.error(request,"Invalid password")
            return redirect('/log/')
        else :
            # return Response("User login success")
            messages.success(request,"Login success")
            return redirect('/db/')

class DASHBOARD(APIView):
    def get(self,request):
        username = request.session.get('username', 'Guest')  # Default to 'Guest' if not logged in

        return render(request,'dashboard.html',{'username':username})

    def post(self,request):
        quantity = request.data['quantity']

        if not quantity:
            messages.error(request,"Quantity is required")
            return redirect('/db/')

        else :
            messages.success(request,"Accept success")











