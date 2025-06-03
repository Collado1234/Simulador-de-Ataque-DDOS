# DDoS Traffic Simulator and Anomaly Detection

## Overview

Este projeto é uma simulação simples de tráfego de rede que pode alternar entre tráfego normal e tráfego de ataque DDoS. Utiliza o algoritmo de clustering DBSCAN para detectar anomalias no padrão de tráfego, indicando possíveis ataques DDoS em tempo real.

O projeto é implementado em Python com interface gráfica Tkinter para visualização dinâmica do tráfego e das anomalias detectadas.

---

## Funcionalidades

- Simulação de tráfego normal e tráfego com ataque DDoS.
- Detecção automática de anomalias usando DBSCAN.
- Visualização gráfica do tráfego em tempo real.
- Destaca os pontos anômalos no gráfico em vermelho.
- Botões para iniciar e parar o ataque DDoS.
- Ajuste automático da escala do gráfico para acompanhar a variação do tráfego.

---

## Como usar

### Requisitos

- Python 3.8+
- Bibliotecas Python:
  - `numpy`
  - `scikit-learn`
  - `tkinter` (geralmente já incluído no Python padrão)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/ddos-traffic-simulator.git
   cd ddos-traffic-simulator
