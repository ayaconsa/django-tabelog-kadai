from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from NagoyameshiApp.views.user.top_view import TopView
from NagoyameshiApp.views.user.company_overview import CompanyOverviewView
from NagoyameshiApp.views.user.terms_of_use import TermsOfUseView
from NagoyameshiApp.views.user.create_account import CreateAccountView
from NagoyameshiApp.views.user.login import LoginView
from NagoyameshiApp.views.user.restaurant_list import RestaurantListView
from NagoyameshiApp.views.user.restaurant_detail import RestaurantDetailView
from NagoyameshiApp.views.user.logout import LogoutView
from NagoyameshiApp.views.user.password_resetting import PasswordResettingView
from NagoyameshiApp.views.user.subscription_guide import SubscriptionGuideView
from NagoyameshiApp.views.user.delete_account import DeleteAccountView
from NagoyameshiApp.views.user.account_info import AccountInfoView
from NagoyameshiApp.views.user.bookings import BookingsView
from NagoyameshiApp.views.user.favorites import FavoritesView
from NagoyameshiApp.views.user.change_payment_method import ChangePaymentMethodView
from NagoyameshiApp.views.user.unsubscribe import UnsubscribeView

from NagoyameshiApp.views.manage.manage_login import ManageLoginView
from NagoyameshiApp.views.manage.manage_top import ManageTopView
from NagoyameshiApp.views.manage.restaurant_info import RestaurantInfoView
from NagoyameshiApp.views.manage.booking_confirmation import BookingConfirmationView
from NagoyameshiApp.views.manage.review_confirmation import ReviewConfirmationView

from NagoyameshiApp.views.superuser.admin_login import AdminLoginView
from NagoyameshiApp.views.superuser.admin_top import AdminTopView
from NagoyameshiApp.views.superuser.category_list import CategoryListView
from NagoyameshiApp.views.superuser.user_list import UserListView
from NagoyameshiApp.views.superuser.sales import SalesView
from NagoyameshiApp.views.superuser.user_number import UserNumberView

from NagoyameshiApp.views.superuser.admin_restaurant_list import AdminRestaurantListView
from NagoyameshiApp.views.superuser.admin_restaurant_detail import AdminRestaurantDetailView
from NagoyameshiApp.views.superuser.admin_restaurant_edit import AdminRestaurantEditView
from NagoyameshiApp.views.superuser.admin_booking_confirmation import AdminBookingConfirmationView
from NagoyameshiApp.views.superuser.admin_review_confirmation import AdminReviewConfirmationView






urlpatterns = [
    
    path('', TopView.as_view(), name="top"),
    path('company_overview/', CompanyOverviewView.as_view(), name="company_overview"),
    path('terms_of_use/', TermsOfUseView.as_view(), name="terms_of_use"),

    path('account_create/', CreateAccountView.as_view(), name="account_create"),
    path('login/', LoginView.as_view(), name="login"),   
    path('restaurant_list/', RestaurantListView.as_view(), name="restaurant_list"),
    path('restaurant_detail/', RestaurantDetailView.as_view(), name="restaurant_detail"),

    path('logout/', LogoutView.as_view(), name="logout"),
    path('password_resetting/', PasswordResettingView.as_view(), name="password_resetting"),
    path('subscription_guide/', SubscriptionGuideView.as_view(), name="subscription_guide"),
    path('delete_account/', DeleteAccountView.as_view(), name="delete_account"),

    path('account_info/', AccountInfoView.as_view(), name="account_info"),
    path('bookings/', BookingsView.as_view(), name="bookings"),
    path('favorites/', FavoritesView.as_view(), name="favorites"),
    path('change_payment_method/', ChangePaymentMethodView.as_view(), name="change_payment_method"),
    path('unsubscribe/', UnsubscribeView.as_view(), name="unsubscribe"),
    
    
    
    path('manage/', ManageTopView.as_view(), name="manage_top"),
    path('manage/login/', ManageLoginView.as_view(), name="manage_login"),
    path('manage/restaurant_info/', RestaurantInfoView.as_view(), name="manage_restaurant_info"),
    path('manage/booking_confirmation/', BookingConfirmationView.as_view(), name="manage_booking_confirmation"),
    path('manage/review_confirmation/', ReviewConfirmationView.as_view(), name="manage_review_confirmation"),
    
    
    
    path('admin/', admin.site.urls),
    path('admin/login/', AdminLoginView.as_view(), name="admin_login"),
    path('admin2/top/', AdminTopView.as_view(), name="admin_top"),
    path('admin/category_list/', CategoryListView.as_view(), name="admin_category_list"),
    path('admin/user_list/', UserListView.as_view(), name="admin_user_list"),
    path('admin/sales/', SalesView.as_view(), name="admin_sales"),
    path('admin/user_number/', UserNumberView.as_view(), name="admin_user_number"),
    
    
    path('admin/restaurant_list/', AdminRestaurantListView.as_view(), name="admin_restaurant_list"),
    path('admin/restaurant_detail/', AdminRestaurantDetailView.as_view(), name="admin_restaurant_detail"),
    path('admin/restaurant_edit/', AdminRestaurantEditView.as_view(), name="admin_restaurant_edit"),
    
    path('admin/booking_confirmation/', AdminBookingConfirmationView.as_view(), name="admin_booking_comfirmation"),
    path('admin/review_confirmation/', AdminReviewConfirmationView.as_view(), name="admin_review_confirmation"),
    
]
