from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user, read=False).order_by('-timestamp')

class MarkAsReadView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        notification = Notification.objects.get(pk=pk, recipient=request.user)
        notification.read = True
        notification.save()
        return Response({"message": "Notification marked as read"})

