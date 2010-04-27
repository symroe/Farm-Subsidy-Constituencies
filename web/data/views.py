from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from data.models import Constituency, Recipient

def overview(request):
    
    top_recipients = Recipient.objects.all().order_by('-amount')[:10]
    top_constituencies_by_amount = Constituency.objects.all().order_by('-total')[:10]
    top_constituencies_by_avg = Constituency.objects.all().order_by('-average')[:10]
    top_constituencies_by_recipients = Constituency.objects.all().order_by('-recipients')[:10]
    
    return render_to_response(
        'overview.html', 
        {
            'top_recipients' : top_recipients,
            'top_constituencies_by_amount' : top_constituencies_by_amount,
            'top_constituencies_by_avg' : top_constituencies_by_avg,
            'top_constituencies_by_recipients' : top_constituencies_by_recipients,
        },
        context_instance=RequestContext(request)
    )

def constituency_list(request):
    constituency_list = Constituency.objects.all()
    sort = request.GET.get('sort')
    if sort:
        if sort == "name":
            order_by = "name"
        elif sort == "recipients":
            order_by = "-recipients"
        elif sort == "average":
            order_by = "-average"
        else:
            order_by = "-total"

            
        constituency_list = constituency_list.order_by(order_by)

    return render_to_response(
        'constituency_list.html', 
        {
            'constituency_list' : constituency_list,
        },
        context_instance=RequestContext(request)
    )

def constituency(request, slug):
    constituency = get_object_or_404(Constituency, slug=slug)
    recipients = Recipient.objects.filter(
        constituency=constituency)
    
    sort = request.GET.get('sort', 'amount')
    if sort == "name":
        order_by = "name"
    else:
        order_by = "-amount"
    recipients = recipients.order_by(order_by)
    
    return render_to_response(
        'constituency.html', 
        {
            'constituency' : constituency,
            'recipients' : recipients,
        },
        context_instance=RequestContext(request)
    )
    
def recipients(request):
    all_recipients = Recipient.objects.all().exclude(name="")
    
    sort = request.GET.get('sort', 'amount')
    if sort == "name":
        order_by = "name"
    elif sort== "constituency":
        order_by = "constituency"
    else:
        order_by = "-amount"
    all_recipients = all_recipients.order_by(order_by)
    
    return render_to_response(
        'recipients.html', 
        {
            'recipients' : all_recipients,
        },
        context_instance=RequestContext(request)
    )
    
    
    