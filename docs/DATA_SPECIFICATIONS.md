# DominiSigns - Especificaciones de Datos

## Guía para CONADIS/ANSORDO

Este documento describe cómo deben prepararse los videos y el diccionario para ser procesados por DominiSigns.

---

## 📹 Especificaciones de Videos

### Formato Requerido

| Aspecto | Especificación |
|---------|----------------|
| **Formato** | MP4 (H.264) |
| **Resolución** | Mínimo 720p (1280x720), ideal 1080p |
| **FPS** | 30 fps (mínimo 24 fps) |
| **Duración** | 1-5 segundos por seña |
| **Fondo** | Uniforme (verde, azul o gris claro) |
| **Iluminación** | Uniforme, sin sombras fuertes |
| **Encuadre** | Persona visible de cintura hacia arriba |

### Requisitos del Intérprete

- Manos completamente visibles en todo momento
- Ropa de color sólido (contraste con manos)
- Sin accesorios que oculten manos (anillos grandes, mangas largas)
- Posición inicial y final: manos en posición neutra

### Estructura de Carpetas

```
videos/
├── abecedario/
│   ├── a.mp4
│   ├── b.mp4
│   └── ...
├── numeros/
│   ├── 1.mp4
│   ├── 2.mp4
│   └── ...
├── saludos/
│   ├── hola.mp4
│   ├── adios.mp4
│   └── ...
├── familia/
│   ├── mama.mp4
│   ├── papa.mp4
│   └── ...
├── colores/
├── animales/
├── alimentos/
├── verbos/
├── adjetivos/
└── ... (una carpeta por categoría)
```

### Nomenclatura de Archivos

| Regla | Ejemplo |
|-------|---------|
| Todo en minúsculas | `hola.mp4` ✓ `Hola.mp4` ✗ |
| Sin acentos | `mama.mp4` ✓ `mamá.mp4` ✗ |
| Sin espacios (usar guiones) | `buenos-dias.mp4` ✓ |
| Sin caracteres especiales | `ano.mp4` ✓ `año.mp4` ✗ |
| Variaciones con sufijo | `hola.mp4`, `hola_grupo.mp4` |

### Mapeo de Caracteres

| Original | Archivo |
|----------|---------|
| á, é, í, ó, ú | a, e, i, o, u |
| ñ | n o nn |
| ü | u |
| espacios | - (guión) |

---

## 📖 Formato del Diccionario

### Archivo Principal: `dictionary.json`

```json
{
  "version": "1.0",
  "source": "CONADIS/ANSORDO",
  "date": "2024-01-15",
  "total_signs": 723,
  "categories": [
    "abecedario",
    "numeros", 
    "saludos",
    "familia",
    "colores",
    "animales"
  ],
  "signs": [
    {
      "id": "hola",
      "word": "Hola",
      "category": "saludos",
      "definition": "Interjección. Se usa como saludo.",
      "video_file": "saludos/hola.mp4",
      "variations": [
        {
          "id": "hola_grupo",
          "description": "Para saludar a un grupo",
          "video_file": "saludos/hola_grupo.mp4"
        }
      ],
      "related": ["buenos-dias", "buenas-tardes", "adios"]
    }
  ]
}
```

### Campos Requeridos por Seña

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `id` | string | ✓ | Identificador único (igual al nombre del video) |
| `word` | string | ✓ | Palabra en español (con acentos) |
| `category` | string | ✓ | Categoría del diccionario |
| `definition` | string | ✓ | Definición breve |
| `video_file` | string | ✓ | Ruta relativa al video |
| `variations` | array | ✗ | Variantes de la seña |
| `related` | array | ✗ | IDs de señas relacionadas |

### Alternativa: Formato CSV

Si es más fácil, pueden entregar un CSV:

```csv
id,word,category,definition,video_file
hola,Hola,saludos,"Interjección de saludo",saludos/hola.mp4
adios,Adiós,saludos,"Despedida",saludos/adios.mp4
mama,Mamá,familia,"Madre",familia/mama.mp4
```

---

## 📁 Estructura Final de Entrega

```
LSRD_DominiSigns/
├── dictionary.json (o dictionary.csv)
├── categories.json (opcional)
└── videos/
    ├── abecedario/
    ├── numeros/
    ├── saludos/
    └── ...
```

---

## ✅ Checklist de Entrega

- [ ] Videos en formato MP4 (H.264)
- [ ] Resolución mínima 720p
- [ ] Nombres de archivo sin acentos ni espacios
- [ ] Una carpeta por categoría
- [ ] Archivo dictionary.json o dictionary.csv
- [ ] Cada entrada tiene: id, word, category, definition, video_file

---

## 📞 Contacto

Para dudas sobre el formato, contactar a: [tu email/contacto]
