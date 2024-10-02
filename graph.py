import matplotlib.pyplot as plt
import numpy as np

# Data for NMOS transistors
nm_gm_Id = np.array([11.18, 11.15, 6.81])
nm_Id_W = np.array([0.0469, 0.0457, 0.1045])
nm_gm_gds = np.array([77.63, 95.93, 22.21])
nm_Vov = np.array([0.159, 0.160, 0.264])
nm_Id_WL = np.array([1.687, 1.643, 3.755])
nm_Gm_ro = np.array([77.63, 95.93, 22.21])

# Data for PMOS transistors
pm_gm_Id = np.array([5.00, 5.00])
pm_Id_W = np.array([0.0497, 0.0484])
pm_gm_gds = np.array([62.38, 37.95])
pm_Vov = np.array([0.357, 0.357])
pm_Id_WL = np.array([1.788, 1.739])
pm_Gm_ro = np.array([62.38, 37.95])

# Plot gm/Id vs. Id/W
plt.figure(figsize=(10, 6))
plt.scatter(nm_Id_W, nm_gm_Id, label='NMOS', color='blue')
plt.scatter(pm_Id_W, pm_gm_Id, label='PMOS', color='red')
plt.xlabel('Id/W (A/um)')
plt.ylabel('gm/Id (1/V)')
plt.title('gm/Id vs. Id/W')
plt.legend()
plt.grid(True)
plt.show()

# Plot gm/Id vs. gm/gds
plt.figure(figsize=(10, 6))
plt.scatter(nm_gm_gds, nm_gm_Id, label='NMOS', color='blue')
plt.scatter(pm_gm_gds, pm_gm_Id, label='PMOS', color='red')
plt.xlabel('gm/gds')
plt.ylabel('gm/Id (1/V)')
plt.title('gm/Id vs. gm/gds')
plt.legend()
plt.grid(True)
plt.show()

# Plot gm/Id vs. Vov
plt.figure(figsize=(10, 6))
plt.scatter(nm_Vov, nm_gm_Id, label='NMOS', color='blue')
plt.scatter(pm_Vov, pm_gm_Id, label='PMOS', color='red')
plt.xlabel('Vov (V)')
plt.ylabel('gm/Id (1/V)')
plt.title('gm/Id vs. Vov')
plt.legend()
plt.grid(True)
plt.show()

# Plot Id/(W/L) vs. gm/Id
plt.figure(figsize=(10, 6))
plt.scatter(nm_gm_Id, nm_Id_WL, label='NMOS', color='blue')
plt.scatter(pm_gm_Id, pm_Id_WL, label='PMOS', color='red')
plt.xlabel('gm/Id (1/V)')
plt.ylabel('Id/(W/L) (A/m)')
plt.title('Id/(W/L) vs. gm/Id')
plt.legend()
plt.grid(True)
plt.show()

# Plot Gm × ro vs. Vds
plt.figure(figsize=(10, 6))
plt.scatter(nm_Vov, nm_Gm_ro, label='NMOS', color='blue')
plt.scatter(pm_Vov, pm_Gm_ro, label='PMOS', color='red')
plt.xlabel('Vds (V)')
plt.ylabel('Gm × ro')
plt.title('Gm × ro vs. Vds')
plt.legend()
plt.grid(True)
plt.show()
