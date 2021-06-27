from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from newapp.models import UserProfileInfo
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')



def payment_process(request):
    # order_id = request.session.get('order_id')
    # print(order_id)
    # order = get_object_or_404(UserProfileInfo, id=order_id)
    # #userprofile = UserProfileInfo.objects.get(user=request.user)
    # print(order)
    # print(order.id)
    # amount = order.amount
    # print(amount)
    host = request.get_host()
    # print(host)

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '100000',
        'item_name': 'test',
        'invoice': 'test_payment',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context= {'form':form}
    return render(request, 'payment/process.html', context)
