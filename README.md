# MNIST_Draw 🖌

## Introdução

O *MNIST_Draw* é uma pequena biblioteca a qual permite o usuário desenhar em uma célula do *Google Colab*.

Seu uso pretendido é para trabalhos que envolvam a biblioteca de números manuscritos ***MNIST***. Por essa razão, suas configurações padrão trazem parâmetros (que podem ser alterados) como:

- Cor de fundo **preta** e cor do traço **branca**;
- Resize automático para **28x28 pixels** após o salvamento;
- Conversão para escala de cinza após o salvamento.

Abaixo, é possível observar um pequeno exemplo de aplicação da biblioteca no próprio *Colab*:

![](docs/assets/example.png)

<br>

## Como utilizar

Para utilizar a biblioteca, importe o repositório em uma **célula de código** do *Colab*:

```bash
!git clone https://github.com/eduardodpms/MNIST_Draw
```

Depois, também em uma célula de código, execute o arquivo `draw.py` para que o *Colab* o reconheça:

```bash
%run /content/MNIST_Draw/draw.py
```

Por fim, chame a função `draw` com os parâmetros desejados:

```bash
draw(output='drawing.png')
```

Assim, surgirá um *canvas* no qual você poderá **desenhar** e **alterar a largura do traço**, mais três botões:

- ***Salvar:*** Salva a imagem no caminho desejado e interrompe a execução da célula (e do desenho);
- ***Limpar:*** Limpa o *Canvas*;
- ***Sair:*** Interrompe a execução da célula (e do desenho).

---

**Obs:** Atente-se ao fato de que os botões só terão efeito enquanto a célula estiver em execução. Ao clicar em **"Salvar"** ou **"Sair"**, ela será interrompida e, caso deseje desenhar novamente, é preciso executar a célula de novo.
