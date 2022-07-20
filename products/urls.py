from django.urls import path

from .views import landing_page, product_page, single_product_view, add_product_view, handle_add_product, add_coins, current_user, share_coins
from .views import share_coins_view, change_share_coin_status

urlpatterns = [
    path('',landing_page, name="homepage"),
    path('products/', product_page, name="products"),
    path('view_product/<int:product_id>/', single_product_view, name="single_product"),
    path('add/', add_product_view),
    path('add_product/', handle_add_product),

    #game_apis
    path('add_coins/<int:user_id>/<int:num_coins>/', add_coins),
    path('share_coins/<int:user_id>/<int:num_coins>/<int:reciever_id>/', share_coins),
    path('current_user/', current_user),

    #share_coins_urls
    path('share_coins/', share_coins_view, name="share_coins"),
    path('exchange_coins/', change_share_coin_status, name="exchange_coins")
]