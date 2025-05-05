from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Menampilkan kolom-kolom ini di halaman daftar (list view) admin
    list_display = ["title", "instructor", "created_at", "updated_at"]

    # Menambahkan kolom yang bisa dicari menggunakan search box
    search_fields = ["title", "instructor__username"]

    # Menambahkan filter sidebar berdasarkan kolom tertentu
    list_filter = ["created_at", "updated_at", "instructor"]
