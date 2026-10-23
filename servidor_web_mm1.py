
import random
import simpy
import statistics

# Datos de la simulacion
LAMBDA = 8
MU = 10
TIEMPO_SIM = 600

# Fijar semilla para reproducir resultados
random.seed(42)

esperas = []
tiempos_sistema = []

def peticion(env, servidor):
    llegada = env.now

    with servidor.request() as turno:
        yield turno
        inicio = env.now

        # Tiempo de servicio aleatorio
        yield env.timeout(random.expovariate(MU))

    esperas.append(inicio - llegada)
    tiempos_sistema.append(env.now - llegada)


def llegadas(env, servidor):
    while True:
        # Tiempo entre llegadas
        yield env.timeout(random.expovariate(LAMBDA))
        env.process(peticion(env, servidor))


# Crear la simulacion
env = simpy.Environment()
servidor = simpy.Resource(env, capacity=1)

env.process(llegadas(env, servidor))
env.run(until=TIEMPO_SIM)

# Resultados de la simulacion
print("Espera promedio en cola:",
      statistics.mean(esperas))

print("Tiempo promedio en el sistema:",
      statistics.mean(tiempos_sistema))

# Resultados teoricos
rho = LAMBDA / MU

print("Wq teorico:", rho / (MU - LAMBDA))
print("W teorico:", 1 / (MU - LAMBDA))
