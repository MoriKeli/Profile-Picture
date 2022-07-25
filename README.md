# Profile-Picture
How to update profile picture using django

#### Technologies used:
  - HTML
  - CSS
  - Bootstrap
  - Django
  
 #### Explanation
 ##### 1. In your models.py, create a user profile model.

![model](https://user-images.githubusercontent.com/78599959/180754896-2ce1fe31-6a4a-40ac-8d68-262535ec812c.png)

 
 ##### 2. Configure your settings with a media folder, where the profile will be 
 stored. Create a folder named MediaFiles otherwise an error will be raised. The folder must have the "default.jpg"
 in Profile model or an error will be raised.

![settings](https://user-images.githubusercontent.com/78599959/180754922-b8d62205-e786-4b4a-8b17-47b0ec6fc973.png)

 ##### 3. Provide a url for django to locate the profile picture.
 
  ![urls](https://user-images.githubusercontent.com/78599959/180755528-57cd82af-ce5d-40b4-8036-bfe7001cbb48.png)

 ##### 4. To change profile picture use django's User model. A user can only have one profile (one user, one profile) thus we need to create a one-to-one relationship.
 
 
 ![model](https://user-images.githubusercontent.com/78599959/180755557-7febc44c-2bd2-4b24-bcca-7f5c49150370.png)

 #### 5. Create signals.py file in your app. Once the user creates an account, we 
 need to fill in "user = models.OneToOneField()" in model Profile with registered user's username.

![signal](https://user-images.githubusercontent.com/78599959/180755603-2eab5168-9cac-4491-a740-9a19e6be63d3.png)
