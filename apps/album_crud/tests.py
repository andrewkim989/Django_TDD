from django.test import TestCase, Client
from .models import *

class AlbumTest(TestCase):
    def test_index(self):
        c = Client()
        idx_response = c.get("/")
        self.assertEqual(idx_response.status_code, 200)
        create_response = c.get("/album/create")
        self.assertEqual(create_response.status_code, 302)

    def test_model_creation(self):
        a = Album.objects.create(title = "Testing Time", artist = "The Pythons", year = 2018)
        self.assertEqual(a.title, "Testing Time")
        self.assertEqual(a.artist, "The Pythons")
        self.assertEqual(a.year, 2018)
    
    @classmethod
    def setUpTestData(cls):
        Album.objects.create(title = "A Test Album", artist = "The Pythons", year = 2200)
    
    def test_model_get(self):
        a = Album.objects.get(id = 1)
        self.assertEqual(a.id, 1)
        self.assertIsInstance(a, Album)

    def test_model_edit(self):
        a = Album.objects.first()
        a.title = "EditedTitle"
        a.artist = "Django Doug"
        a.year = 1999
        a.save()
        edited_a = Album.objects.first()
        self.assertEqual(edited_a.title, "EditedTitle")
        self.assertEqual(edited_a.artist, "Django Doug")
        self.assertEqual(edited_a.year, 1999)

    def test_model_delete(self):
        num_deleted = Album.objects.get(id = 1).delete()[0]
        self.assertEqual(num_deleted, 1)

    def test_view_create(self):
        c = Client()
        post_data = {
            "title": "Testing Views",
            "artist" : "Danger Django",
            "year": 2017
        }
        response = c.post("/album/create", post_data)
        self.assertEqual(response.status_code, 302)
        newly_created_album = Album.objects.last()
        self.assertEqual(newly_created_album.title, post_data["title"])
        self.assertEqual(newly_created_album.artist, post_data["artist"])
        self.assertEqual(newly_created_album.year, post_data["year"])
    
    def test_context(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.context["answer"], 42)

    def test_view_edit(self):
        c = Client()
        post_data = {
            "title": "A Test Edit",
            "artist" : "Test Artist Edit",
            "year": 3099
        }
        response = c.post("/album/1/edit", post_data)

        self.assertEqual(response.status_code, 302)
        edited = Album.objects.get(id = 1)
        self.assertEqual(edited.title, post_data["title"])
        self.assertEqual(edited.artist, post_data["artist"])
        self.assertEqual(edited.year, post_data["year"])
    
    def test_view_delete(self):
        c = Client()
        response = c.get("/album/1/delete")

        self.assertEqual(response.status_code, 302)
        #num_deleted = Album.objects.get(id = 1).delete()[0]
        #self.assertEqual(num_deleted, 1)
        a = Album.objects.all().filter(id = 1)
        self.assertEqual(len(a), 0)
        self.assertFalse(a)

    def test_view_read(self):
        c = Client()
        response = c.get("/album/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["album"].id, 1)
        self.assertEqual(response.context["album"].title, "A Test Album")
        self.assertEqual(response.context["album"].artist, "The Pythons")
        self.assertEqual(response.context["album"].year, 2200)

class UserTest(TestCase):
    def test_model_create(self):
        user = User.objects.create(first_name = "Twilight", last_name = "Sparkle", 
        email = "purplesmart@eq.net", password = "bookpony")
        self.assertEqual(user.first_name, "Twilight")
        self.assertEqual(user.last_name, "Sparkle")
        self.assertEqual(user.email, "purplesmart@eq.net")
        self.assertEqual(user.password, "bookpony")

    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name = "Rainbow", last_name = "Dash", 
        email = "20cooler@eq.net", password = "dashie")
    
    def test_model_get(self):
        u = User.objects.get(id = 1)
        self.assertEqual(u.id, 1)
        self.assertIsInstance(u, User)
        self.assertEqual(u.first_name, "Rainbow")

    def test_model_edit(self):
        u = User.objects.get(id = 1)
        u.first_name = "Derpy"
        u.last_name = "Hooves"
        u.email = "derp@eq.net"
        u.password = "muffins"
        u.save()
        edited_u = User.objects.get(id = 1)
        self.assertEqual(edited_u.first_name, "Derpy")
        self.assertEqual(edited_u.last_name, "Hooves")
        self.assertEqual(edited_u.email, "derp@eq.net")
        self.assertEqual(edited_u.password, "muffins")

    def test_model_delete(self):
        num = User.objects.get(id = 1).delete()[0]
        self.assertEqual(num, 1)

        user = User.objects.all().filter(id = 1)
        self.assertFalse(user)

    def test_view_new(self):
        c = Client()
        data = {
            "first_name": "Princess",
            "last_name": "Luna",
            "email": "nightprincess@eq.net",
            "password": "moonpony"
        }

        response = c.post("/user/new", data)
        self.assertEqual(response.status_code, 302)
        new_user = User.objects.last()
        self.assertEqual(new_user.first_name, data["first_name"])
        self.assertEqual(new_user.last_name, data["last_name"])
        self.assertEqual(new_user.email, data["email"])
        self.assertEqual(new_user.password, data["password"])
    
    def test_view_edit(self):
        c = Client()
        editdata = {
            "first_name": "Autumn",
            "last_name": "Blaze",
            "email": "happykirin@eq.net",
            "password": "bestkirin"
        }
        response = c.post("/user/1/edit", editdata)

        self.assertEqual(response.status_code, 302)
        edit = User.objects.get(id = 1)
        self.assertEqual(edit.first_name, editdata["first_name"])
        self.assertEqual(edit.last_name, editdata["last_name"])
        self.assertEqual(edit.email, editdata["email"])
        self.assertEqual(edit.password, editdata["password"])

    def test_view_delete(self):
        c = Client()
        response = c.get("/user/1/delete")

        self.assertEqual(response.status_code, 302)
        u = User.objects.all().filter(id = 1)
        self.assertEqual(len(u), 0)
        self.assertFalse(u)
    
    def test_view_read(self):
        c = Client()
        response = c.get("/user/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].id, 1)
        self.assertEqual(response.context["user"].first_name, "Rainbow")
        self.assertEqual(response.context["user"].last_name, "Dash")
        self.assertEqual(response.context["user"].email, "20cooler@eq.net")
        self.assertEqual(response.context["user"].password, "dashie")