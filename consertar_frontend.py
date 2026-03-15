import glob, pathlib, re

# Define o caminho da pasta de templates
p = pathlib.Path("freelacademy/templates") 

for f in glob.glob(str(p / "*.html")):
    txt = pathlib.Path(f).read_text(encoding="utf-8")
    
    # Adiciona a tag load static se não existir
    if not txt.strip().startswith("{% load static %}"):
        txt = "{% load static %}\n" + txt
    
    # Troca os caminhos antigos pelo formato Django
    txt = re.sub(r'href="assets/css/([^"]+)"', r'href="{% static \'css/\g<1>\' %}"', txt)
    txt = re.sub(r'href="assets/(css|js|img)/([^"]+)"', r'href="{% static \'\g<1>/\g<2>\' %}"', txt)
    txt = re.sub(r'src="assets/(js|img)/([^"]+)"', r'src="{% static \'\g<1>/\g<2>\' %}"', txt)
    
    # Grava o ficheiro corrigido
    pathlib.Path(f).write_text(txt, encoding="utf-8")

print("Frontend padronizado com sucesso!")