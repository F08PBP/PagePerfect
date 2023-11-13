from django.urls import path
from .views import main, catalogBook, bookFromWriter, test, getBook, mainBook, mainBookFromWriter, mainSetBook, setBook, accBookFromWriter, denBookFromWriter, showingToMember, notShowingToMember, employee_page
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
]
