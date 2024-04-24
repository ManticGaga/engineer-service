import pytest
from app.api.models import EngineerIn, EngineerOut

engineers = EngineerIn(
    name='Алексей Петров',
    phone='+71212121212',
    pay='50000',
    genre='Мужчина'
)


def test_create_client(engineers: EngineerIn = engineers):
    assert dict(engineers) == {'name': engineers.name,
                              'phone': engineers.phone,
                              'pay': engineers.pay,
                              'genre': engineers.genre
                              }


def test_update_client_age(engineers: EngineerIn = engineers):
    engineers_upd = EngineerOut(
        name='Алексей Петров',
        phone='+71212121212',
        pay='50000',
        genre='Мужчина',
        id=1
    )
    assert dict(engineers_upd) == {'name': engineers.name,
                              'phone': engineers.phone,
                              'pay': engineers.pay,
                              'genre': engineers.genre,
                              'id': engineers_upd.id
                              }


def test_update_client_genre(engineers: EngineerIn = engineers):
    engineers_upd = EngineerOut(
        name='Алексей Петров',
        phone='+71212121212',
        pay='50000',
        genre='Мужчина',
        id=1
    )
    assert dict(engineers_upd) == {'name': engineers.name,
                              'phone': engineers.phone,
                              'pay': engineers.pay,
                              'genre': engineers.genre,
                              'id': engineers_upd.id
                              }
