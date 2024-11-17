import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        assert 'Матрица' in collector.get_books_genre()

    def test_set_book_genre_book_updates_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фантастика')
        collector.set_book_genre('Матрица', 'Детективы')
        assert collector.get_book_genre('Матрица') == 'Детективы'

    @pytest.mark.parametrize("book_name, genre", [
        ('Хоббит', 'Фантастика'),
        ('Убийство в Восточном экспрессе', 'Детективы'),
        ('Оно', 'Ужасы'),
        ('Алладин', 'Мультфильмы'),
        ('Один дома', 'Комедии'),
    ])
    def test_get_book_genre_parametrized(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фантастика')
        fiction_books = collector.get_books_with_specific_genre('Фантастика')
        assert fiction_books == ['Матрица']


    def test_get_books_genre_multiple_books_with_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фантастика')
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        expected_books_list = {
            'Матрица': 'Фантастика',
            'Хоббит': 'Фантастика',
            'Убийство в Восточном экспрессе': 'Детективы'
        }
        assert collector.get_books_genre() == expected_books_list

    def test_get_books_for_children_finds_children_books_only(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Алладин')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        collector.add_new_book('Один дома')
        collector.set_book_genre('Один дома', 'Комедии')
        children_books = collector.get_books_for_children()
        expected_children_books = ['Хоббит', 'Алладин', 'Один дома']
        assert children_books == expected_children_books

    def test_add_book_to_favorites_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        favorite_list = collector.get_list_of_favorites_books()
        assert 'Хоббит' in favorite_list

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_new_book('Алладин')
        collector.add_book_in_favorites('Хоббит')
        collector.add_book_in_favorites('Алладин')
        collector.delete_book_from_favorites('Хоббит')
        favorite_list = collector.get_list_of_favorites_books()
        expected_favorite_list = ['Алладин']
        assert favorite_list == expected_favorite_list

    def test_get_list_of_favorites_books_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.add_new_book('Алладин')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        collector.add_book_in_favorites('Хоббит')
        collector.add_book_in_favorites('Алладин')
        favorites_books = collector.get_list_of_favorites_books()
        expected_books = ['Хоббит', 'Алладин']
        assert favorites_books == expected_books
