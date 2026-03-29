import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Campaign

def home(request):
    return render(request, 'index.html')


@csrf_exempt 
def campaigns_api(request):
    if request.method == 'GET':
        campaigns = list(Campaign.objects.values())
        return JsonResponse(campaigns, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        campaign = Campaign.objects.create(
            name=data['name'],
            budget=data['budget'],
            spend=data['spend'],
            status=data['status']
        )
        return JsonResponse({
            'id': campaign.id,
            'name': campaign.name,
            'budget': float(campaign.budget),
            'spend': float(campaign.spend),
            'status': campaign.status
        })