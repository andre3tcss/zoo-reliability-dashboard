import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, parse_dates=['timestamp'])


def generate_and_save_charts(df: pd.DataFrame) -> None:
    """Gera e salva os três gráficos a partir do DataFrame fornecido."""
    expected = {"timestamp", "cpu_usage_percent", "memory_usage_mb", "api_response_time_ms"}
    if not expected.issubset(df.columns):
        missing = expected - set(df.columns)
        raise ValueError(f"Colunas ausentes no CSV: {missing}")

    # CPU
    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["cpu_usage_percent"], marker="o", linestyle="-")
    plt.title("Uso de CPU ao Longo do Tempo")
    plt.xlabel("Timestamp")
    plt.ylabel("Uso de CPU (%)")
    plt.grid(True)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("grafico_linha_cpu.png", bbox_inches="tight")
    plt.close()

    # Memória
    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["memory_usage_mb"], marker="o", linestyle="-")
    plt.title("Uso de Memória ao Longo do Tempo")
    plt.xlabel("Timestamp")
    plt.ylabel("Uso de Memória (MB)")
    plt.grid(True)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("grafico_linha_memoria.png", bbox_inches="tight")
    plt.close()

    # API Response
    plt.figure(figsize=(10, 6))
    plt.hist(df["api_response_time_ms"], bins=20, edgecolor="black")
    plt.title("Distribuição do tempo de resposta da API")
    plt.xlabel("Tempo de resposta (ms)")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.savefig("histograma_api.png", bbox_inches="tight")
    plt.close()


def main() -> None:
    df = load_data("dados_performance.csv")
    generate_and_save_charts(df)


if __name__ == "__main__":
    main()
