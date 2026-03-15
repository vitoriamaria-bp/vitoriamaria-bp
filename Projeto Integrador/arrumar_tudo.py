import os
import re
from pathlib import Path

def arrumar_projeto():
    print("Iniciando correção automática do projeto...")
    
    # 1. ARRUMAR O SETTINGS.PY (Caminho do CSS)
    settings_path = Path('setup/settings.py')
    if settings_path.exists():
        conteudo = settings_path.read_text(encoding='utf-8')
        
        # Limpa qualquer configuração antiga de STATICFILES_DIRS para evitar erros
        conteudo = re.sub(r'STATICFILES_DIRS\s*=\s*\[.*?\]', '', conteudo, flags=re.DOTALL)
        
        # Adiciona a configuração exata apontando para a pasta 'assets'
        config_estaticos = "\n# Configuração inserida automaticamente para carregar o CSS\nSTATICFILES_DIRS = [\n    BASE_DIR / 'templates' / 'static' / 'assets',\n]\n"
        conteudo += config_estaticos
        
        settings_path.write_text(conteudo, encoding='utf-8')
        print("✅ setup/settings.py atualizado (Caminho do CSS corrigido).")
    else:
        print("❌ Erro: Arquivo setup/settings.py não encontrado.")

    # 2. ARRUMAR OS LINKS NOS HTMLS
    templates_dir = Path('templates')
    
    # Dicionário que mapeia o nome do arquivo antigo para o nome da rota no Django
    mapa_urls = {
        "index.html": "index",
        "login.html": "login",
        "cadastro.html": "cadastro",
        "recuperar-senha.html": "recuperar_senha",
        "planos.html": "planos",
        "projetos.html": "projetos",
        "freelancers.html": "freelancers",
        "contato.html": "contato",
        "faq.html": "faq",
        "privacidade.html": "privacidade",
        "regras.html": "regras",
        "termos.html": "termos",
        "cliente-home.html": "cliente_home",
        "cliente-novo-projeto.html": "criar_projeto",
        "cliente-buscar-freelancers.html": "cliente_buscar_freelancers",
        "cliente-chat.html": "cliente_chat",
        "cliente-configuracoes.html": "cliente_configuracoes",
        "cliente-detalhes-projeto.html": "cliente_detalhes_projeto",
        "cliente-financeiro.html": "cliente_financeiro",
        "freelancer-home.html": "freelancer_home",
        "freelancer-baixar-app.html": "freelancer_baixar_app",
        "freelancer-buscar-projetos.html": "freelancer_buscar_projetos",
        "freelancer-carteira.html": "freelancer_carteira",
        "freelancer-chat.html": "freelancer_chat",
        "freelancer-configuracoes.html": "freelancer_configuracoes",
        "freelancer-detalhes-projeto.html": "freelancer_detalhes_projeto",
        "freelancer-portfolio.html": "freelancer_portfolio"
    }

    if templates_dir.exists():
        arquivos_html = list(templates_dir.glob('**/*.html'))
        for filepath in arquivos_html:
            texto_html = filepath.read_text(encoding='utf-8')
            
            # Substitui cada referência de href pelo formato Django
            for arquivo_antigo, nome_rota in mapa_urls.items():
                padrao = r'href=(["\'])\.?/?' + re.escape(arquivo_antigo) + r'\1'
                substituto = f'href="{{% url \'{nome_rota}\' %}}"'
                texto_html = re.sub(padrao, substituto, texto_html)
                
            filepath.write_text(texto_html, encoding='utf-8')
        
        print(f"✅ {len(arquivos_html)} arquivos HTML foram varridos e tiveram seus links atualizados.")
    else:
        print("❌ Erro: Pasta 'templates' não encontrada.")

    print("\nTudo pronto! O CSS e a navegação devem funcionar agora.")

if __name__ == '__main__':
    arrumar_projeto()