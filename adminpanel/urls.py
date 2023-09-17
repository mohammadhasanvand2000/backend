from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MonthlyVisitAnalytics,DailyAnalyticsAPI, WeeklyAnalyticsAPI,MonthlyVisitAnalytics, MonthlyAnalyticsAPI,OrderViewSet,ArticleViewSet,TicketRetrieveUpdateView,TicketListCreateView,OrderItemViewSet, ProductViewSet,BestsellingViewSet,Additional_fieldViewSet,Customer_commentViewSet,UserViewSet,TicketViewSet,KingCategoryViewSet


router = DefaultRouter()

router.register('', ProductViewSet)

router2 = DefaultRouter()

router2.register('', BestsellingViewSet)

router3 = DefaultRouter()

router3.register('', UserViewSet)

router4 = DefaultRouter()

router4.register('', TicketViewSet)

router5 = DefaultRouter()

router5.register('', KingCategoryViewSet)

router6 = DefaultRouter()

router6.register('', Customer_commentViewSet)

router7 = DefaultRouter()

router7.register('', Additional_fieldViewSet)

router8 = DefaultRouter()

router8.register('', OrderItemViewSet)

router9 = DefaultRouter()

router9.register('', OrderViewSet)

router10 = DefaultRouter()

router10.register('', ArticleViewSet)




urlpatterns = [
    path('products/', include(router.urls)),                                                        #  products      management
    path('bestsell/', include(router2.urls)),                                                       #  bestsells     management
    path('users/',include(router3.urls), name='users'),                                             #  users         management
    path('ticket/',include(router4.urls), name='ticket'),                                           #  tickets       management
    path('category/',include(router5.urls), name='category'),                                       #  categorys     management
    path('comment/',include(router6.urls), name='comment'),                                         #  comments      management
    path('add_field/',include(router7.urls), name='add_field'),                                     #  add_fields    management
    path('order_item',include(router8.urls), name='order_item'),                                    #  order_items   management
    path('order/',include(router9.urls), name='Order'),                                             #  orders        management
    path('ticketsuser/', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('ticketsadmin/<int:pk>/', TicketRetrieveUpdateView.as_view(), name='ticket-retrieve-update'),
    path('article/',include(router10.urls), name='Order'), 
    path('analytics/daily/', DailyAnalyticsAPI.as_view(), name='daily-analytics'),
    path('analytics/weekly/', WeeklyAnalyticsAPI.as_view(), name='weekly-analytics'),
    path('analytics/monthly/', MonthlyAnalyticsAPI.as_view(), name='monthly-analytics'),
    path('monthly-visit-analytics/', MonthlyVisitAnalytics.as_view(), name='monthly-visit-analytics'),
   

    
]
