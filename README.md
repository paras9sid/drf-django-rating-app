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

    Create Element & Access List: http://127.0.0.1:8000/api/watch/stream/

    <img width="1280" height="979" alt="all_streams" src="https://github.com/user-attachments/assets/ec3593d8-7286-4486-a9b0-ed6cc83e5824" />

    Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/

    <img width="1280" height="979" alt="stream_by_id" src="https://github.com/user-attachments/assets/0519c70d-9078-4772-b443-9a20e48ceb9b" />

7. Watch List

    Create & Access List: http://127.0.0.1:8000/api/watch/

    <img width="1280" height="983" alt="watchlist_all" src="https://github.com/user-attachments/assets/94c7a472-94d8-49f6-b5cc-9d227a6ab226" />

    Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/<int:movie_id>/

    <img width="1280" height="983" alt="watchlist_by_id" src="https://github.com/user-attachments/assets/7b6d1a5e-5e82-4085-8990-79b3bf568b56" />

9. Reviews

    Create Review For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/create/

    <img width="1280" height="983" alt="reviews_create" src="https://github.com/user-attachments/assets/4558b23c-1175-4a94-a392-a3715b5eb1ac" />

    List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/

    <img width="1280" height="983" alt="watchlist_reviews" src="https://github.com/user-attachments/assets/bf679237-bf96-4c49-a3dc-2e101d2ee606" />
   
    Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watch/reviews/<int:review_id>/

    <img width="1280" height="984" alt="review_by_id" src="https://github.com/user-attachments/assets/a0e66984-95ca-4d9d-b073-af60b3faa14f" />

11. User Review

    Access All Reviews For Specific User: http://127.0.0.1:8000/api/watch/user-reviews/?username=example
