IMDB API Clone With DRF
🔗 Final Project Links (Arranged According To Usage)

Stack - 
Backend - python, Django, Django Rest Framework

#Deployed - Railway Cloud

Home - https://www.djangoapi.online

<img width="1280" height="979" alt="Home" src="https://github.com/user-attachments/assets/1c1552a5-554e-45e4-aac6-2567d47a5214" />

1. Watch - https://www.djangoapi.online/api/watch/stream/

<img width="1280" height="987" alt="Django_drf_api" src="https://github.com/user-attachments/assets/21abdf18-e482-4928-889a-136e3f00a352" />

#Local Machine Endpoints - download zip and extract or clone the repository.

1. Admin Access

   Admin Section: https://www.djangoapi.online/dashboard/login/?next=/dashboard/

   <img width="1280" height="987" alt="api_db" src="https://github.com/user-attachments/assets/1eba2ec8-5fcc-41a4-b147-e83b4b0db991" />

3. Accounts

   Registration: http://127.0.0.1:8000/api/account/register/

   <img width="1280" height="710" alt="api_register" src="https://github.com/user-attachments/assets/9cb9f9ac-b321-4345-9dfe-cb3147adad73" />

    Login: http://127.0.0.1:8000/api/account/login/

    <img width="1280" height="979" alt="login" src="https://github.com/user-attachments/assets/0a2c03d0-49df-4db8-a4e5-bb7a9d09679b" />

    Logout: http://127.0.0.1:8000/api/account/logout/

    <img width="1280" height="979" alt="Logout" src="https://github.com/user-attachments/assets/473afb3d-1a49-44c8-bad9-7cd168de7313" />


5. Stream Platforms

    Create Element & Access List: https://www.djangoapi.online/api/watch/stream/

    <img width="1280" height="984" alt="all_stream" src="https://github.com/user-attachments/assets/4689fa79-63c6-4f9f-8315-fc3058318b08" />

    Access, Update & Destroy Individual Element: https://www.djangoapi.online/api/watch/stream/<int:streamplatform_id>/

    <img width="1280" height="984" alt="stream_by_id" src="https://github.com/user-attachments/assets/3aa2b096-ebfb-446b-b3a6-5a02aa840f7b" />

7. Watch List

    Create & Access List: https://www.djangoapi.online/api/watch/

    <img width="1280" height="984" alt="all_watchlist" src="https://github.com/user-attachments/assets/42398433-6812-485e-ae9c-cbfe99158233" />

    Access, Update & Destroy Individual Element: https://www.djangoapi.online/api/watch/<int:movie_id>/

    <img width="1280" height="984" alt="watchlist_by_id" src="https://github.com/user-attachments/assets/b40dfcad-1b05-4449-b0ac-b06333947007" />

9. Reviews

    Create Review For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/create/

    <img width="1280" height="983" alt="reviews_create" src="https://github.com/user-attachments/assets/4558b23c-1175-4a94-a392-a3715b5eb1ac" />

    List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/

    <img width="1280" height="983" alt="watchlist_reviews" src="https://github.com/user-attachments/assets/bf679237-bf96-4c49-a3dc-2e101d2ee606" />
   
    Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watch/reviews/<int:review_id>/

    <img width="1280" height="984" alt="review_by_id" src="https://github.com/user-attachments/assets/a0e66984-95ca-4d9d-b073-af60b3faa14f" />

11. User Review

    Access All Reviews For Specific User: http://127.0.0.1:8000/api/watch/user-reviews/?username=example
