# Inferindo a altura da nossa comunidade

Projeto usando dados de nossa comunidade na [Twitch](https://www.twitch.tv/teomewhy) para criar um algoritmo de aprendizado de máquina com o intuito de prever a altura de uma pessoa com base em algumas perguntas.

Sinta-se livre para compartilhar e divulgar este material de forma gratuíta, referenciando os autores e contribuidores do projeto. Ressaltamos a **proibição** da comercialização deste material, sob a licença [_Creative Commons BY-NC-SA 3.0 BR_](https://creativecommons.org/licenses/by-nc-sa/3.0/br/).

<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" alt="" width="200">

## Dados

Os dados foram obtidos por meio de um [questionário](https://forms.gle/tmQR2bKC7krdEBSL6) criado no google forms, coletando as respostas da galera que respondeu. As perguntas foram criadas a partir de insights durante uma [live](https://www.twitch.tv/teomewhy).

**Não foram coletados dados que permitam a identificação dos respondentes.**

## Modelo

Com os dados em mãos partimos para o treinamento do modelo de Machine Learning.

Por amor a simplicidade, realizamos um pipeline simples com as seguintes etapas:
* imputação de valores missings para variáveis categóricas (fill='Missing');
* imputação de valores missings para variáveis numéricas (fill=-999);
* OneHotEncode para variáveis categóricas;
* Modelo de Árvore de Decisão;

## Preparação do ambiente

Você pode rodar este experimento em sua própria máquina usando o Dockerfile. Basta realizar o builda da imagem e depois executála:

### Build

```bash
docker build -t alturalit .
```

### Execução

```bash
docker run --rm -ti -p 8501:8501 alturalit
```

## Predições

Basta acessar o endereço [`http://localhost:8501/`](http://localhost:8501/) em seu navegador para brincar com nossa calculadora de idade.