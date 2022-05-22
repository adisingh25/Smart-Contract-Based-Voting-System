import uuid

# views.py
from django.contrib import messages
from django.shortcuts import redirect,HttpResponseRedirect
from django.shortcuts import render

from . import models
from . import vote
from .sendsms import sendsms


def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

def home(request):

    if request.method=='POST':
        name2 = request.POST['name2']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        feedback = request.POST['feedback']
        ins = models.Feedback(name2=name2, email=email, phonenumber=phonenumber, feedback=feedback)
        ins.save()

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')


def candidateudma(request):
    allTasks = models.Candidateudma.objects.all()
    context = {'task': allTasks}
    return render(request,'candidateudma.html',context)

def candidateaura(request):
    allTasks = models.Candidateaura.objects.all()
    context = {'task': allTasks}
    return render(request,'candidateaura.html',context)

def candidatepalg(request):
    allTasks = models.Candidatepalg.objects.all()
    context = {'task': allTasks}
    return render(request,'candidatepalg.html',context)


def udma(request):
    success = False
    x=1
    # global uniqueid
    # uniqueid=""
    context = {'success': success, 'uid': x}
    print(success)
    if request.method == "POST":
        if request.POST.get('name3'):
            # global uniqueid
            uniqueid = str(request.POST['name3'])

            address = request.POST['address3']
            phonenumber = request.POST['phonenumber3']
            email = request.POST['email3']
            alluid = models.UIDudma.objects.get(uniqueid=uniqueid)
            pannumber = alluid.pannumber
            allobjects = models.Voterregisteredudma.objects.get(pannumber=pannumber)
            name = allobjects.name
            age = allobjects.age
            ins = models.Voterregisteredudma(name=name, age=age, address=address, pannumber=pannumber, email=email,
                                               phonenumber=phonenumber)

            ins2 = models.Voterregisteredudma.objects.get(pannumber=pannumber)
            ins2.delete()
            ins.save()



        if request.POST.get('name'):
            print("yesss")
            name = request.POST['name']
            age = int(request.POST['age'])
            address = request.POST['address']
            pannumber = request.POST['pannumber']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            constituency = "Udma"
            allTasks = models.Votergovt.objects.all()
            x = str(uuid.uuid1())
            while models.UIDudma.objects.filter(uniqueid=x):
                x = str(uuid.uuid1())
            x = str(x[0:10])
            # send_mail(
            #     'UID Generated for evoting',
            #     x,
            #     'noreplyvamp@yahoo.com',
            #     [email],
            #     fail_silently=False,
            # )

            ins2 = models.UIDudma(pannumber=pannumber, uniqueid=x)
            ins = models.Voterregisteredudma(name=name, age=age, address=address, pannumber=pannumber, email=email,phonenumber=phonenumber)
            if (models.Votergovt.objects.filter(name=name, pannumber=pannumber,constituency=constituency,age=age).exists())and (not models.Voterregisteredudma.objects.filter(name=name,pannumber=pannumber).exists())and(age>=18):
                ins.save()
                sendsms(x)
                success = True
                ins2.save()
                vote.abcd()
                vote.vote(name,age,pannumber,x)
                # y = "+91" + str(phonenumber)
                # sendsms(mess=x, ph=y)
                context = {'success': success, 'uid': x}
            elif not(models.Votergovt.objects.filter(name=name, pannumber=pannumber, constituency=constituency,age=age).exists()) or (models.Voterregisteredudma.objects.filter(name=name, pannumber=pannumber).exists()) and (age >= 18):
                message='Incorrect Name or Age or PAN Number'
                context={'messages':'You have entered something wrong , please check the entered credentials','m1':'wrong name','m2':'wrong age','m3':'wrong PAN Number'}

        if request.POST.get('uid'):
            print('form 2')
            # global uniqueid
            uniqueid=str(request.POST['uid'])
            pannumber=str(request.POST['pan'])
            if models.UIDudma.objects.filter(uniqueid=uniqueid,pannumber=pannumber).exists():
                print("Yes you are on correct page")
                allTasks = models.Candidateudma.objects.all()
                context={'task':allTasks}
                # return render(request, 'votepalg.html', context)
            # if request.POST.get('pannumber1'):
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     print("YES YES YES YES")
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     vote.Voting1(uniqueid)
            #
            # if request.POST.get('pannumber2'):
            #     vote.Voting2(uniqueid)
            # if request.POST.get('VOTE 3'):
            #     vote.Voting3(uniqueid)
            # return render(request,'votepalg.html',context)

            return redirect('votehere/')
        # else:
        #     messages.success(request,'Incorrect UID or PAN Number')
        #
        #     return redirect('home')
        # def getid():
        #     return uniqueid

    return render(request,'udma.html',context)



