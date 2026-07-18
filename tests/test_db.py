import unittest
import os

os.environ['TESTING'] = 'true'

from peewee import SqliteDatabase
from app import TimelinePost

test_db = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)

MODELS = [TimelinePost]

class TestDB(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        """Test creating and querying timeline posts in the database."""
        first_post = TimelinePost.create(
            name='John Doe',
            email='john@example.com',
            content='Hello world, I am John!'
        )
        assert first_post is not None

        second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content='Hello world, I am Jane!'
        )
        assert second_post is not None

        # Query the database to verify
        posts = TimelinePost.select()
        assert posts.count() == 2

        first = posts[0]
        assert first.name == 'John Doe'
        assert first.email == 'john@example.com'
        assert first.content == 'Hello world, I am John!'

        second = posts[1]
        assert second.name == 'Jane Doe'
        assert second.email == 'jane@example.com'
        assert second.content == 'Hello world, I am Jane!'
