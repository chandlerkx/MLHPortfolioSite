import unittest
import os

os.environ['TESTING'] = 'true'

from app import app, TimelinePost
from peewee import SqliteDatabase

test_db = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)

MODELS = [TimelinePost]

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        test_db.bind(MODELS)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_home(self):
        """Test that the home page loads successfully."""
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<title>frontend</title>' in html

    def test_home_has_root_div(self):
        """Test that the home page contains the root div for the React app."""
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<div id="root">' in html

    def test_timeline(self):
        """Test GET and POST on /api/timeline_post."""
        # Start with 0 posts
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data['timeline_posts'] == []

        # POST a valid timeline post
        response = self.client.post('/api/timeline_post', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'content': 'Hello world, I am John!'
        })
        assert response.status_code == 200

        # GET should now return 1 post
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        json_data = response.get_json()
        assert len(json_data['timeline_posts']) == 1
        assert json_data['timeline_posts'][0]['name'] == 'John Doe'

    def test_timeline_page(self):
        """Test that the /timeline page loads successfully."""
        response = self.client.get('/timeline')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert 'Timeline' in html

    def test_malformed_timeline_post(self):
        """Test that malformed POST requests return 400 with appropriate messages."""
        # Missing name
        response = self.client.post('/api/timeline_post', data={
            'email': 'john@example.com',
            'content': 'Hello world, I am John!'
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert 'Invalid name' in html

        # Empty name
        response = self.client.post('/api/timeline_post', data={
            'name': '',
            'email': 'john@example.com',
            'content': 'Hello world, I am John!'
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert 'Invalid name' in html

        # Empty content
        response = self.client.post('/api/timeline_post', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'content': ''
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert 'Invalid content' in html

        # Bad email
        response = self.client.post('/api/timeline_post', data={
            'name': 'John Doe',
            'email': 'not-an-email',
            'content': 'Hello world, I am John!'
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert 'Invalid email' in html
