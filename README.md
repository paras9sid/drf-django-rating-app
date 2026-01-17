IMDB API Clone With DRF
🔗 Final Project Links (Arranged According To Usage)

Stack - 
Backend - python, Django, Django Rest Framework

#Deployed - www.pythonanywhere.com

1. Watch - https://siddharth108.pythonanywhere.com/api/watch/


#Local Machine Endpoints - download zip and extract or clone the repository.

1. Admin Access

    Admin Section: http://127.0.0.1:8000/dashboard/

2. Accounts

    Registration: http://127.0.0.1:8000/api/account/register/

    Login: http://127.0.0.1:8000/api/account/login/

    Logout: http://127.0.0.1:8000/api/account/logout/

4. Stream Platforms

    Create Element & Access List: http://127.0.0.1:8000/api/watch/stream/

    Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/

5. Watch List

    Create & Access List: http://127.0.0.1:8000/api/watch/

    Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/<int:movie_id>/

6. Reviews

    Create Review For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/create/

    List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/
   
    Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watch/reviews/<int:review_id>/

7. User Review

    Access All Reviews For Specific User: http://127.0.0.1:8000/api/watch/user-reviews/?username=example
