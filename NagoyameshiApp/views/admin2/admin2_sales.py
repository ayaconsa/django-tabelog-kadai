from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from NagoyameshiApp.models.custom_user import CustomUser
from datetime import datetime, timedelta

# 管理者：売上集計
class SalesView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "NagoyameshiApp/admin2/sales.html"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト

    def get_sales_data(self):
        today = datetime.today()
        first_day_of_year = today.replace(month=1, day=1)
        current_year = today.year
        start_year = 2021

        # 年間売上
        yearly_revenue_data = []
        for year in range(start_year, current_year + 1):
            yearly_revenue = 0
            yearly_subscribers = 0
            yearly_unsubscribes = 0  # 年間退会者数
            for month in range(1, 13):
                month_start = datetime(year=year, month=month, day=1)
                month_end = (month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
                
                # 月末時点での有料会員数を取得
                subscribers_end_of_month = CustomUser.objects.filter(subscription=True, updated_at__lte=month_end).count()
                
                # 当月に退会した人数を取得
                unsubscribed_this_month = CustomUser.objects.filter(cancellation_date__year=year, cancellation_date__month=month).count()
                
                # 月ごとの売上を計算
                monthly_subscribers = subscribers_end_of_month + unsubscribed_this_month
                monthly_revenue = monthly_subscribers * 300

                yearly_revenue += monthly_revenue
                yearly_unsubscribes += unsubscribed_this_month
                if month == 12:
                    yearly_subscribers = subscribers_end_of_month

            yearly_revenue_data.insert(0, {  # 最新のデータが上に来るようにリストの先頭に挿入
                'year': year,
                'revenue': yearly_revenue,
                'subscribers': yearly_subscribers,
                'unsubscribes': yearly_unsubscribes
            })

        # 月間売上
        monthly_revenue_data = []
        month_start = datetime(year=start_year, month=1, day=1)
        while month_start <= today:
            month_end = (month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            
            # 月末時点での有料会員数を取得
            subscribers_end_of_month = CustomUser.objects.filter(subscription=True, updated_at__lte=month_end).count()
            
            # 当月に退会した人数を取得
            unsubscribed_this_month = CustomUser.objects.filter(cancellation_date__year=month_start.year, cancellation_date__month=month_start.month).count()
            
            # 月ごとの売上を計算
            monthly_subscribers = subscribers_end_of_month + unsubscribed_this_month
            monthly_revenue = monthly_subscribers * 300

            monthly_revenue_data.insert(0, {  # 最新のデータが上に来るようにリストの先頭に挿入
                'month': month_start.strftime('%Y/%m'),
                'revenue': monthly_revenue,
                'subscribers': subscribers_end_of_month,
                'unsubscribes': unsubscribed_this_month
            })

            month_start = (month_start + timedelta(days=32)).replace(day=1)

        return {
            'yearly_revenue_data': yearly_revenue_data,
            'monthly_revenue_data': monthly_revenue_data
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sales_data = self.get_sales_data()
        context.update(sales_data)
        return context
