from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Projeto, Usuario
from .forms import ProjetoForm

# ==========================================
# PÁGINAS PÚBLICAS E AUTENTICAÇÃO
# ==========================================
def index(request): 
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        tipo = request.POST.get('perfil')
        nome = request.POST.get('nomeCompleto')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cpf = request.POST.get('cpf_cnpj')
        telefone = request.POST.get('telefone')
        
        # Validação de e-mail e CPF duplicados
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está em uso.")
            return redirect('cadastro')
        if Usuario.objects.filter(cpf_cnpj=cpf).exists():
            messages.error(request, "Este CPF/CNPJ já está cadastrado.")
            return redirect('cadastro')

        # Criação do usuário com criptografia automática de senha
        user = Usuario.objects.create_user(
            username=email, # Usamos o e-mail como login principal
            email=email,
            password=senha,
            first_name=nome,
            tipo=tipo,
            cpf_cnpj=cpf,
            telefone=telefone
        )
        messages.success(request, "Conta criada com sucesso! Por favor, faça o login.")
        return redirect('login')

    return render(request, 'cadastro.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        tipo_acesso = request.POST.get('tipoAcesso')
        
        # Tenta encontrar e validar o usuário no banco de dados
        user = authenticate(request, username=email, password=senha)
        
        if user is not None:
            # Verifica se o tipo de acesso (cliente/freelancer) bate com a conta
            if user.tipo == tipo_acesso:
                login(request, user)
                if user.tipo == 'cliente':
                    return redirect('cliente_home')
                else:
                    return redirect('freelancer_home')
            else:
                messages.error(request, f"Esta conta está registrada como {user.tipo.title()}, não como {tipo_acesso.title()}.")
        else:
            messages.error(request, "E-mail ou senha inválidos.")
            
    return render(request, 'login.html')

def recuperar_senha(request): return render(request, 'recuperar-senha.html')
def planos(request): return render(request, 'planos.html')
def projetos(request): return render(request, 'projetos.html')
def freelancers(request): return render(request, 'freelancers.html')
def contato(request): return render(request, 'contato.html')
def faq(request): return render(request, 'faq.html')
def privacidade(request): return render(request, 'privacidade.html')
def regras(request): return render(request, 'regras.html')
def termos(request): return render(request, 'termos.html')


# ==========================================
# PAINEL DO CLIENTE (Protegido por Login)
# ==========================================
@login_required(login_url='login')
def cliente_home(request):
    projetos = Projeto.objects.filter(cliente=request.user)
    return render(request, 'cliente-home.html', {'projetos': projetos})

@login_required(login_url='login')
def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.cliente = request.user
            projeto.save()
            return redirect('cliente_home')
    else:
        form = ProjetoForm()
    return render(request, 'cliente-novo-projeto.html', {'form': form})

@login_required(login_url='login')
def deletar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk, cliente=request.user)
    projeto.delete()
    return redirect('cliente_home')

@login_required(login_url='login')
def cliente_buscar_freelancers(request): return render(request, 'cliente-buscar-freelancers.html')
@login_required(login_url='login')
def cliente_chat(request): return render(request, 'cliente-chat.html')
@login_required(login_url='login')
def cliente_configuracoes(request): return render(request, 'cliente-configuracoes.html')
@login_required(login_url='login')
def cliente_detalhes_projeto(request): return render(request, 'cliente-detalhes-projeto.html')
@login_required(login_url='login')
def cliente_financeiro(request): return render(request, 'cliente-financeiro.html')


# ==========================================
# PAINEL DO FREELANCER (Protegido por Login)
# ==========================================
@login_required(login_url='login')
def freelancer_home(request): return render(request, 'freelancer-home.html')
@login_required(login_url='login')
def freelancer_baixar_app(request): return render(request, 'freelancer-baixar-app.html')
@login_required(login_url='login')
def freelancer_buscar_projetos(request): return render(request, 'freelancer-buscar-projetos.html')
@login_required(login_url='login')
def freelancer_carteira(request): return render(request, 'freelancer-carteira.html')
@login_required(login_url='login')
def freelancer_chat(request): return render(request, 'freelancer-chat.html')
@login_required(login_url='login')
def freelancer_configuracoes(request): return render(request, 'freelancer-configuracoes.html')
@login_required(login_url='login')
def freelancer_detalhes_projeto(request): return render(request, 'freelancer-detalhes-projeto.html')
@login_required(login_url='login')
def freelancer_portfolio(request): return render(request, 'freelancer-portfolio.html')