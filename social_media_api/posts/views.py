from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response


from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




#Filters
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the list of users the current authenticated user is following
        following_users = self.request.user.following.all()

        # Filter posts by these users and order by creation date (most recent first)
        return Post.objects.filter(author__in=following_users).order_by('-created_at')




class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create a notification for the post author
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id
            )
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        return Response({"message": "You haven't liked this post yet"}, status=status.HTTP_400_BAD_REQUEST)
