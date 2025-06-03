import tkinter as tk
import random
from anomaly import AnomalyDetector

# Configurações de tráfego
normal_traffic_rate = 50         # Taxa média de tráfego normal
ddos_traffic_rate = 500          # Taxa média durante um ataque DDoS
is_ddos = False                  # Estado do ataque (ativo ou não)

# Dados de tráfego e histórico
traffic_data = [normal_traffic_rate]           # Dados atuais (janela deslizante)
traffic_data_history = [normal_traffic_rate]   # Histórico completo dos dados
anomaly_detector_history = [False]             # Histórico de anomalias detectadas (True/False)

# Instância do detector de anomalias
anomaly_detector = AnomalyDetector()

# Função para iniciar o ataque DDoS
def start_ddos():
    """
    Ativa o estado de ataque DDoS.
    """
    global is_ddos
    is_ddos = True

# Função para parar o ataque DDoS
def stop_ddos():
    """
    Desativa o estado de ataque DDoS.
    """
    global is_ddos
    is_ddos = False

# Atualização dos dados de tráfego
def update_traffic():
    """
    Atualiza os dados de tráfego, detecta anomalias e atualiza o gráfico.
    """
    global traffic_data, traffic_data_history, anomaly_detector_history

    # Gerando dados dependendo do estado do ataque
    if is_ddos:
        value = random.randint(ddos_traffic_rate - 50, ddos_traffic_rate + 50)
    else:
        value = random.randint(normal_traffic_rate - 10, normal_traffic_rate + 10)

    # Adicionando valores no histórico
    traffic_data.append(value)
    traffic_data_history.append(value)
    anomaly_detector_history.append(False)

    # Mantendo os dados em uma janela de 100 pontos
    if len(traffic_data) > 100:
        traffic_data = traffic_data[-100:]
        traffic_data_history = traffic_data_history[-100:]
        anomaly_detector_history = anomaly_detector_history[-100:]

    # Detectando anomalias
    anomalies_detected = anomaly_detector.detect(traffic_data)

    for i, is_anomaly in zip(range(len(traffic_data)), anomalies_detected):
        if is_anomaly:
            anomaly_detector_history[i] = True
            # Corrige o dado no gráfico para não deformar a linha
            traffic_data[i] = normal_traffic_rate

    # Redesenha o gráfico com os dados atualizados
    draw_graph()

    # Atualiza novamente após 1 segundo
    root.after(1000, update_traffic)

# Desenha o gráfico do tráfego
def draw_graph():
    """
    Desenha o gráfico com os dados de tráfego e marca as anomalias.
    """
    canvas.delete("all")  # Limpa o canvas anterior

    canvas_height = 300
    canvas_width = 500

    if not traffic_data_history:
        return  # Sem dados, não desenha

    # Determina máximo e mínimo do histórico para escalonamento dinâmico
    max_value = max(traffic_data_history)
    min_value = min(traffic_data_history)

    # Proteção contra divisão por zero
    if max_value == min_value:
        max_value += 1

    # Margem de 10% no topo e na base para melhor visualização
    max_value *= 1.1
    min_value = min_value * 0.9 if min_value > 0 else 0

    # Calcula o fator de escala para ajustar os valores ao tamanho do canvas
    scale = canvas_height / (max_value - min_value)

    # Desenha as linhas do gráfico
    for i in range(1, len(traffic_data_history)):
        x1 = (i - 1) * (canvas_width / 100)
        y1 = canvas_height - ((traffic_data_history[i - 1] - min_value) * scale)
        x2 = i * (canvas_width / 100)
        y2 = canvas_height - ((traffic_data_history[i] - min_value) * scale)

        # Cor vermelha se é anomalia, azul se normal
        if anomaly_detector_history[i]:
            canvas.create_line(x1, y1, x2, y2, fill="red", width=2)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

# Interface Gráfica (Tkinter)
root = tk.Tk()
root.title("DDoS Traffic Simulator")

# Canvas para desenhar o gráfico
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

# Botão para iniciar o ataque
start_button = tk.Button(root, text="Start DDoS Attack", command=start_ddos)
start_button.pack(side=tk.LEFT, padx=20, pady=20)

# Botão para parar o ataque
stop_button = tk.Button(root, text="Stop DDoS Attack", command=stop_ddos)
stop_button.pack(side=tk.LEFT, padx=20, pady=20)

# Inicia o loop de atualização do tráfego
root.after(50, update_traffic)

# Inicia a interface Tkinter
root.mainloop()
