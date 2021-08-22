from django.urls import path

from . import views

urlpatterns=[
	path('', views.home, name='home'),
	path('contact/', views.contact, name='contact'),
	path('terms/', views.terms, name='terms'),
	path('faq/', views.faq, name='faq'),
	path('privacy/', views.privacy, name='privacy'),
	path('readmore/', views.readmore, name='readmore'),
	path('about/', views.about, name='about'),
	path('signup/', views.signup, name='signup'),
	path('signin/', views.signin, name='signin'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('requestwithdrawal/', views.requestwithdrawal, name='requestwithdrawal'),
	path('plans/', views.plans, name='plans'),
	path('depositeform/', views.depositeform, name='depositeform'),
	path('deposite/', views.deposite, name='deposite'),
	path('account_settings/', views.account_settings, name='account_settings'),
	path('payments/create/<pk>', views.create_payment, name='create_payment'),
    path('payment/invoice/<pk>',views.track_invoice, name='track_payment'),
    path('payments/receive/', views.receive_payment, name='receive_payment'),
	path('logout/', views.logoutuser, name='logout'),
]