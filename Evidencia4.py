class Pulidora:
    def __init__(self):
        self.estado = 'apagada'
        self.velocidad = 0
        self.modo = 'básico'
        self.nivel_lente = 0

    def encender(self):
        if self.estado == 'apagada':
            self.estado = 'encendida'
        else:
            raise Exception("La pulidora ya está encendida.")

    def apagar(self):
        if self.estado == 'encendida':
            self.estado = 'apagada'
        else:
            raise Exception("La pulidora ya está apagada.")

    def ajustar_velocidad(self, velocidad):
        if self.estado == 'encendida':
            self.velocidad = velocidad
        else:
            raise Exception("La pulidora debe estar encendida para ajustar la velocidad.")

    def seleccionar_modo(self, modo):
        if self.estado == 'encendida':
            if modo in ['básico', 'avanzado', 'ultra']:
                self.modo = modo
            else:
                raise ValueError("Modo no válido.")
        else:
            raise Exception("La pulidora debe estar encendida para seleccionar el modo.")

    def pulir_lente(self):
        if self.estado == 'encendida':
            if self.nivel_lente > 0:
                self.nivel_lente -= self.velocidad * 0.1  # Simplificación de pulido
                if self.nivel_lente < 0:
                    self.nivel_lente = 0
            else:
                raise ValueError("El lente ya está limpio.")
        else:
            raise Exception("La pulidora debe estar encendida para pulir el lente.")

    def reportar_estado(self):
        return {
            'estado': self.estado,
            'velocidad': self.velocidad,
            'modo': self.modo,
            'nivel_lente': self.nivel_lente
        }

    def __str__(self):
        return (f"Pulidora (Estado: {self.estado}, Velocidad: {self.velocidad}, "
                f"Modo: {self.modo}, Nivel de Lente: {self.nivel_lente})")
    