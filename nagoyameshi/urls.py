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
from NagoyameshiApp.views.user.create_checkout_session import CreateCheckoutSessionView
from NagoyameshiApp.views.user.checkout_success import CheckoutSuccessView
from NagoyameshiApp.views.user.checkout_cancel import CheckoutCancelView
from NagoyameshiApp.views.user.cancel_subscription import CancelSubscriptionView

from NagoyameshiApp.views.user.delete_account import DeleteAccountView
from NagoyameshiApp.views.user.account_info import AccountInfoView
from NagoyameshiApp.views.user.account_info_update import AccountInfoEditView
from NagoyameshiApp.views.user.account_delete import AccountDeleteView
from NagoyameshiApp.views.user.bookings import BookingsView
from NagoyameshiApp.views.user.booking_cancel import BookingCancelView
from NagoyameshiApp.views.user.favorites import FavoritesView
from NagoyameshiApp.views.user.favorite_delete import FavoriteDeleteView

from NagoyameshiApp.views.user.change_payment_method import ChangePaymentMethodView
from NagoyameshiApp.views.user.unsubscribe import UnsubscribeView
from NagoyameshiApp.views.user.toggle_favorite import ToggleFavoriteView

from NagoyameshiApp.views.manage.manage_login import ManageLoginView
from NagoyameshiApp.views.manage.manage_top import ManageTopView
from NagoyameshiApp.views.manage.restaurant_info import RestaurantInfoView
from NagoyameshiApp.views.manage.booking_confirmation import BookingConfirmationView
from NagoyameshiApp.views.manage.review_confirmation import ReviewConfirmationView

from NagoyameshiApp.views.admin2.admin2_login import AdminLoginView
from NagoyameshiApp.views.admin2.admin2_top import AdminTopView
from NagoyameshiApp.views.admin2.admin2_category_list import CategoryListView
from NagoyameshiApp.views.admin2.admin2_category_delete import CategoryDeleteView
from NagoyameshiApp.views.admin2.admin2_category_registration import CategoryRegistrationView


from NagoyameshiApp.views.admin2.admin2_user_list import UserListView
from NagoyameshiApp.views.admin2.admin2_sales import SalesView
from NagoyameshiApp.views.admin2.admin2_user_number import UserNumberView

from NagoyameshiApp.views.admin2.admin2_restaurant_list import AdminRestaurantListView
from NagoyameshiApp.views.admin2.admin2_restaurant_detail import AdminRestaurantDetailView
from NagoyameshiApp.views.admin2.admin2_restaurant_edit import AdminRestaurantEditView
from NagoyameshiApp.views.admin2.admin2_restaurant_delete import AdminRestaurantDeleteView

from NagoyameshiApp.views.admin2.admin2_restaurant_registration import AdminRestaurantRegistrationView
from NagoyameshiApp.views.admin2.admin2_booking_confirmation import AdminBookingConfirmationView
from NagoyameshiApp.views.admin2.admin2_review_confirmation import AdminReviewConfirmationView
from NagoyameshiApp.views.admin2.admin2_review_deletion_confirmation import ReviewDeletionConfirmationView






urlpatterns = [
    
    path('', TopView.as_view(), name="top"),
    path('company_overview/', CompanyOverviewView.as_view(), name="company_overview"),
    path('terms_of_use/', TermsOfUseView.as_view(), name="terms_of_use"),

    path('account_create/', CreateAccountView.as_view(), name="account_create"),
    path('login/', LoginView.as_view(), name="login"),   
    path('restaurant_list/', RestaurantListView.as_view(), name="restaurant_list"),
    path('restaurant_detail/<int:pk>', RestaurantDetailView.as_view(), name="restaurant_detail"),

    path('logout/', LogoutView.as_view(), name="logout"),
    path('password_resetting/', PasswordResettingView.as_view(), name="password_resetting"),
    path('subscription_guide/', SubscriptionGuideView.as_view(), name="subscription_guide"),
    path('create_checkout_session/', CreateCheckoutSessionView.as_view(), name="create_checkout_session"),
    path('checkout_success/', CheckoutSuccessView.as_view(), name="checkout_success"),
    path('checkout_cancel/', CheckoutCancelView.as_view(), name="checkout_cancel"),
    path('cancel_subscription/', CancelSubscriptionView.as_view(), name='cancel_subscription'),



    path('delete_account/', DeleteAccountView.as_view(), name="delete_account"),

    path('account_info/', AccountInfoView.as_view(), name="account_info"),
    path('account_info_edit/', AccountInfoEditView.as_view(), name="account_info_edit"),
    path('account_delete/', AccountDeleteView.as_view(), name="account_delete"),

    path('bookings/', BookingsView.as_view(), name="bookings"),
    path('bookings/cancel/<int:pk>', BookingCancelView.as_view(), name="booking_cancel"),
    path('favorites/', FavoritesView.as_view(), name="favorites"),
    path('favorites/delete/<int:pk>', FavoriteDeleteView.as_view(), name="favorites_delete"),
    path('change_payment_method/', ChangePaymentMethodView.as_view(), name="change_payment_method"),
    path('unsubscribe/', UnsubscribeView.as_view(), name="unsubscribe"),
    path('toggle_favorite/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
    
    path('manage/', ManageTopView.as_view(), name="manage_top"),
    path('manage/login/', ManageLoginView.as_view(), name="manage_login"),
    path('manage/restaurant_info/', RestaurantInfoView.as_view(), name="manage_restaurant_info"),
    path('manage/booking_confirmation/', BookingConfirmationView.as_view(), name="manage_booking_confirmation"),
    path('manage/review_confirmation/', ReviewConfirmationView.as_view(), name="manage_review_confirmation"),
    
    
    # デフォルトのadmin
    path('admin/', admin.site.urls),
    
    # デフォルトのadminとは変えないとうまく表示されないのでadmin2にした
    path('admin2/login/', AdminLoginView.as_view(), name="admin_login"),
    path('admin2/', AdminTopView.as_view(), name="admin_top"),
    path('admin2/category_list/', CategoryListView.as_view(), name="admin_category_list"),
    path('admin2/category_confirm_delete/<int:pk>', CategoryDeleteView.as_view(), name="admin_category_delete"),
    path('admin2/category_registration/', CategoryRegistrationView.as_view(), name="admin_category_registration"),
    
    path('admin2/user_list/', UserListView.as_view(), name="admin_user_list"),
    path('admin2/sales/', SalesView.as_view(), name="admin_sales"),
    path('admin2/user_number/', UserNumberView.as_view(), name="admin_user_number"),
    
    
    path('admin2/restaurant_list/', AdminRestaurantListView.as_view(), name="admin_restaurant_list"),
    path('admin2/restaurant_detail/<int:pk>', AdminRestaurantDetailView.as_view(), name="admin_restaurant_detail"),
    path('admin2/restaurant_edit/<int:pk>', AdminRestaurantEditView.as_view(), name="admin_restaurant_edit"),
    path('admin2/restaurant_delete/<int:pk>', AdminRestaurantDeleteView.as_view(), name="admin_restaurant_delete"),
    path('admin2/restaurant_registration/', AdminRestaurantRegistrationView.as_view(), name="admin_restaurant_registration"),
    
    
    path('admin2/booking_confirmation/<int:pk>', AdminBookingConfirmationView.as_view(), name="admin_booking_confirmation"),
    path('admin2/review_confirmation/<int:pk>', AdminReviewConfirmationView.as_view(), name="admin_review_confirmation"),
    path('admin2/review_deletion_confirmation/<int:pk>', ReviewDeletionConfirmationView.as_view(), name="admin_review_deletion_confirmation"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)