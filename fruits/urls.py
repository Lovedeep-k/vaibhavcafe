from django.urls import include, path

from.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index),
    path("index",index),
    path("aa",aa),
    path("about",about),
    path("cart",cart),
    path("checkouts",checkouts),
    path("contact",contact),
    path("indexx",indexs),
    path("news",news),
    path("shop",shop),
    path("singlenews",singlenews),
    path("singleproduct/<int:id>",singleproduct),
    path('remove/<int:id>',remove),
    path('thankyou',thankyou),
    ]

    


