import logging
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

LOGGER = logging.getLogger()
dict_user = {}


def main_view(request):
    if request.user.is_anonymous():
        LOGGER.warning(request.user)
    else:
        LOGGER.warning(request.user)

    LOGGER.warning(request.session.session_key)
    return render(request, 'redis_test/main_view.html', {'user': request.user})


@csrf_exempt
def visit_count(request, user_id):
    if request.method == 'POST':
        """ /visits/userid의 userid를 저장한다 """
        LOGGER.warning("POST visit request")
        LOGGER.warning(user_id)

        if dict_user.get(user_id, 0) == 0:
            dict_user[user_id] = 1
        else:
            dict_user[user_id] += 1

        LOGGER.warning(dict_user[user_id])
        return render(request, 'redis_test/main_view.html', {'user': request.user})
    else:
        """ 최근 5분간의 해당 userid의 사용자의 방문 수를 보여준다 """
        LOGGER.warning("GET visit request")
        LOGGER.warning(user_id)
        LOGGER.warning(dict_user[user_id])
        return render(request, 'redis_test/visit.html', {'visit_count': dict_user[user_id]})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')
    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')
