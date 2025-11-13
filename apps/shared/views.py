from django.db import connection
from django.http import JsonResponse


def health_check(request):
    """Health check endpoint for load balancer"""
    try:
        # Check database connection
        connection.ensure_connection()
        return JsonResponse({"status": "healthy"}, status=200)
    except Exception as e:
        return JsonResponse({"status": "unhealthy", "error": str(e)}, status=503)
