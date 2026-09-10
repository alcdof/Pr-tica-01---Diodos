import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Valores vindos da tabela
tensao_1N400x = [-3.213, -1.1268, -0.0310, 0.1924, 0.3726, 0.4589, 0.5292, 0.5943, 0.6233, 0.6424, 0.6525, 0.6565, 0.7134, 0.7362, 0.7614, 0.7814, 0.7895]
corrente_1N400x = [-0.064, -0.015, -0.022, -0.029, -0.019, 0.043, 0.243, 1.019, 1.835, 2.680, 3.516, 3.866, 13.415, 22.907, 43.269, 72.840, 93.390]
tensao_1N4148 = [-3.0642, -1.1129, -0.0067, 0.1567, 0.3734, 0.4280, 0.5587, 0.5954, 0.6366, 0.6531, 0.6785, 0.6869, 0.7636, 0.8009, 0.8490, 0.8939, 0.9128]
corrente_1N4148 = [-0.003, -0.006, -0.012, -0.072, -0.002, 0.043, 0.322, 0.691, 1.667, 2.116, 2.836, 3.904, 13.291, 22.636, 42.585, 72.080, 91.450]

# Configuração do gráfico
plt.xlabel(r'$V_D$ (V)')
plt.ylabel(r'$I_d$ (mA)')
plt.title('Corrente em um diodo em função da tensão aplicada')
plt.grid(True)

# Plotando as duas funções
plt.plot(tensao_1N4148, corrente_1N4148, label='Diodo 1N4148', color='red')
plt.plot(tensao_1N400x, corrente_1N400x, label='Diodo 1N400x', color='blue')

# TODO: encontrar um jeito de usar essas barrinhas
# x_ponto = 0.6233
# y_ponto = 2.680
# plt.axvline(x=x_ponto, color='gray', linestyle='--', linewidth=1)
# plt.axhline(y=y_ponto, color='gray', linestyle='--', linewidth=1)

# Legenda
plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)

# ajusta o layout pra ficar melhor e gera o gráfico
plt.tight_layout()
plt.show()