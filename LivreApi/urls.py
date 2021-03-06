from django import views
from django.urls import path
from . import views
from django.contrib import admin
from .views import Createbook, Createcat, MyTokenObtainPairView, Search
# from rest_framework import routers #router

urlpatterns = [

    path('api/books' , views.showbooks , name='books'),
    # path('api/search' , views.search , name='search'),
    path('api/books/<int:id>' , views.showbook , name='book'),
    path('api/delbook/<int:id>' , views.delbook , name='delbook'),
    path('api/userbooks/<int:id>' , views.userbooks , name='userbooks'),
    path('api/subsbooks' , views.subsbooks , name='usersbooks'),
   
   
    #category
    path('api/categorys', views.categorys_view, name='categorys'),
    path('api/categories', views.categories, name='categories'),
    path('api/category/<int:id>', views.category_view, name='category'),
    path('api/subscription/<int:id>', views.subscription_view, name='subscription'),
    path('api/unsubscription/<int:id>', views.unsubscription_view, name='unsubscription'),
    path('api/user_subscription', views.user_subscription_view, name='user_subscription'),
    path('api/add_book/' , views.add_book , name='add_book'),
    path('api/listcat' , views.listcat , name = 'listcat'),
# Login & Register
    #Register_A_New_User
        path('api/register' , views.registration_view.as_view() , name='register'),
    # Login  
        path('api/login', MyTokenObtainPairView.as_view(), name='login'),

############
# User Profile
    #Show_(Logged in)Main_User_Profile
        path('api/profile/' , views.profile , name='profile'),
    #Edit_(Logged in)Main_User_Profile
        path('api/manage_profile' , views.manage_profile , name='manage_profile'),      
    #Show_Other_User_Profile
        path('api/others_profile/<int:id>' , views.others_profile , name='others_profile'),
    #Change_image
        path('api/changeimage' , views.change_image.as_view() , name='change_image'),


############   
#Messages
    #View_Main_User_Messages
       path('api/messages/' , views.messages , name='messages'),
    #Sending_Message
        path('api/message/<int:id>' , views.message , name='message'),
        path('api/delmessage/<int:id>' , views.delmessage , name='message'),
        path('api/sentmessages' , views.sentmessages , name='sentmessage'),
        path('api/sendusers' , views.sendusers , name='sendusers'),

############    
#Books
    #Add_Book
        path('api/add_book/' , views.add_book , name='add_book'),
    #Show_Main_User_Books
        path('api/show_main_user_books/' , views.show_main_user_books , name='show_main_user_books'),
    #Show_Other_User_Books
        path('api/show_other_user_books/<int:id>' , views.show_other_user_books , name='show_other_user_books'),


############    
#Transactions
    # Excahnge_Book
        path('api/exchange_book/<int:bookid>' , views.exchange_book , name='exchange_book'),
    # Accept_Excahnging_Book
        path('api/accept_exchange/<int:exchangeid>' , views.accept_exchange , name='accept_exchange'),
    # Decline_Excahnging_Book
        path('api/decline_exchange/<int:exchangeid>' , views.decline_exchange , name='decline_exchange'),
    
    #Show_Main_User_Sent_Transactions
        path('api/user_sender_transaction/' , views.show_sender_transaction , name='show_sender_transaction'),
    #Show_Main_User_Recived_Transactions
        path('api/user_reciver_transaction/' , views.show_reciver_transaction , name='show_reciver_transaction'),
    #finish_exchange
        path('api/finishexchange/<int:exchangeid>' , views.finish_exchange , name='finis_transaction'),
    #admin urls
        path('api/admin_listing/<str:option>' ,views.admin_listing , name='admin_listing'),
        path('api/admin_operation/<str:option>' ,views.admin_operation , name='admin_operation'),
        path('api/admin_operation/<str:option>/<int:id>' ,views.admin_operation , name='admin_operation'),

        path('api/createcat/', Createcat.as_view(), name='createcat'),
        
    #Search
        path('api/search' ,Search.as_view(), name = 'search'),
    #Rate
        path('api/rate/<int:id>' ,views.rate, name='rate'),
        path('api/show_rate/<int:id>' ,views.show_rate, name='show_rate'),
        
        path('api/createbook/', Createbook.as_view(), name='createbook')
]