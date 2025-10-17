import pybullet as p
import pybullet_data
import time
import math

# Iniciar PyBullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.resetSimulation()

# Plano base
p.loadURDF("plane.urdf")

# Cargar un cubo como base del carrito
box_id = p.loadURDF("r2d2.urdf", [0, 0, 0.1])  # puedes usar cube_small.urdf si prefieres

# Gravedad
p.setGravity(0, 0, -9.8)

# Cámara
p.resetDebugVisualizerCamera(cameraDistance=2, cameraYaw=60, cameraPitch=-30, cameraTargetPosition=[0, 0, 0])

# Movimiento de traslación en eje X (simula desplazamiento)
t = 0
while True:
    x = 2 * math.sin(t)
    p.resetBasePositionAndOrientation(box_id, [x, 0, 0.1], [0, 0, 0, 1])
    p.stepSimulation()
    t += 0.01
    time.sleep(1/240)
