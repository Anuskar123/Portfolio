from rest_framework.decorators import api_view
from rest_framework.response import Response 
from home.models import Post
from home.api.serializers import PostSerializers
from rest_framework import status


@api_view(['GET'])
def post_List(request):
    posts = Post.objects.all()
    serializer = PostSerializers(posts, many=True,context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
def api_Add(request):
    data = request.data
    serializer = PostSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def api_Delete():
    post = Post.objects.all()
    post.delete()
    return Response('Post deleted successfully!')

