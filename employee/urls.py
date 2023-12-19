from django.urls import path
from .views import add_book_stock, get_active_json, get_books_for_employee, get_catalog_json, main, catalogBook, bookFromWriter, test, getBook, mainBook, mainBookFromWriter, mainSetBook, setBook, accBookFromWriter, denBookFromWriter, showingToMember, notShowingToMember, employee_page, toggle_catalog_visibility, update_book_status
from .views import main, catalogBook, bookFromWriter, test, getBook, mainBook, mainBookFromWriter, mainSetBook, setBook, accBookFromWriter, denBookFromWriter, showingToMember, notShowingToMember, mainCatalog

app_name = 'employee'

urlpatterns = [
    path('main', main, name='main'),
    path('catalog', mainCatalog, name='catalog'),
    path('set-book', mainSetBook, name='mainSetBook'),
    path('book-from-writer', mainBookFromWriter, name='mainBookFromWriter'),
    path('book/<int:book_id>', mainBook, name='bookFromWriter'),
    path('api/catalog', catalogBook, name='catalogBook'),
    path('api/acc', bookFromWriter, name='bookFromWriter'),
    path('api/book/<int:book_id>', getBook, name='bookFromWriter'),
    path('api/set', setBook, name='setBook'),
    path('acceptBook', accBookFromWriter, name='acceptBook'),
    path('deniedBook', denBookFromWriter, name='deniedBook'),
    path('show', showingToMember, name='showingToMember'),
    path('notshow', notShowingToMember, name='notShowingToMember'),
    path('test', test, name='test'),
    path('get-book-json/', get_books_for_employee, name='get_books_for_employee'),
    path('get-catalog-json/', get_catalog_json, name='get_catalog_json'),
    path('get-active-json/', get_active_json, name='get_active_json'),
    path('catalog/toggle-visibility/<int:pk>/', toggle_catalog_visibility, name='toggle-catalog-visibility'),
    path('update-book-status/<int:book_id>/<str:status>/', update_book_status, name='update_book_status'),
    path('add-book-stock/', add_book_stock, name='add_book_stock'),
]
