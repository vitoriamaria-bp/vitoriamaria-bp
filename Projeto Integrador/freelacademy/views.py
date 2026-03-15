from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto
from .forms import ProjetoForm

# --- PÁGINAS PÚBLICAS ---
def index(request): return render(request, 'index.html')
def login_view(request): return render(request, 'login.html')
def cadastro(request): return render(request, 'cadastro.html')
def recuperar_senha(request): return render(request, 'recuperar-senha.html')
def planos(request): return render(request, 'planos.html')
def projetos(request): return render(request, 'projetos.html')
def freelancers(request): return render(request, 'freelancers.html')
def contato(request): return render(request, 'contato.html')
def faq(request): return render(request, 'faq.html')
def privacidade(request): return render(request, 'privacidade.html')
def regras(request): return render(request, 'regras.html')
def termos(request): return render(request, 'termos.html')

# --- PÁGINAS DO CLIENTE ---
def cliente_home(request):
    # Lista todos os projetos (para facilitar os testes)
    projetos = Projeto.objects.all()
    return render(request, 'cliente-home.html', {'projetos': projetos})

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            # Verifica se o utilizador está autenticado antes de o associar
            if request.user.is_authenticated:
                projeto.cliente = request.user
            projeto.save()
            return redirect('cliente_home')
    else:
        form = ProjetoForm()
    return render(request, 'cliente-novo-projeto.html', {'form': form})

def deletar_projeto(request, pk):
    # Procura o projeto pelo ID e elimina-o
    projeto = get_object_or_404(Projeto, pk=pk)
    projeto.delete()
    return redirect('cliente_home')

def cliente_buscar_freelancers(request): return render(request, 'cliente-buscar-freelancers.html')
def cliente_chat(request): return render(request, 'cliente-chat.html')
def cliente_configuracoes(request): return render(request, 'cliente-configuracoes.html')
def cliente_detalhes_projeto(request): return render(request, 'cliente-detalhes-projeto.html')
def cliente_financeiro(request): return render(request, 'cliente-financeiro.html')

# --- PÁGINAS DO FREELANCER ---
def freelancer_home(request): return render(request, 'freelancer-home.html')
def freelancer_baixar_app(request): return render(request, 'freelancer-baixar-app.html')
def freelancer_buscar_projetos(request): return render(request, 'freelancer-buscar-projetos.html')
def freelancer_carteira(request): return render(request, 'freelancer-carteira.html')
def freelancer_chat(request): return render(request, 'freelancer-chat.html')
def freelancer_configuracoes(request): return render(request, 'freelancer-configuracoes.html')
def freelancer_detalhes_projeto(request): return render(request, 'freelancer-detalhes-projeto.html')
def freelancer_portfolio(request): return render(request, 'freelancer-portfolio.html')