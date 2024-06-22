from django.db import models
from NagoyameshiApp.models.custom_user import CustomUser
from NagoyameshiApp.models.restaurant import Restaurant
import datetime

class Booking(models.Model):
    TIME = [
        (datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), 
        (datetime.time(11, 0), '11:00'), (datetime.time(11, 30), '11:30'),
        (datetime.time(12, 0), '12:00'), (datetime.time(12, 30), '12:30'),
        (datetime.time(13, 0), '13:00'), (datetime.time(13, 30), '13:30'),
        (datetime.time(14, 0), '14:00'), (datetime.time(14, 30), '14:30'),
        (datetime.time(15, 0), '15:00'), (datetime.time(15, 30), '15:30'),
        (datetime.time(16, 0), '16:00'), (datetime.time(16, 30), '16:30'),
        (datetime.time(17, 0), '17:00'), (datetime.time(17, 30), '17:30'),
        (datetime.time(18, 0), '18:00'), (datetime.time(18, 30), '18:30'),
        (datetime.time(19, 0), '19:00'), (datetime.time(19, 30), '19:30'),
        (datetime.time(20, 0), '20:00'), (datetime.time(20, 30), '20:30'),
    ]
    
    TIME_Sorted = sorted(TIME)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    date = models.DateField(verbose_name="予約日")
    time = models.TimeField(choices=TIME_Sorted, verbose_name="予約時間")
    number_of_persons = models.PositiveIntegerField(verbose_name="人数")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    @staticmethod
    def get_sorted_bookings(user=None, restaurant=None):
        bookings = Booking.objects.all()
        if user:
            bookings = bookings.filter(user=user)
        if restaurant:
            bookings = bookings.filter(restaurant=restaurant)
        return bookings.order_by('date', 'time')

    class Meta:
        app_label = 'NagoyameshiApp'