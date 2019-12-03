
import unittest
from blog.models import User, Post
from blog import db

class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.user_wendyorengo = User(username = "wendyorengo", password = "minayojane", email="orengowendy594@gmail.com")
        self.new_post = Post(title="code", body = "coding rocks", user_id =self.user_wendyorengo.id )
    def tearDown(self):
        Post.query.delete()
        User.query.delete()



    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title, 'code')
        self.assertEquals(self.new_post.body,"coding rocks")
        self.assertEquals(self.new_post.user_id, self.user_alexmuliande.id)

    def test_save_blog(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

    def test_get_posts(self):

        self.new_post.save_blog()
        posts = Post.get_posts()
        self.assertTrue(len(posts)==1)