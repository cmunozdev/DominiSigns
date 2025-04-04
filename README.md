# DominiSigns: Traductor de Avatar para Lenguaje de Señas Dominicano

![DominiSigns Logo](https://via.placeholder.com/200x200.png?text=DominiSigns)

## 📝 Descripción del Proyecto

DominiSigns es una innovadora aplicación de accesibilidad que utiliza inteligencia artificial para traducir texto y voz al lenguaje de señas dominicano (LSRD) a través de un avatar 3D animado. Nuestro objetivo es derribar barreras de comunicación y promover la inclusión de la comunidad sorda en República Dominicana.

## 🌟 Características Principales

- **Traducción de Texto a Señas**: Convierte entradas de texto a animaciones de lenguaje de señas dominicano
- **Traducción de Voz a Señas**: Reconoce audio y lo convierte a señas
- **Avatar 3D Personalizado**: Avatar realista que realiza señas con precisión y fluidez
- **Diccionario Integrado**: Base de datos completa de LSRD
- **Interfaz Accesible**: Diseñada siguiendo principios de accesibilidad universal

## 🚀 Estado del Proyecto

Actualmente en fase de desarrollo activo. El proyecto se encuentra en las siguientes etapas:

- [x] Recopilación de diccionario y videos de referencia de LSRD
- [ ] Desarrollo del procesador de texto/voz
- [ ] Creación del avatar 3D base
- [ ] Implementación de las animaciones de señas
- [ ] Desarrollo de la interfaz de usuario
- [ ] Pruebas con la comunidad sorda dominicana

## 🛠️ Tecnologías Utilizadas

- **Frontend**: React, Three.js
- **Backend**: Node.js, Express
- **Procesamiento de Lenguaje**: TensorFlow/PyTorch para NLP
- **Animación 3D**: Blender, Mixamo
- **IA Generativa**: Pollinations.ai API
- **Base de Datos**: MongoDB

## 📋 Requisitos

- Node.js v14 o superior
- Acceso a API de Pollinations.ai
- Dependencias listadas en package.json

## 🔧 Instalación y Configuración

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/dominisigns.git
cd dominisigns

# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env
# Edita el archivo .env con tus credenciales de API

# Iniciar el servidor de desarrollo
npm run dev
```

## 📊 Arquitectura del Sistema

```
                      ┌───────────────┐
                      │  Entrada de   │
                      │ Texto/Audio   │
                      └───────┬───────┘
                              │
                      ┌───────▼───────┐
                      │  Procesador   │
                      │     NLP       │
                      └───────┬───────┘
                              │
        ┌───────────┬─────────▼────────┬───────────┐
        │           │                  │           │
┌───────▼───┐ ┌─────▼─────┐    ┌───────▼───┐ ┌─────▼─────┐
│ Análisis  │ │ Traducción│    │ Generación │ │ Secuencia │
│ Sintáctico│ │   LSRD    │    │ Animaciones│ │  de Señas │
└───────┬───┘ └─────┬─────┘    └───────┬───┘ └─────┬─────┘
        │           │                  │           │
        └───────────┴─────────┬────────┴───────────┘
                              │
                      ┌───────▼───────┐
                      │    Avatar     │
                      │     3D        │
                      └───────────────┘
```

## 👥 Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir:

1. Haz un fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-funcion`)
3. Realiza tus cambios y haz commit (`git commit -am 'Añade nueva función'`)
4. Sube los cambios a tu rama (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

Consulta nuestro [documento de contribución](CONTRIBUTING.md) para más detalles.

## 🔍 Casos de Uso

- **Educación**: Apoyo en aulas inclusivas
- **Servicios Públicos**: Mejora de accesibilidad en hospitales, bancos, etc.
- **Comunicación Personal**: Facilita interacciones cotidianas
- **Eventos y Conferencias**: Interpretación automática para presentaciones

## 🌍 Impacto Social

Este proyecto está dirigido a las aproximadamente 100,000 personas sordas en República Dominicana que utilizan LSRD como su principal medio de comunicación. Al facilitar una herramienta tecnológica que respeta las particularidades culturales y lingüísticas del país, buscamos:

1. Reducir barreras de comunicación
2. Promover la inclusión social
3. Preservar y difundir el lenguaje de señas dominicano
4. Apoyar la independencia y autonomía de la comunidad sorda

## 📞 Contacto

Para preguntas, sugerencias o colaboraciones, contacta con:
- Email: [tu-email@ejemplo.com](mailto:tu-email@ejemplo.com)
- Twitter: [@tu_usuario](https://twitter.com/tu_usuario)
- Web: [www.dominisigns.org](https://www.dominisigns.org)

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- [Asociación Nacional de Sordos de República Dominicana](https://ansordo.org)
- Comunidad de desarrolladores de accesibilidad
- Equipo de Pollinations.ai por su apoyo técnico
- Todos los intérpretes y colaboradores que han contribuido con material de referencia
