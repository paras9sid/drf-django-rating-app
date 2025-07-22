from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):

    # withpout setup - 401 error- test case F
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # adding elemnt to have something in streamplatform list - not empty list
        self.stream = models.StreamPlatform.objects.create(name="netflix",
                                                        about="#1 ott platform", 
                                                        website="https://netflix.com"
                                                        )

    def test_streamplatform_create(self):
        
        data = {
            "name": "netflix",
            "about": "#1 ott platform",
            "website": "https://netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #homework - put and delete request
    # del 403 req 0- permissionss set
    # def test_streamplatform_del(self):
    #     response = self.client.delete(reverse('streamplatform-detail', args=(self.stream.id, )))
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class WatchlistTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # adding elemnt to have something in streamplatform list - not empty list
        self.stream = models.StreamPlatform.objects.create(name="netflix",
                                                        about="#1 ott platform", 
                                                        website="https://netflix.com"
                                                        )
        
        self.watchlist = models.WatchList.objects.create(platform=self.stream,
                                                        title="Example Movie",
                                                        storyline="Example Story",
                                                        is_active=True
                                                        )

    def test_watchlist_create(self):
        data={
            "platform": self.stream,
            "title": "Example Movie",
            "storyline": "Example Story",
            "is_active": True
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response=self.client.get(reverse("movie-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_watchlist_ind(self):
        response=self.client.get(reverse("movie-detail", args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, "Example Movie")

    #put and delete - homework
    # def test_watchlist_update(self):
    #     # updated data
    #     data={
    #         "platform": self.stream,
    #         "title": "Example Movie-updated",
    #         "storyline": "Example Story-updated",
    #         "is_active": False
    #     }
    #     response = self.client.put(reverse("movie-detail", args=(self.watchlist.id, )), data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_del(self):
        response = self.client.delete(reverse('movie-detail', args=(self.watchlist.id, )))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ReviewTestCase(APITestCase):

    def setUp(self):
        #user created
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # stream platform created
        # adding elemnt to have something in streamplatform list - not empty list
        self.stream = models.StreamPlatform.objects.create(name="netflix",
                                                        about="#1 ott platform", 
                                                        website="https://netflix.com"
                                                        )
        #watchlist created
        self.watchlist = models.WatchList.objects.create(platform=self.stream,
                                                        title="Example Movie",
                                                        storyline="Example Story",
                                                        is_active=True
                                                        )
        #before review put request
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream,
                                                        title="Example Movie",
                                                        storyline="Example Story",
                                                        is_active=True
                                                        )
        
        # review manually created
        self.review = models.Review.objects.create(review_user=self.user,
                                                rating=5,
                                                description="Great Movie!",
                                                watchlist=self.watchlist2,
                                                is_active=True
                                                )
        
    def test_review_create(self):
        data = {
            "review_user" : self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "is_active": True
        }

        response = self.client.post(reverse("review-create", args=(self.watchlist.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)
        # self.assertEqual(models.Review.objects.get().rating, 5)

        response = self.client.post(reverse("review-create", args=(self.watchlist.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #add a review as unauthenticated user
    def test_review_create_unauth(self):
        data = {
            "review_user" : self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "is_active": True
        }
        #no user logged in - 
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse("review-create", args=(self.watchlist.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        # updated data
        data = {
            "review_user" : self.user,
            "rating": 4,
            "description": "Great Movie!- updated!",
            "watchlist": self.watchlist,
            "is_active": False
        }
        response = self.client.put(reverse("review-detail", args=(self.review.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_ind(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #HW - delete request check
    def test_review_del(self):
        response = self.client.delete(reverse('review-detail', args=(self.review.id, )))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_review_user(self):
        response = self.client.get('/api/watch/user-reviews/?username=' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

