from django.urls import path
from . import views

urlpatterns = [
    # --- Públicas ---
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('recuperar-senha/', views.recuperar_senha, name='recuperar_senha'),
    path('planos/', views.planos, name='planos'),
    path('projetos/', views.projetos, name='projetos'),
    path('freelancers/', views.freelancers, name='freelancers'),
    path('contato/', views.contato, name='contato'),
    path('faq/', views.faq, name='faq'),
    path('privacidade/', views.privacidade, name='privacidade'),
    path('regras/', views.regras, name='regras'),
    path('termos/', views.termos, name='termos'),

    # --- Cliente ---
    path('cliente/home/', views.cliente_home, name='cliente_home'),
    path('cliente/novo-projeto/', views.criar_projeto, name='criar_projeto'),
    path('projeto/deletar/<int:pk>/', views.deletar_projeto, name='deletar_projeto'),
    path('cliente/buscar-freelancers/', views.cliente_buscar_freelancers, name='cliente_buscar_freelancers'),
    path('cliente/chat/', views.cliente_chat, name='cliente_chat'),
    path('cliente/configuracoes/', views.cliente_configuracoes, name='cliente_configuracoes'),
    path('cliente/detalhes-projeto/', views.cliente_detalhes_projeto, name='cliente_detalhes_projeto'),
    path('cliente/financeiro/', views.cliente_financeiro, name='cliente_financeiro'),

    # --- Freelancer ---
    path('freelancer/home/', views.freelancer_home, name='freelancer_home'),
    path('freelancer/baixar-app/', views.freelancer_baixar_app, name='freelancer_baixar_app'),
    path('freelancer/buscar-projetos/', views.freelancer_buscar_projetos, name='freelancer_buscar_projetos'),
    path('freelancer/carteira/', views.freelancer_carteira, name='freelancer_carteira'),
    path('freelancer/chat/', views.freelancer_chat, name='freelancer_chat'),
    path('freelancer/configuracoes/', views.freelancer_configuracoes, name='freelancer_configuracoes'),
    path('freelancer/detalhes-projeto/', views.freelancer_detalhes_projeto, name='freelancer_detalhes_projeto'),
    path('freelancer/portfolio/', views.freelancer_portfolio, name='freelancer_portfolio'),
]