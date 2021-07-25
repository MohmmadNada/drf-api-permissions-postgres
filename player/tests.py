from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import SuperPlayer

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username ='testplayeruser', password='password')
        test_user.save()
        
        test_player = SuperPlayer.objects.create(
            name = 'naymar',
            score = 88,
            country = 'Brazil',
            addBy = test_user
        )
        test_player.save()

    def test_blog_content(self):
        player = SuperPlayer.objects.get(id=1)
        actual_name = str(player.name)
        actual_score = player.score
        actual_country = str(player.country)
        actual_addby = str(player.addBy)
        # print('actual_addby =>>>>>>>>>',type(actual_addby),'=> ',actual_addby)
        self.assertEqual(actual_name, 'naymar')
        self.assertEqual(actual_score, 88)
        self.assertEqual(actual_country, 'Brazil')
        self.assertEqual(actual_addby,'testplayeruser')