import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_matrix_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        assert 'Матрица' in collector.get_books_genre()

    def test_set_book_genre_matrix_updates_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        assert collector.get_books_genre()['Матрица'] == ''
        collector.set_book_genre('Матрица', 'Фантастика')
        assert collector.get_book_genre('Матрица') == 'Фантастика'
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

    def test_get_books_with_specific_genre_various_books_returns_valid_lists(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фантастика')
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Ужасающий')
        collector.set_book_genre('Ужасающий', 'Ужасы')
        collector.add_new_book('Алладин')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        collector.add_new_book('Один дома')
        collector.set_book_genre('Один дома', 'Комедии')
        fiction_books = collector.get_books_with_specific_genre('Фантастика')
        horror_books = collector.get_books_with_specific_genre('Ужасы')
        cartoons = collector.get_books_with_specific_genre('Мультфильмы')
        comedy_books = collector.get_books_with_specific_genre('Комедии')
        detective_books = collector.get_books_with_specific_genre('Детективы')
        assert 'Матрица' in fiction_books
        assert 'Хоббит' in fiction_books
        assert 'Оно' in horror_books
        assert 'Ужасающий' in horror_books
        assert 'Алладин' in cartoons
        assert 'Один дома' in comedy_books
        assert 'Убийство в Восточном экспрессе' in detective_books

    def test_get_books_genre_multiple_books_with_genres(self):
        collector = BooksCollector()
        assert len(collector.get_books_genre()) == 0
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

    def test_get_books_for_children_various_books_returns_children_books_only(self):
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
        adult_books = ['Оно', 'Убийство в Восточном экспрессе']
        assert children_books == expected_children_books
        for book in children_books:
            assert book not in adult_books

    def test_add_book_in_favorites_multiple_books_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.add_new_book('Алладин')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        collector.add_book_in_favorites('Хоббит')
        favorite_list = collector.get_list_of_favorites_books()
        assert 'Хоббит' in favorite_list
        assert len(favorite_list) == 1

    def test_delete_book_from_favorites_existing_book_book_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.add_new_book('Алладин')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        collector.add_book_in_favorites('Хоббит')
        collector.add_book_in_favorites('Алладин')
        collector.delete_book_from_favorites('Хоббит')
        favorite_list = collector.get_list_of_favorites_books()
        assert 'Алладин' in favorite_list
        assert len(favorite_list) == 1

    def test_get_list_of_favorites_books_multiple_books_returns_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.add_new_book('Алладин')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        collector.add_book_in_favorites('Хоббит')
        collector.add_book_in_favorites('Алладин')
        favorites_books = collector.get_list_of_favorites_books()
        expected_books = ['Хоббит', 'Алладин']
        assert len(favorites_books) == 2
        assert favorites_books == expected_books
