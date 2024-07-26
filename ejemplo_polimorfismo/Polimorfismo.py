from abc import ABC, abstractmethod

class Estudiante(ABC):
    def __init__(self, nombres, apellidos, identificacion, edad):
        self._nombres_estudiante = nombres
        self._apellidos_estudiante = apellidos
        self._identificacion_estudiante = identificacion
        self._edad_estudiante = edad
        self._matricula = 0.0

    def establecer_nombres_estudiante(self, nombres):
        self._nombres_estudiante = nombres

    def establecer_apellido_estudiante(self, apellidos):
        self._apellidos_estudiante = apellidos

    def establecer_identificacion_estudiante(self, identificacion):
        self._identificacion_estudiante = identificacion

    def establecer_edad_estudiante(self, edad):
        self._edad_estudiante = edad

    @abstractmethod
    def calcular_matricula(self):
        pass

    def obtener_nombres_estudiante(self):
        return self._nombres_estudiante

    def obtener_apellido_estudiante(self):
        return self._apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self._identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self._edad_estudiante

    def obtener_matricula(self):
        return self._matricula


class EstudianteDistancia(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad):
        super().__init__(nombres, apellidos, identificacion, edad)
        self._numero_asignaturas = 0
        self._costo_asignatura = 0.0

    def establecer_numero_asignaturas(self, numero):
        self._numero_asignaturas = numero

    def establecer_costo_asignatura(self, costo):
        self._costo_asignatura = costo

    def calcular_matricula(self):
        self._matricula = self._numero_asignaturas * self._costo_asignatura

    def obtener_numero_asignaturas(self):
        return self._numero_asignaturas

    def obtener_costo_asignatura(self):
        return self._costo_asignatura


class EstudiantePresencial(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad):
        super().__init__(nombres, apellidos, identificacion, edad)
        self._numero_creditos = 0
        self._costo_credito = 0.0

    def establecer_numero_creditos(self, numero):
        self._numero_creditos = numero

    def establecer_costo_credito(self, costo):
        self._costo_credito = costo

    def calcular_matricula(self):
        self._matricula = self._numero_creditos * self._costo_credito

    def obtener_numero_creditos(self):
        return self._numero_creditos

    def obtener_costo_credito(self):
        return self._costo_credito


if __name__ == "__main__":
    # Crear un estudiante de ejemplo para mostrar cómo funciona
    est_distancia = EstudianteDistancia("René", "Elizalde", "110011", 36)
    est_distancia.establecer_numero_asignaturas(5)
    est_distancia.establecer_costo_asignatura(100.0)
    est_distancia.calcular_matricula()

    print(f"Estudiante: {est_distancia.obtener_nombres_estudiante()} {est_distancia.obtener_apellido_estudiante()}")
    print(f"Matrícula: {est_distancia.obtener_matricula()}")