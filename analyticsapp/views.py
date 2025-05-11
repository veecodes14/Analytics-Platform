from .models import Site, Profile, UserActivity
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_total_visits(request):
    site_id = request.GET.get('site')

    if site_id:
        total_visits = UserActivity.objects.filter(site__id=site_id).count()
    else:
        total_visits = UserActivity.objects.count()

    return Response({'total_visits': total_visits})
    

@api_view(['GET'])
def get_total_unique_visits(request):
    start_date = request.query_params.get('start')
    end_date = request.query_params.get('end')
    site_id = request.GET.get('site')

    activities = UserActivity.objects.all()

    if site_id:
        activities = activities.filter(site__id=site_id)
    if start_date:
        activities = activities.filter(timestamp__date__gte=start_date)
    if end_date:
        activities = activities.filter(timestamp__date__lte=end_date)

    unique_visitors = activities.values('visitor').distinct().count()

    return Response({'total_unique_visits': unique_visitors})


 




    


# Create your views here.
