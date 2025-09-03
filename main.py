import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados_performance.csv', parse_dates=['timestamp'])

plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['cpu_usage_percent'], marker='o', linestyle='-')
plt.title('Uso de CPU ao Longo do Tempo')
plt.xlabel('Timestamp')
plt.ylabel('Uso de CPU (%)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_linha_cpu.png')

plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['memory_usage_mb'], marker='o', linestyle='-')
plt.title('Uso de Memória ao Longo do Tempo')
plt.xlabel('Timestamp')
plt.ylabel('Uso de Memória (MB)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_linha_memoria.png')

plt.figure(figsize=(10, 6))
plt.hist(df['api_response_time_ms'], bins=20, color='g', edgecolor='black')
plt.title('Distribuição do tempo de resposta da API')
plt.xlabel('Tempo de resposta (ms)')
plt.ylabel('Frequência')
plt.savefig('histograma_api.png')