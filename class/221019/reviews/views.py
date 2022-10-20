from django.shortcuts import redirect, render
from django.db.models import Q
from reviews.forms import ReviewForm, CommentForm
from reviews.models import Review, Comment

from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, "reviews/index.html")

@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("reviews:search")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/form.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        "review": review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, "reviews/detail.html", context)

@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/form.html", context)

@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        review.delete()
        return redirect("reviews:search")
    else:
        from django.http import HttpResponseForbidden

        return HttpResponseForbidden()


@login_required
def comments_create(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect("reviews:detail", review.pk)
    

def comments_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)


def search(request):
    all_data = Review.objects.order_by("-pk")
    search = request.GET.get("search", "")
    if search:
        search_list = all_data.filter(
            Q(title__icontains=search) | Q(movie_name__icontains=search)
        )

        context = {
            "search_list": search_list,
        }
    else:
        context = {
            "search_list": all_data,
        }

    return render(request, "reviews/search.html", context)