def amroha(request):
    success = False
    x=1
    # global uniqueid
    # uniqueid=""
    context = {'success': success, 'uid': x}
    print(success)
    if request.method == "POST":
        if request.POST.get('name3'):
            # global uniqueid
            uniqueid = str(request.POST['name3'])

            address = request.POST['address3']
            phonenumber = request.POST['phonenumber3']
            email = request.POST['email3']
            alluid = models.UIDamroha.objects.get(uniqueid=uniqueid)
            pannumber = alluid.pannumber
            allobjects = models.Voterregisteredamroha.objects.get(pannumber=pannumber)
            name = allobjects.name
            age = allobjects.age
            ins = models.Voterregisteredamroha(name=name, age=age, address=address, pannumber=pannumber, email=email,
                                               phonenumber=phonenumber)

            ins2 = models.Voterregisteredamroha.objects.get(pannumber=pannumber)
            ins2.delete()
            ins.save()



        if request.POST.get('name'):
            print("yesss")
            name = request.POST['name']
            age = int(request.POST['age'])
            address = request.POST['address']
            pannumber = request.POST['pannumber']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            constituency = "Amroha"
            allTasks = models.Votergovt.objects.all()
            x = str(uuid.uuid1())
            while models.UIDamroha.objects.filter(uniqueid=x):
                x = str(uuid.uuid1())
            x = str(x[0:10])
            # send_mail(
            #     'UID Generated for evoting',
            #     x,
            #     'noreplyvamp@yahoo.com',
            #     [email],
            #     fail_silently=False,
            # )

            ins2 = models.UIDamroha(pannumber=pannumber, uniqueid=x)
            ins = models.Voterregisteredamroha(name=name, age=age, address=address, pannumber=pannumber, email=email,phonenumber=phonenumber)
            if (models.Votergovt.objects.filter(name=name, pannumber=pannumber,constituency=constituency,age=age).exists())and (not models.Voterregisteredamroha.objects.filter(name=name,pannumber=pannumber).exists())and(age>=18):
                ins.save()
                # sendsms(x)
                success = True
                ins2.save()
                vote.abcd()
                vote.vote(name,age,pannumber,x)
                # y = "+91" + str(phonenumber)
                # sendsms(mess=x, ph=y)
                context = {'success': success, 'uid': x}


            elif not (models.Votergovt.objects.filter(name=name, pannumber=pannumber, constituency=constituency,age=age).exists()) or (models.Voterregisteredamroha.objects.filter(name=name, pannumber=pannumber).exists()) and (age >= 18):

                message = 'Incorrect Name or Age or PAN Number'

                context = {'messages': 'You have entered something wrong , please check the entered credentials','m1': 'wrong name', 'm2': 'wrong age', 'm3': 'wrong PAN Number'}

        if request.POST.get('uid'):
            print('form 2')
            # global uniqueid
            uniqueid=str(request.POST['uid'])
            pannumber=str(request.POST['pan'])
            if models.UIDamroha.objects.filter(uniqueid=uniqueid,pannumber=pannumber).exists():
                print("Yes you are on correct page")
                allTasks = models.Candidateaura.objects.all()
                context={'task':allTasks}
                # return render(request, 'votepalg.html', context)
            # if request.POST.get('pannumber1'):
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     print("YES YES YES YES")
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     vote.Voting1(uniqueid)
            #
            # if request.POST.get('pannumber2'):
            #     vote.Voting2(uniqueid)
            # if request.POST.get('VOTE 3'):
            #     vote.Voting3(uniqueid)
            # return render(request,'votepalg.html',context)
            return redirect('votehere/')
        # def getid():
        #     return uniqueid

    return render(request,'amroha.html',context)

