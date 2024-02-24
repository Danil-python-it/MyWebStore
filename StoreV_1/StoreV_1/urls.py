"""
URL configuration for StoreV_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from StoreLovePage import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

user_patterns = (
	[
		path("profile",views.ProfilePage, name="profile"),
		path("login", views.LoginPage, name="login"),
		path("logout", views.LogoutPage, name="logout"),
		path("registration", views.RegistionPage, name="registration"),
		path("baskets", views.BasketPage, name="Baskets"),
    ]
)
show_patterns = (
	[
		path("category/<int:id>",views.CategoryPage, name="Category"),
		path("shopitem/<int:id>", views.ShopItemPage, name="ShopItem"),

    ]
)
admin_patterns = (
	[
		path("category",views.CategoryCreatePage, name="crt"),
		path("shop_items",views.ShopItemsCreatePage, name="shit"),
    ]
)


urlpatterns = [
    path('admin/', admin.site.urls),
	path('create/', include(admin_patterns)),
	path('', views.MainPage, name="MainPage"),
	path('user/', include(user_patterns)),
    path('show/', include(show_patterns))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()