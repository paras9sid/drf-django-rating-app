IMDB API Clone With DRF
🔗 Final Project Links (Arranged According To Usage)

Stack - 
Backend - python, Django, Django Rest Framework

#Deployed on Railway - https://www.djangoapi.online/


1. Watch - https://www.djangoapi.online/api/watch/

<img width="1920" height="1040" alt="api-watch" src="https://github.com/user-attachments/assets/bdfc61ea-6436-4de5-8ba5-595453335198" />

#Local Machine Endpoints - download zip and extract or clone the repository.

1. Admin Access

    Admin Section: https://www.djangoapi.online/dashboard/login/?next=/dashboard/

2. Accounts

    Registration: https://www.djangoapi.online/api/account/register/

    Login: https://www.djangoapi.online/api/account/login/

    Logout: https://www.djangoapi.online/api/account/logout/

4. Stream Platforms

    Create Element & Access List: https://www.djangoapi.online/api/watch/stream/

    <img width="1920" height="1040" alt="api-watch-stream" src="https://github.com/user-attachments/assets/c191a5b6-9067-4eba-b71f-5191c3ff2af8" />


    Access, Update & Destroy Individual Element: https://www.djangoapi.online/api/watch/stream/<int:streamplatform_id>/

6. Watch List

    Create & Access List: https://www.djangoapi.online/api/watch/

    Access, Update & Destroy Individual Element: https://www.djangoapi.online/api/watch/<int:movie_id>/

7. Reviews

    Create Review For Specific Movie: https://www.djangoapi.online/api/watch/<int:movie_id>/reviews/create/

    List Of All Reviews For Specific Movie: https://www.djangoapi.online/api/watch/<int:movie_id>/reviews/

    <img width="1920" height="1040" alt="api-watch-reviews" src="https://github.com/user-attachments/assets/7bb94356-0eb1-401d-8989-d493eef06bb0" />
   
    Access, Update & Destroy Individual Review: https://www.djangoapi.online/api/watch/reviews/<int:review_id>/

9. User Review

    Access All Reviews For Specific User: https://www.djangoapi.online/api/watch/user-reviews/?username=example
