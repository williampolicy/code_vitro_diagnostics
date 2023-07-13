import numpy as np
import matplotlib.pyplot as plt

# 定义Henderson-Hasselbalch方程
def compute_pH(pKa, HCO3, pCO2):
    return pKa + np.log10(HCO3 / (0.03 * pCO2))

# # 设定常数和变量的值
# pKa = 6.1
# HCO3 = 24  # 正常范围约为22-28 mmol/L
# pCO2_normal = 40  # 正常范围约为35-45 mmHg
# pCO2_abnormal = 30  # 假设样本暴露在空气中，pCO2值降低到30 mmHg

# # 计算正常和异常情况下的pH值
# pH_normal = compute_pH(pKa, HCO3, pCO2_normal)
# pH_abnormal = compute_pH(pKa, HCO3, pCO2_abnormal)

# # 绘制结果
# plt.figure(figsize=(8, 6))
# plt.plot([pCO2_normal, pCO2_abnormal], [pH_normal, pH_abnormal], 'o-')
# plt.xlabel('pCO2 (mmHg)')
# plt.ylabel('pH')
# plt.title('pH vs. pCO2')
# plt.legend(['Normal', 'Abnormal'])
# plt.grid(True)
# plt.show()


# 设定常数和变量的值
pKa = 6.1
HCO3 = 24  # 正常范围约为22-28 mmol/L

# 设定一系列pCO2值
pCO2_values = np.linspace(20, 60, 100)  # 正常范围约为35-45 mmHg

# 计算正常和异常情况下的pH值
pH_normal = compute_pH(pKa, HCO3, pCO2_values)

# 假设样本暴露在空气中，pCO2值整体降低10 mmHg
pH_abnormal = compute_pH(pKa, HCO3, pCO2_values - 10)

# 绘制结果
plt.figure(figsize=(8, 6))
plt.plot(pCO2_values, pH_normal, label='Normal')
plt.plot(pCO2_values, pH_abnormal, label='Abnormal (exposure to air)')
plt.xlabel('pCO2 (mmHg)')
plt.ylabel('pH')
plt.title('pH vs. pCO2')
plt.legend()
plt.grid(True)
plt.show()
