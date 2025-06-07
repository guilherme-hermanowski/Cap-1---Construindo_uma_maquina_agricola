
//define algumas conexões de pinos, como ambos botões e também o Led do rele.
#define BUTTON_FOSFORO 23
#define BUTTON_POTASSIO 22
#define LED_RELE 2

//Bibliotecas para utilização de funções e também a biblioteca do Sensor DTH22 para ESP
#include "DHTesp.h"
#include <math.h>

//Declarando alguns valores e definindo o pin de conexão do sensor DTH22
const int DHT_PIN = 15;
const float GAMMA = 0.7;
const float RL10 = 100;
float LastValue_PH = 1.22;

// Criando o objeto da classe DHTesp e chamar o sensor.
DHTesp dhtSensor;


// Função para quando é inicializado o código, passando os estados dos botoes, inicialização dos sensores
void setup() {
  Serial.begin(115200);
  dhtSensor.setup(DHT_PIN, DHTesp::DHT22);
  pinMode(BUTTON_FOSFORO, INPUT_PULLUP);
  pinMode(BUTTON_POTASSIO, INPUT_PULLUP);
  pinMode(LED_RELE, OUTPUT);

}

//Declaração de último estado para as variaveis, intuito de utilizar em condição para disparo do Log do sensor
int lastState_FOSFORO = HIGH;
int lastState_POTASSIO = HIGH;
float desvio = 0.01;

//Loop, toda lógica, estrutura e ações de interação com o diagrama e simulador do sensor atende a
//Lógica gerada dentro dessa função de Loop
void loop() {

  //Declaração e recebimento dos dados do sensor nessa nova volta
    //Intuito disso é para não gerar log a esmo, e sim ao alterar algum valor disparar o registro em tela
    // Somente para facilitar a avaliação do funcionamento do código

  //Botoes (Fosforo e potassio)  
  int value_FOSFORO = digitalRead((BUTTON_FOSFORO));
  int value_POTASSIO = digitalRead((BUTTON_POTASSIO));

  //Calculo do valor "Lux", alterado para ser o Ph conforme instrução da atividade
  //Código foi copiado de modelos base do wokwi e adaptado, para uso e condições da lógica nossa.
  float fosforo_mol_random = 0;
  float potassio_mol_random = 0;
  int analogValue = analogRead(35);
  float voltage = analogValue / 1024. * 5;
  float  resistance = 2000 * voltage / fmax(1 - voltage / 5, 0.01);
  float  value_PH = pow(RL10 * 1e3 * pow(10, GAMMA) / resistance, (1 / GAMMA));

  //Leitura do sensor DTH22 - temperatura e Umidade
  TempAndHumidity  data = dhtSensor.getTempAndHumidity();
  float temperatura = data.temperature;
  float umidade = data.humidity;

  //A partir deste trecho, a lógica utiliza foi pensando em não gerar log automático 
  //1: Se o valor das variáveis forem iguais ao último Loop, não gera alerta/log (Serial.print)
  //2: Botões - fosforo e potassio - e Ph (lux) são analisados individualmente
  //3: Para não ficar vazio os teste, implementamos o DTH22 para ser disparado em qualquer diferença dos outros sensores.

  //Fosforo
  if (lastState_FOSFORO != value_FOSFORO){ 
    if (value_FOSFORO == LOW){
      Serial.println("");
      fosforo_mol_random = random(1, 10000 + 1) / 100.0;
      Serial.print("Presença Fosforo: ");
      Serial.println(fosforo_mol_random);
    // Serial.println(value_FOSFORO);
    }
  }
    
  //Potassio
  if (lastState_POTASSIO != value_POTASSIO) {
    if (value_POTASSIO == LOW){
      Serial.println("");
      potassio_mol_random = random(1, 10000 + 1) / 100.0;
      Serial.print("Presença Potassio: ");
      Serial.println(potassio_mol_random);
     // Serial.println(value_POTASSIO);
    }
  }

  //Ph - necessário a utilização de tratamento com a função FABS da biblioteca <math.h>, pois nessa linguagem o valor de mesmos floats em até 2 casas depois da virgula seria reconhecido diferente
  //Exemplo: 1.22 <> 1.22
  if (fabs(LastValue_PH - value_PH) >= desvio) {
    Serial.println("");
    Serial.print("Ph: ");
    Serial.println(value_PH);
  }

  //Umidade e temperatura: Condições dos outros valores serem modificados para também ser disparado Umidade e Temperatura.
  if ((lastState_FOSFORO != value_FOSFORO and value_FOSFORO == LOW) || (lastState_POTASSIO != value_POTASSIO and value_POTASSIO == LOW )|| (fabs(LastValue_PH - value_PH) >= desvio)){
    if (!isnan(temperatura) && !isnan(umidade)) {
        delay(500); // Wait for a new reading from the sensor (DHT22 has ~0.5Hz sample rate)
        Serial.println("Temp (°C): " + String(temperatura, 2));
        Serial.println("Humidity (%): " + String(umidade, 1));
        Serial.println("");
      }
  }

  //Condição para desligar o relé, representado por LED Vermelho.
  //Simula o desligamento da bomba caso a umidade for maior ou igual a 30%
  //Obs: essa validação não depende de recebimento de logs em tela, se alterar no terminal do sensor a umidade, automaticamente irá desligar, simulando um cenário real.
  if(umidade >= 40){
    digitalWrite(LED_RELE, LOW);
    // DESLIGA O RELÉ (VERMELHO)
  }
  // Se for menor que 40% de umidade, irá ligar a bomba, representado pelo LED verde.
  else{
    digitalWrite(LED_RELE, HIGH);
    // LIGA O RELÉ (VERDE)
  }
  
  // Modelo de saída para copiar os dados 
  if ((lastState_FOSFORO != value_FOSFORO && value_FOSFORO == LOW) || (lastState_POTASSIO != value_POTASSIO && value_POTASSIO == LOW) || fabs(LastValue_PH - value_PH) >= desvio) {
    if (!isnan(temperatura) && !isnan(umidade)) {
      Serial.println("============================================ COPIAVEL PARA SCRIPT PYTHON ============================================");
      Serial.println("");
      Serial.print("log,");
      Serial.print(fosforo_mol_random); Serial.print(",");
      Serial.print(potassio_mol_random); Serial.print(",");
      Serial.print(value_PH, 2); Serial.print(",");
      Serial.print(temperatura, 2); Serial.print(",");
      Serial.println(umidade, 1);
      Serial.println("");
      Serial.print("=====================================================================================================================");
      Serial.println();
      } 
  }  
  

    //Define os novos valores para "Ultimo Valor do proximo loop".
    lastState_FOSFORO = value_FOSFORO;
    lastState_POTASSIO = value_POTASSIO;
    LastValue_PH = value_PH;

}
