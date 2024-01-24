## Meu projeto de automação de dados

### Instalação e Configuração

1. Clone o repositório:
```bash
git clone https://github.com/lvgalvao/dataprojectstarterkit.git
cd dataprojectstarterkit
```
2. Configure a versão correta do Python com `pyenv`:
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```
3. Instale as dependências do projeto:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  
```

4. Rode a aplicação
```bash
task run
```

5. Rode os testes
```bash
task test
```

1. Rode a documentação
```bash
task test
```