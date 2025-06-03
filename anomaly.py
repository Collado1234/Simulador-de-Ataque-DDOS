import numpy as np
from sklearn.cluster import DBSCAN

class AnomalyDetector:
    """
    Classe para detecção de anomalias em dados de tráfego utilizando o algoritmo DBSCAN.

    DBSCAN é um algoritmo de agrupamento baseado em densidade que permite identificar
    pontos que não pertencem a nenhum cluster, ou seja, pontos considerados ruídos (anomalias).
    """

    def __init__(self, eps=20, min_samples=5, min_train_points=10):
        """
        Inicializa o detector de anomalias com os parâmetros do DBSCAN.

        :param eps: Distância máxima entre dois pontos para que sejam considerados vizinhos.
        :param min_samples: Número mínimo de pontos na vizinhança para formar um núcleo (core point).
        :param min_train_points: Quantidade mínima de pontos necessários para começar a detecção.
        """
        self.eps = eps  # Raio da vizinhança
        self.min_samples = min_samples  # Número mínimo de pontos na vizinhança
        self.min_train_points = min_train_points  # Quantidade mínima de pontos para rodar o DBSCAN

        # Inicializa o modelo DBSCAN com os parâmetros definidos
        self.dbscan = DBSCAN(eps=self.eps, min_samples=self.min_samples)

    def detect(self, traffic_data):
        """
        Detecta anomalias nos dados de tráfego.

        :param traffic_data: Lista de valores numéricos representando taxas de tráfego.
        :return: Lista de booleanos, onde True indica que o ponto é uma anomalia, e False que não é.
        """
        # Verifica se há dados suficientes para aplicar o DBSCAN
        if len(traffic_data) >= self.min_train_points:
            # Converte os dados em um array NumPy e ajusta para o formato esperado pelo DBSCAN
            traffic_data_np = np.array(traffic_data).reshape(-1, 1)

            # Executa o algoritmo DBSCAN e obtém os rótulos dos clusters
            labels = self.dbscan.fit_predict(traffic_data_np)

            # O DBSCAN rotula anomalias como -1. Converte isso em True (anômalo) ou False (normal)
            return [True if label == -1 else False for label in labels]
        else:
            # Se não houver dados suficientes, assume que não há anomalias
            return [False] * len(traffic_data)
