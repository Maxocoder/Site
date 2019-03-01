from django.shortcuts import render
from car_shop.forms import *
from car_shop.models import *
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _


def main(request):
    context = {}
    context['form'] = FormRegistration()
    return render(request, 'car_shop/Main.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = FormRegistration(request.POST)
        formtime = FormTime(request.POST)

        try:
            time = datetime.datetime.strptime(request.POST['time'], "%d.%m.%Y %H:%M")

            if time < datetime.datetime.utcnow().replace():
                return render(request, 'car_shop/registration.html', {'form': form, 'time': formtime,
                                                                  'past': 'Выберите правильную дату(не прошлое время)'})

            if time.hour > 18 and time.minute > 0:
                return render(request, 'car_shop/registration.html', {'form': form, 'time': formtime,
                  'minutes': 'Диагностика длится один час, сервис работает до 20:00, пожалуйста, выберите другое время'})
        except:
            formtime = FormTime(request.POST['time'])
            return render(request, 'car_shop/registration.html', {'form': form, 'time': formtime,
                                                                  'except': 'введите правильную форму даты'})
        if form.is_valid():
            context = {}
            context['firstname'] = form.cleaned_data['firstname']
            context['lastname'] = form.cleaned_data['lastname']
            context['reporting'] = form.cleaned_data['reporting']
            context['auto'] = form.cleaned_data['auto']
            context['email'] = form.cleaned_data['email']
            context['profi'] = form.cleaned_data['profi']
            context['datetime'] = time

            temp = BaseRegister(firstname=context['firstname'], lastname= context['lastname'],
                            reporting=context['reporting'], auto=context['auto'], email=context['email'],
                            profi=context['profi'], date=context['datetime'])
            temp.save()
            context['datetime'] = context['datetime'].strftime("%d.%m.%Y %H:%M:%S")

            return render(request, 'car_shop/registration_success.html', context=context)
        else:
            return render(request, 'car_shop/registration.html', {'form': form, 'time': time})
    else:
        form = FormRegistration()
        return render(request, 'car_shop/registration.html', {'form': form})
