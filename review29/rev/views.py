from django.shortcuts import render
from django.http import JsonResponse
from .forms import ProductReviewForm
from .models import ProductReview

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

@ensure_csrf_cookie
def get_csrf_token_view(request):
    return JsonResponse({'message': 'CSRF cookie đã được set'})

@csrf_exempt  # tạm thời bỏ qua kiểm tra CSRF
def save_review_view(request):
    if request.method == 'POST':
        form = ProductReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            return JsonResponse({'message': 'Đã lưu thành công!', 'video_url': review.video_url})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Chỉ hỗ trợ phương thức POST'}, status=405)

def list_reviews(request):
    reviews = ProductReview.objects.all().values()
    return JsonResponse(list(reviews), safe=False)

def get_review_by_url(request):
    url = request.GET.get('video_url')
    if not url:
        return JsonResponse({'error': 'Thiếu tham số video_url'}, status=400)

    try:
        review = ProductReview.objects.get(video_url=url)
        data = {
            'video_url': review.video_url,
            'video_file': review.video_file.url if review.video_file else None,
            'aff_link_1': review.aff_link_1,
            'aff_link_2': review.aff_link_2,
            'aff_link_3': review.aff_link_3,
            'aff_link_4': review.aff_link_4,
            'aff_link_5': review.aff_link_5,
        }
        return JsonResponse(data)
    except ProductReview.DoesNotExist:
        return JsonResponse({'error': 'Không tìm thấy video'}, status=404)
