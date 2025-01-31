from django.views.generic import CreateView
from django.urls import reverse_lazy
from NagoyameshiApp.models.review import Review
from NagoyameshiApp.forms import ReviewForm

# レビュー投稿（有料会員のみ）
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'NagoyameshiApp/user/review_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('reviews', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = self.get_object()
        context['restaurant'] = review.restaurant
        return context