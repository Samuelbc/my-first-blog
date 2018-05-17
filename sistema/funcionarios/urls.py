from django.urls import path
from . import views




app_name = "funcionarios"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('addcomp/', views.EntComp.as_view(), name='entrada_comportamento'),
    path('addrend/', views.EntRend.as_view(), name='entrada_rendimento'),
    path('adderro/', views.EntErro.as_view(), name='entrada_erro'),
    path('<str:func_nome>/', views.BasicFuncView.as_view(), name='basic_func'),
    path('<str:func_nome>/comportamento', views.FuncComportamento.as_view(), name='comportamento'),
    path('<str:func_nome>/erros', views.FuncErro.as_view(), name='erros'),
    path('<str:func_nome>/rendimento', views.FuncRendimento.as_view(), name='rendimento')
]