# context = {'success': 'success', 'uid': 'x'}
# global uniqueid
def palghar(request):
    success = False
    x=''
    # global uniqueid
    # uniqueid=""
    context = {'success': success, 'uid': x}
    print(success)
    if request.method == "POST":
        if request.POST.get('name3'):
            # global uniqueid
            uniqueid = str(request.POST['name3'])

            address = request.POST['address3']
            phonenumber = request.POST['phonenumber3']
            email = request.POST['email3']
            alluid = models.UIDpalghar.objects.get(uniqueid=uniqueid)
            pannumber = alluid.pannumber
            allobjects = models.Voterregisteredpalghar.objects.get(pannumber=pannumber)
            name = allobjects.name
            age = allobjects.age
            ins = models.Voterregisteredpalghar(name=name, age=age, address=address, pannumber=pannumber, email=email,
                                               phonenumber=phonenumber)

            ins2 = models.Voterregisteredpalghar.objects.get(pannumber=pannumber)
            ins2.delete()
            ins.save()



        if request.POST.get('name'):
            print("yesss")
            name = request.POST['name']
            age = int(request.POST['age'])
            address = request.POST['address']
            pannumber = request.POST['pannumber']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            constituency = "Palghar"
            allTasks = models.Votergovt.objects.all()
            x = str(uuid.uuid1())
            while models.UIDpalghar.objects.filter(uniqueid=x):
                x = str(uuid.uuid1())
            x = str(x[0:10])
            # send_mail(
            #     'UID Generated for evoting',
            #     x,
            #     'noreplyvamp@yahoo.com',
            #     [email],
            #     fail_silently=False,
            # )

            ins2 = models.UIDpalghar(pannumber=pannumber, uniqueid=x)
            ins = models.Voterregisteredpalghar(name=name, age=age, address=address, pannumber=pannumber, email=email,phonenumber=phonenumber)
            if (models.Votergovt.objects.filter(name=name, pannumber=pannumber,constituency=constituency,age=age).exists())and (not models.Voterregisteredpalghar.objects.filter(name=name,pannumber=pannumber).exists())and(age>=18):
                ins.save()
                # sendsms(x)
                success = True
                ins2.save()
                vote.abcd()
                vote.vote(name,age,pannumber,x)
                # y = "+91" + str(phonenumber)
                # sendsms(mess=x, ph=y)
                context = {'success': success, 'uid': x}
            elif not (models.Votergovt.objects.filter(name=name, pannumber=pannumber, constituency=constituency,age=age).exists()) or (models.Voterregisteredpalghar.objects.filter(name=name, pannumber=pannumber).exists()) and (age >= 18):
                message = 'Incorrect Name or Age or PAN Number'
                context = {'messages': 'You have entered something wrong , please check the entered credentials','m1': 'wrong name', 'm2': 'wrong age', 'm3': 'wrong PAN Number'}

        if request.POST.get('uid'):
            print('form 2')
            # global uniqueid
            uniqueid=str(request.POST['uid'])
            pannumber=str(request.POST['pan'])
            if models.UIDpalghar.objects.filter(uniqueid=uniqueid,pannumber=pannumber).exists():
                print("Yes you are on correct page")
                allTasks = models.Candidatepalg.objects.all()
                context={'task':allTasks}
                # return render(request, 'votepalg.html', context)
            # if request.POST.get('pannumber1'):
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     print("YES YES YES YES")
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     vote.Voting1(uniqueid)
            #
            # if request.POST.get('pannumber2'):
            #     vote.Voting2(uniqueid)
            # if request.POST.get('VOTE 3'):
            #     vote.Voting3(uniqueid)
            # return render(request,'votepalg.html',context)
            return redirect('votehere/')
        # def getid():
        #     return uniqueid

    return render(request,'palghar.html',context)


def voteudma(request):
    allTasks = models.Candidateudma.objects.all()
    context = {'task': allTasks}
    # if request.method=='POST':
    #     if request.POST.get('VOTE 1'):
    #         print("*************")
    #         print("*************")
    #         print("*************")
    #
    #         # uniqueid=request.POST['uniqueid1']
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         #
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #     if request.POST.get('VOTE 2'):
    #         print("2222222222222")
    #         print("2222222222222")
    #         print("2222222222222")
    #         # uniqueid = request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #
    #     if request.POST.get('VOTE 3'):
    #         pass
    #         # uniqueid=request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    if request.method=="POST":
        if request.POST.get('UID1'):
            uid1 = request.POST['UID1']
            if models.UIDudma.objects.filter(uniqueid=uid1).exists():

                vote.Voting1u(uid1)
                return render(request, 'success.html')
        if request.POST.get('UID2'):
            uid2 = request.POST['UID2']
            if models.UIDudma.objects.filter(uniqueid=uid2).exists():

                vote.Voting2u(uid2)
                return render(request, 'success.html')
        if request.POST.get('UID3'):
            uid3 = request.POST['UID3']

            if models.UIDudma.objects.filter(uniqueid=uid3).exists():
                vote.Voting3u(uid3)
                return render(request,'success.html')
    return render(request,'voteudma.html',context)



