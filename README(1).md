# Armazenamento de Dados em Banco SQL com Python

# FIAP - Inteligência artificial e data science

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

## Nome do grupo
25

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Guilherme Campos Hermanowski </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Gabriel Viel </a>
- <a href="https://www.linkedin.com/company/inova-fusca"> Matheus Alboredo Soares</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Jonathan Willian Luft </a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>


# Script Python de Armazenamento e Simulação de Dados Sensoriais

Este projeto complementa a Fase 2 do sistema de monitoramento agrícola, integrando dados do ESP32 com operações de banco de dados simuladas via Python. O objetivo é demonstrar, através de comandos DML, o funcionamento completo do ciclo de CRUD.

## 📌 Objetivos da Fase

- Copiar dados enviados via Monitor Serial (log do ESP32).
- Processar os dados em Python e gerar comandos SQL correspondentes.
- Simular operações de **INSERT**, **SELECT**, **UPDATE** e **DELETE** no banco `FarmTech_BD`.
- Justificar a estrutura com base no MER (Modelo Entidade-Relacionamento) da Fase 2.

---

## 🧠 Justificativa da Estrutura de Dados

As tabelas utilizadas (`NPK_coleta`, `PH_coleta`, `Umidade_coleta`) refletem diretamente o MER da Fase 2, no qual temos:

- **Sensores** identificados por `ID_Sensor` com suas respectivas categorias (NPK, PH, Umidade).
- Cada tipo de sensor gera coletas distintas, armazenadas em tabelas específicas para permitir maior organização e desempenho.
- O relacionamento com `Sensores` é feito via chave estrangeira `ID_Sensor`.
- O script manipula os dados conforme essa modelagem, garantindo integridade e rastreabilidade.

---

## 💻 Como Funciona

- **Observações:**
  - As operações de DML são feitas confome a seguinte lógica:
    - Ao colar o registro de log copiado do Serial Monitor, é possível escolher qual comando será gerado (SELECT, INSERT, UPDATE e DELETE) e de cada tabela correspondente os valores de log.
  - Existe um menu para selecionar o comando desejado, além de disponibilizar novos dados de log quando a operação for UPDATE.
  - Nas intruções SQL de SELECT, UPDATE e DELETE, os valores dos logs copiados foram utilizados para filtro na consulta (WHERE)

  
1. O usuário cola no terminal a linha copiada do Serial Monitor, por exemplo:  
   ```
   log,58.44,77.13,6.45,24.75,37.2
   ```

2. O script converte os dados e apresenta um menu de operações SQL com base no log:
   - `SELECT` para consulta.
   - `INSERT` para simular armazenamento.
   - `UPDATE` com novos valores digitados manualmente.
   - `DELETE` para remover registros com base no log.

3. Cada operação gera os comandos SQL correspondentes, prontos para execução em um ambiente SQL Server.


---

## 🧪 Exemplo de Operação: SELECT, INSERT , UPDATE e DELETE

```sql
INSERT INTO NPK_coleta (ID_coleta_nutriente, Dt_log, ID_Sensor, Tipo_desc, Nitrogenio, Fosforo, Potassio, Unidades)
VALUES (1,'2025-05-20 20:45:15', 1, 'Botao RED/GREEN', 0.00, 58.44, 77.13, 'mol');
```

---

## 🔗 Relacionamento com o MER

O código respeita a modelagem relacional da base, mantendo os vínculos entre `Sensores` e suas respectivas coletas (mesmo que com valores estaticos na simulação, ex:Sensor_ID, e ID das coletas (PK das tabelas de log dos sensores.
Todas as operações realizadas refletem transações reais que seriam executadas no banco `FarmTech_BD`.





## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
