#include <WiFi.h>

const char* ssid = "WiFi ESP32";
const char* wifi_password = "esp446923"; // Método prototipal, em um modelo de lançamento, o produto deveria apresentar uma interface de configuração para conectar à uma rede


TaskHandle_t Core0T;
TaskHandle_t Core1T;

WiFiServer server(3621);

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  Serial.println("Conectando ao WiFi...");
  WiFi.begin(ssid, wifi_password); // Conecta ao WiFi designado
  server.begin();

  xTaskCreatePinnedToCore(NetworkHandle, "CPU 0", 5200, NULL, 1, &Core0T, 0); //Aumente o usStackDepth para evitar Unhandled debug exception
  xTaskCreatePinnedToCore(SensorHandle, "CPU 1", 1000, NULL, 1, &Core1T, 1);
  
}

void NetworkHandle(void * pr){

  while (WiFi.status() != WL_CONNECTED){ delay(300); }
  Serial.println("Conectado!");
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());

  WiFiClient client;
  
  while (true){

    client = server.available();
    if(client){
      Serial.println("Um dispositivo requisitou conexão!\nMensagem:");
      while(client.connected()){
        while(client.available()){
          Serial.print((char)client.read());
        }
        delay(1);
      }
      Serial.println("Conexão finalizada!");
    }
    
    delay(300);
  }
}

void SensorHandle(void * pr){
 
  while(true){delay(1);}
  
}

void loop() {
  delay(1);
}