def votepalghar(request):
    allTasks = models.Candidatepalg.objects.all()
    context = {'task': allTasks}
    # if request.method=='POST':
    #     if request.POST.get('VOTE 1'):
    #         print("*************")
    #         print("*************")
    #         print("*************")
    #
    #         # uniqueid=request.POST['uniqueid1']
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         #
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #     if request.POST.get('VOTE 2'):
    #         print("2222222222222")
    #         print("2222222222222")
    #         print("2222222222222")
    #         # uniqueid = request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #
    #     if request.POST.get('VOTE 3'):
    #         pass
    #         # uniqueid=request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    if request.method=="POST":
        if request.POST.get('UID1'):
            uid1 = request.POST['UID1']
            if models.UIDpalghar.objects.filter(uniqueid=uid1).exists():

                vote.Voting1(uid1)
                return render(request, 'success.html')
        if request.POST.get('UID2'):
            uid2 = request.POST['UID2']
            if models.UIDpalghar.objects.filter(uniqueid=uid2).exists():

                vote.Voting2(uid2)
                return render(request, 'success.html')
        if request.POST.get('UID3'):
            uid3 = request.POST['UID3']

            if models.UIDpalghar.objects.filter(uniqueid=uid3).exists():
                vote.Voting3(uid3)

                return render(request, 'success.html')
    return render(request,'votepalg.html',context)


def voteamroha(request):
    allTasks = models.Candidateaura.objects.all()
    context = {'task': allTasks}
    # if request.method=='POST':
    #     if request.POST.get('VOTE 1'):
    #         print("*************")
    #         print("*************")
    #         print("*************")
    #
    #         # uniqueid=request.POST['uniqueid1']
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         #
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #     if request.POST.get('VOTE 2'):
    #         print("2222222222222")
    #         print("2222222222222")
    #         print("2222222222222")
    #         # uniqueid = request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #
    #     if request.POST.get('VOTE 3'):
    #         pass
    #         # uniqueid=request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    if request.method=="POST":
        if request.POST.get('UID1'):
            uid1 = request.POST['UID1']
            if models.UIDamroha.objects.filter(uniqueid=uid1).exists():

                vote.Voting1a(uid1)

                return render(request, 'success.html')
        if request.POST.get('UID2'):
            uid2 = request.POST['UID2']
            if models.UIDamroha.objects.filter(uniqueid=uid2).exists():

                vote.Voting2a(uid2)

                return render(request, 'success.html')
        if request.POST.get('UID3'):
            uid3 = request.POST['UID3']

            if models.UIDamroha.objects.filter(uniqueid=uid3).exists():
                vote.Voting3a(uid3)
                return render(request,'success.html')
        # return HttpResponseRedirect('/')
    return render(request,'voteaura.html',context)


def thankyou(request):
    return render(request,'thankyou.html')

def winnervote(request):

    print("\n\n\n\n\n\n\n")
    (win,v)=vote.winner()
    winner={'sno':1,'name':'AMD - Manohar'}
    if win==1:

        print('Party Serial Number : 3 \n CMD - Praveen')


    elif win == 2:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 2 \n HMT - Prashant')

    elif win==3:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 1 \n AMD - Manohar')

    else :
        print('No winner its either a tie or no one has voted yet')
    print("Number of votes : ", v)
    return render(request,'winner.html',winner)


def winnervotea(request):

    print("\n\n\n\n\n\n\n")
    (win,v)=vote.winnera()
    winner={'sno':1,'name':'HMT - Yashvan'}
    if win==1:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 1 \n HMT - Yashvan')

    elif win == 2:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 2 \n CMD Mahima')

    elif win==3:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 3 \n AMD - Nirnay Jindal')

    else :
        print('No winner its either a tie or no one has voted yet')
    print("Number of votes : ", v)
    return render(request,'winner.html',winner)


