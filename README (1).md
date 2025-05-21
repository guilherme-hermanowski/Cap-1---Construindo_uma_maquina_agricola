
# Projeto de Monitoramento de Solo com ESP32

Este projeto simula a leitura de sensores de **umidade**, **temperatura**, **pH**, **fósforo** e **potássio** em um ambiente de cultivo, utilizando um ESP32. A lógica de controle foi desenvolvida em C++ e pode ser simulada no ambiente Wokwi.

## 📁 Conteúdo do Projeto

- `main.cpp`: Código fonte funcional em C++ para ESP32.
- `circuito.png`: Imagem do circuito montado no simulador Wokwi.
- `README.md`: Este documento explicativo.

---

## ⚙️ Componentes e Conexões

- **Sensor Fosforo**:
  - Conexão: pino 23
- **Sensor Potassio**:  
  - Conexão: pino 22
- **Sensor LDR**: 
  - Conexão: 35
  - Responsável por simular a coleta do PH.
- **Sensor DHT22**: 
  - Conexão: 15
  - Responsável por coleta de temperatura e umidade.
- **LED (Relé simulado)**: 
  - Conexão: pino 2
  - Utilizado como atuador da bomba de irrigação.
  

---

## 🧠 Lógica de Funcionamento


- **Observações:**
  - Segundo a liberdade e criatividade da lógica de coleta dos sensores, definimos que o para a simulação, o sistema evita logs repetitivos: só gera nova saída quando há mudança no estado dos sensores **LDR (Ph), Botões (Fosforo e Potassio)**.
  - A coleta do sensor de Temperatura e Umidade é mostrado toda vez que há alterações em alguns desses sensores (para não poluir o monitor e também facilitar validação da avaliação.
  - A coleta do sensor do Relé, simulando a bomba de irrigação é feita automaticamente só com a alteração de umidade no sensor DTH22.
  - O valor de pH é tratado com `fabs()` para considerar desvios mínimos.
  - Ao final do Loop com alteração de parametros do sensor LDR ou botão, o log é gerado coletando de todos os sensores (até os que não foram alterados, para gerar carga na cópia para execução do entregável 2) - Simulando uma Trigger para disparo de log / coleta

- O sistema lê os botões de **fósforo** e **potássio**. Quando pressionados, gera valores aleatórios simulando a presença em mol desses nutrientes.
- O valor de **pH** é calculado com base em um valor analógico lido pelo sensor LDR
- O sensor DHT22 fornece leitura de **temperatura** e **umidade**.
- A **bomba de irrigação (LED)** é acionada ou desligada conforme o valor da umidade:
  - **≥ 40%**: bomba desligada (LED Vermelho Ligado)
  - **< 40%**: bomba ligada (LED Verde Ligado)
- Todos os dados são exibidos no monitor serial, com um bloco especialmente formatado para facilitar a cópia e posterior uso em scripts Python.

---

## 📤 Exemplo de Saída no Serial

```
Presença Fosforo: 68.32
Presença Potassio: 92.14
Ph: 5.89
Temp (°C): 23.55
Humidity (%): 35.7

============================================ COPIAVEL PARA SCRIPT PYTHON ============================================

log,68.32,92.14,5.89,23.55,35.7

**Sendo (seria a data no projeto real por exemplo), (Fosforo), (Potassio), (Ph), (Temp), (Umidade)

=====================================================================================================================
```


