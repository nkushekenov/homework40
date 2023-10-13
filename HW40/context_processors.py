from HW40.models import Book
def books(request):
    books = Book.objects.all()
    return {'books': books}