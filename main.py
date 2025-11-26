from machine import Pin, I2C                     # importa classes para controlar pinos GPIO e o barramento I2C (MicroPython)
from max30100_simulated import Max30100Simulated # importa uma classe que simula o sensor de pulso (BPM)
import ssd1306                                   # biblioteca do display OLED SSD1306 (driver)
import time                                      # importa o módulo time para delays

# Inicializa o barramento I2C: I2C(0) com SCL conectado ao pino 22 e SDA ao pino 21
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Define largura e altura do display OLED (em pixels)
# Cria o objeto do display SSD1306 via I2C, passando larg, alt e o objeto i2c
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
# Instancia o sensor simulado (vai gerar BPM aleatórios)
sensor = Max30100Simulated()

# Define dois pinos como saída para controlar LEDs que simulam batimento
led = Pin(5, Pin.OUT)
led2 = Pin(18, Pin.OUT)

measure_count = 0

# Função que obtém o BPM do sensor simulado e converte para string
def bpm_change():
    return str(sensor.bpm_simulator()) # chama o método que retorna um inteiro e converte para string
    # retorna o valor do BPM como texto

# Função que simula um batimento com dois LEDs (pisca um, espera, pisca o outro)
def simulated_heartbeat():
    led.on()  # liga o LED 1
    led.off() # desliga imediatamente (dá um 'pulso curto')
    time.sleep_ms(300) # espera 300 milissegundos
    led2.on() # liga o LED 2
    led2.off() # desliga o LED 2

# Função que dispara um alerta visual (piscar rápido) quando o BPM é alto
def alert_high_bpm():
    for _ in range(3): # repete 3 vezes
        led.on()       # liga LED 1
        led2.on()      # liga LED 2
        time.sleep_ms(100) # espera 100 ms
        led.off()      # desliga LED 1
        led2.off()     # desliga LED 2
        time.sleep_ms(100)

# Função que escreve informações no display OLED
def show_bpm(bpm):
    oled.fill(0) # apaga/limpa o display (preenche com cor 0)
    oled.text("---------------",0,0)
    oled.text("Pulso", 15, 15) # escreve "Pulso" na posição x=15,y=15
    oled.text("cardiaco", 25, 25)  # escreve "cardiaco" logo abaixo
    oled.text(bpm + " BPM",35,45)  # mostra o valor do BPM seguido de " BPM"
    # Se o BPM (convertido para inteiro) for maior que 90, exibe alerta no OLED
    if int(bpm) > 90:
        oled.text("Alerta!!", 20, 55) # mensagem de alerta
    oled.show()
    time.sleep(1)

while True:
    start = time.ticks_ms()
    measure_count += 1
    bpm_now = bpm_change()
    if int(bpm_now) > 90:
       alert_high_bpm
    simulated_heartbeat()
    show_bpm(bpm_now)

    end = time.ticks_ms()
    response_time = end - start

    print("")
    print("==== Medição {} ====".format(measure_count))
    print("Sensor/Atuador: MAX30100 Simulado")
    print("Tempo de resposta: {} ms".format(response_time))
    print("====================")
    print("")