def winnervoteu(request):

    print("\n\n\n\n\n\n\n")
    (win,v)=vote.winneru()
    winner={'sno':1,'name':'HMT - Yashvan'}
    if win==1:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 1 \n HMT - Prerna')

    elif win == 2:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 2 \n CMD Abhishek')

    elif win==3:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 3 \n AMD - Bansal')

    else :
        print('No winner its either a tie or no one has voted yet')
    print("Number of votes : ",v)

    return render(request,'winner.html',winner)

def winneroverall(request):
    print("\n\n\n\n\n\n\n")
    # winner = {'sno': 1, 'name': 'HMT - Yashvan'}
    (wina,va)=vote.winnera()
    if wina==1:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 1 \n HMT - Yashvan')

    elif wina == 2:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 2 \n CMD Mahima')

    elif wina==3:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 3 \n AMD - Nirnay Jindal')

    else :
        print('No winner its either a tie or no one has voted yet')
    print("\n\n")

    (winp,vp)=vote.winner()
    if winp == 1:

        print('Party Serial Number : 3 \n CMD - Praveen')


    elif winp == 2:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 2 \n HMT - Prashant')

    elif winp == 3:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 1 \n AMD - Manohar')

    else:
        print('No winner its either a tie or no one has voted yet')
    print("\n")
    (winu,vu)=vote.winneru()
    if winu==1:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 1 \n HMT - Prerna')

    elif winu == 2:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 2 \n CMD Abhishek')

    elif winu==3:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 3 \n AMD - Bansal')

    else :
        print('No winner its either a tie or no one has voted yet')
    nh=0
    nc=0
    na=0
    if wina ==1:
        nh+=1
    if wina ==2:
        nc+=1
    if wina ==3:
        na+=1

    if winu == 1:
        nh += 1
    if winu == 2:
        nc += 1
    if winu == 3:
        na += 1

    if winp == 1:
        nc += 1
    if winp == 2:
        nh += 1
    if winp== 3:
        na += 1

    winner=max(nc,nh,na)
    if winner == nc:
        if winner==nh or winner==na:
            print("Multiple winners\n")
        print("*************\n")
        print("Winner is CMD")
        print("Number of constituencies : ",winner)

        print("\n")
        print("*************\n")

    if winner == nh:
        if winner==nc or winner==na:
            print("Multiple winners\n")

        print("*************\n")
        print("Winner is HMT")
        print("Number of constituencies : ",winner)


        print("\n")
        print("*************\n")

    if winner == na:
        if winner==nh or winner==nc:
            print("Multiple winners\n")
        print("*************\n")
        print("Winner is AMD")
        print("Number of constituencies : ",winner)
        print("\n")
        print("*************\n")


    return render(request,'winner.html')

def winnerdetails(request):
    (a,b,c,d,e,f,g,h,i) = vote.winnerdetails()

    print("Voting results of Amroha : \n")
    print('Party Serial Number : 1 \n HMT - Yashvan ')
    print("Number of votes : ",d)
    print("\n")
    print('Party Serial Number : 2 \n CMD Mahima')
    print("Number of votes : ", e)
    print("\n")

    print('Party Serial Number : 3 \n AMD - Nirnay Jindal')
    print("Number of votes : ", f)
    print("\n")

    print("\n\n")
    print("Voting results of Palghar : \n")
    print('Party Serial Number : 1 \n AMD - Manohar')
    print("Number of votes : ", a)
    print("\n")


    print('Party Serial Number : 2 \n HMT - Prashant')
    print("Number of votes : ", b)
    print("\n")



    print('Party Serial Number : 3 \n CMD - Praveen')
    print("Number of votes : ", c)
    print("\n")

    print("Voting results of Udma : \n")
    print('Party Serial Number : 1 \n HMT - Prerna')
    print("Number of votes : ", f)
    print("\n")

    print('Party Serial Number : 2 \n CMD Abhishek')
    print("Number of votes : ", g)
    print("\n")

    print('Party Serial Number : 3 \n AMD - Bansal')
    print("Number of votes : ", h)
    print("\n")

    return render(request , 'winner.html')


