# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:17:28 2024

@author: satya
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ensure you have a view called 'index'
]
