import pybullet as p
import pybullet_data
import time
import math

# Conectarse a PyBullet con interfaz gráfica
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Cargar plano base
p.loadURDF("plane.urdf")

# Crear un cubo que actuará como dron
cube_start_pos = [0, 0, 1]
cube_start_orientation = p.getQuaternionFromEuler([0, 0, 0])
cube_id = p.loadURDF("cube_small.urdf", cube_start_pos, cube_start_orientation)

# Configurar gravedad
p.setGravity(0, 0, -9.8)

# Ajustar cámara
p.resetDebugVisualizerCamera(cameraDistance=2, cameraYaw=50, cameraPitch=-30, cameraTargetPosition=[0, 0, 0])

# Simulación del vuelo
t = 0
while True:
    # Aplicar fuerza vertical tipo "motor" para mantener flotando
    thrust = 9.8 + 2 * math.sin(t)  # fuerza oscilante
    p.applyExternalForce(cube_id, -1, [0, 0, thrust], [0, 0, 0], p.WORLD_FRAME)

    # Aplicar ligera rotación para hacerlo dinámico
    roll = 0.1 * math.sin(2 * t)
    pitch = 0.1 * math.cos(2 * t)
    quat = p.getQuaternionFromEuler([roll, pitch, 0])
    p.resetBaseVelocity(cube_id, [0, 0, 0], [0, 0, 0])
    p.resetBasePositionAndOrientation(cube_id, [0, 0, 1 + 0.2 * math.sin(t)], quat)

    p.stepSimulation()
    t += 0.02
    time.sleep(1/240)
