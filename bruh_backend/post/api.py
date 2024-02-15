from django.http import JsonResponse

from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_create(request):
    data = request.data

    print(data)

    return JsonResponse({'message': 'Post created successfully'}, status=201)
