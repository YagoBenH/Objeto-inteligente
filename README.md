# Objeto Inteligente – Medidor de Batimentos Cardíacos (Simulado)

Este projeto implementa um sistema embarcado com **ESP32**, **Display OLED SSD1306**, LEDs e um **sensor de batimentos cardíacos simulado (MAX30100)**.  
O objetivo é exibir o BPM no display, simular o batimento através de LEDs e registrar informações de medição no terminal.

---

## Componentes Utilizados

- ESP32
- Display OLED SSD1306 (I2C)
- 2 LEDs para simulação do batimento
- Biblioteca simulada `Max30100Simulated`
- MicroPython

---

## Funcionalidades

 Leitura simulada do BPM  
 Exibição no display OLED  
 LEDs piscando simulando batimento cardíaco  
 Alerta visual quando BPM > 90  
 Exibição no terminal de:
- Número da medição  
- Sensor/Atuador  
- Tempo de resposta da operação  

---

## Exemplo de saída no terminal

==== Medição 1 ====
Sensor/Atuador: MAX30100 Simulado
Tempo de resposta: 432 ms
==== Medição 2 ====
Sensor/Atuador: MAX30100 Simulado
Tempo de resposta: 447 ms

Lógica do Projeto

O código realiza este ciclo:

1. Lê o BPM do sensor simulado  
2. Aciona LEDs representando um batimento  
3. Atualiza o display OLED  
4. Em caso de BPM acima de 90, mostra alerta visual  
5. Mede o tempo total de execução e imprime no terminal  


##  Código Principal (`main.py`)
