from pathlib import Path

# Procura a sua pasta de templates correta
templates_dir = Path('freelacademy/templates')
if not templates_dir.exists():
    templates_dir = Path('templates')

contador = 0
for filepath in templates_dir.glob('**/*.html'):
    texto = filepath.read_text(encoding='utf-8')
    
    # Se encontrar a barra invertida antes da aspa (\'), ele troca só pela aspa (')
    if "\\'" in texto:
        texto_limpo = texto.replace("\\'", "'")
        filepath.write_text(texto_limpo, encoding='utf-8')
        contador += 1

print(f"✅ {contador} arquivos foram limpos e corrigidos com sucesso!")