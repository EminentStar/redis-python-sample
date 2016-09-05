from django.shortcuts import render
import logging


# Create your views here.

LOGGER = logging.getLogger()


def main_view(request):
    if request.user.is_anonymous():
        LOGGER.warning(request.user)
    else:
        LOGGER.warning(request.user)

    LOGGER.warning(request.session.session_key)
    return render(request, 'redis_test/main_view.html', {'user': request.user})



