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
        if sort == "recipients":
            order_by = "-recipients"
        if sort == "total":
            order_by = "-total"
        if sort == "average":
            order_by = "-average"
        constituency_list = constituency_list.order_by(order_by)
    print constituency_list.query.as_sql()
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
        constituency=constituency).order_by(request.GET.get('sort', '-amount'))
    
    return render_to_response(
        'constituency.html', 
        {
            'constituency' : constituency,
            'recipients' : recipients,
        },
        context_instance=RequestContext(request)
    )
    