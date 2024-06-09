from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.review import Review
from NagoyameshiApp.forms import ReviewForm

# レビュー編集
class ReviewEditView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'NagoyameshiApp/user/review_form.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('reviews', kwargs={'pk': self.object.restaurant.pk})