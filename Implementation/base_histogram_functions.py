import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from collections import Counter

def graficar_histograma_bytes(values, filename="random_bits_histogram.png"):
    # Paso 1: Calcular frecuencias
    byte_counts = Counter(values)
    most_freq_byte = max(byte_counts, key=byte_counts.get)
    least_freq_byte = min(byte_counts, key=byte_counts.get)
    most_freq_density = byte_counts[most_freq_byte] / len(values)
    least_freq_density = byte_counts[least_freq_byte] / len(values)

    # Paso 2: Crear histograma
    plt.figure(figsize=(10, 6))
    count, bins, _ = plt.hist(values, bins=256, density=True, alpha=0.6, color='skyblue', label='Frequency')

    # Paso 3: Superponer distribución normal
    mu, sigma = np.mean(values), np.std(values)
    x = np.linspace(0, 255, 256)
    plt.plot(x, norm.pdf(x, mu, sigma), 'r-', linewidth=2, label=f'Normal Distribution\nμ={mu:.2f}, σ={sigma:.2f}')

    # Paso 4: Resaltar el más y menos frecuente
    plt.axvline(most_freq_byte, color='green', linestyle='--', linewidth=1.5, label=f'Most Frequent: {most_freq_byte}')
    plt.text(most_freq_byte + 1, most_freq_density,
             f'{most_freq_byte}\nCount: {byte_counts[most_freq_byte]}',
             color='green', fontsize=9, ha='left', va='bottom')

    plt.axvline(least_freq_byte, color='purple', linestyle='--', linewidth=1.5, label=f'Least Frequent: {least_freq_byte}')
    plt.text(least_freq_byte + 1, least_freq_density,
             f'{least_freq_byte}\nCount: {byte_counts[least_freq_byte]}',
             color='purple', fontsize=9, ha='left', va='bottom')

    # Paso 5: Configuración final
    total_bytes = len(values)
    plt.title(f'Histogram of {total_bytes:,} Random Bytes\nwith Normal Distribution Overlay')
    plt.xlabel('Byte Value (0–255)')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Paso 6: Guardar y mostrar
    plt.savefig(filename, dpi=300)
    plt.show()


def bits_a_bytes(bit_string):
    # Asegurar que la longitud sea múltiplo de 8
    if len(bit_string) % 8 != 0:
        raise ValueError("La cadena de bits debe tener una longitud múltiplo de 8.")
    
    # Convertir cada grupo de 8 bits a entero
    return [int(bit_string[i:i+8], 2) for i in range(0, len(bit_string), 8)]


## Ejemplo de uso
bit_string = "011011000110010100101111"
bytes_list = bits_a_bytes(bit_string)
print(bytes_list)  # Ejemplo de salida: [108, 101, 47]

graficar_histograma_bytes(bytes_list, "histograma.png")