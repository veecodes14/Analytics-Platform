import uuid
from .models import Visitor, Site
from django.utils.deprecation import MiddlewareMixin

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        site_domain = request.get_host()
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        ip_address = self.get_client_ip(request)

        visitor_id = request.COOKIES.get('visitor_id')
        site = Site.objects.filter(domain__icontains=site_domain).first()

        if not visitor_id or not Visitor.objects.filter(visitor_id=visitor_id).exists():
            new_visitor = Visitor.objects.create(
                site=site,
                user_agent=user_agent,
                ip_address=ip_address
            )

            request.new_visitor = new_visitor
            request.visitor_id = new_visitor.visitor_id
        else:
            request.visitor_id = visitor_id

    def process_response(self, request, response):
        if hasattr(request, 'new_visitor'):
            response.set_cookie('visitor_id', str(request.visitor_id), max_age=31536000)
        return response
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    



