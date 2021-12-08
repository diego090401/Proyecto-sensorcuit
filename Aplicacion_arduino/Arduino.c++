#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
uint8_t timeout, intentos;
bool errorconexion=false;
char ssid[] = "FPechiri_5G";   // SSID de la red o router donde se conecta el módulo
char pass[] = "Felipe150309";   // Password de la red o router
byte mac[6];
WiFiServer server(80);

//IPAddress DNS1(8, 8, 8, 8); //Opcional
//IPAddress DNS2(8, 8, 4, 4); //Opcional
WiFiClient client;  //Crea cliente WIfi
MySQL_Connection conn((Client *)&client); //Crea un objeto de conexión entre el cliente y MySQL
// Prepara la trama para la consulta SQL
char BASE_SQL[] = "INSERT INTO basearduino.tabladatos (identifica, valor) VALUES (%s,%lu)";
char consulta[128];

IPAddress server_addr(192, 168 , 1, 84);          // IP del servidor MySQL
char user[] = "Diego_0904";           // Usuario con permisos para MySQL
char password[] = "HepsuMI0QeS223Cphghh";       // Contraseña del usuario para MySQL

void setup() {
  Serial.begin(9600);
  Serial.println("Iniciando conexión");
  Serial.print("Configurando IP estática a : ");
//  Serial.print(F("Setting static ip to : "));
  Serial.println(ip);
  Serial.println("");
  Serial.print("Conectando a la red Wifi con SSID : ");
  Serial.println(ssid);
  WiFi.begin(ssid, pass);           //Inicia la conexión con la red o router
 timeout=0;
  while ((WiFi.status() != WL_CONNECTED) && (timeout++ < 150)) { //Espera a conectarse a la red hasta unos 30s
    delay(200);
    Serial.print(".");
  }
  Serial.println("");
  if (timeout>=151){
    Serial.println("Error al conectar a la red Wifi");
    errorconexion=true;
  } else {
    Serial.println("Módulo conectado a WiFi");
    muestra_mac();          //Muestra la MAC asignada
    Serial.print("IP asignada: ");
    Serial.print(WiFi.localIP());   //Muestra la IP asignada real
    Serial.println("");
    Serial.println("Conectando a base de datos");
      
}
