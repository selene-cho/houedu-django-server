from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("/", include("main.urls")),
    path("api/v1/courses/", include("courses.urls")),
    path("api/v1/reviews/", include("reviews.urls")),
    path("api/v1/users/", include("users.urls")),
]
