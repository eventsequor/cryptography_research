# Topicos modernos de criptografía

### Nombre: Daniel Andres Jaimes Cardenas
1. Tipo de Artículo: Survey (Revisión Bibliográfica)
2. Titulo: The NIST Random Bit Generation Process: A Survey of the SP 800-90 Standards and Entropy Sources
3. Objetivo General
Realizar una revisión bibliográfica (tipo survey) para describir, analizar y sintetizar el marco de trabajo propuesto por NIST (serie SP 800-90) para la Generación de Bits Aleatorios (RBG), con un énfasis particular en el rol crucial, la caracterización y la validación de las fuentes de entropía, integrando perspectivas y hallazgos clave de la literatura académica relevante
4. Objetivos Específicos
Describir el Ecosistema NIST para RBG: Explicar la arquitectura general y los componentes fundamentales del marco NIST SP 800-90, detallando la función e interacción entre las fuentes de entropía (SP 800-90B), los generadores determinísticos (SP 800-90A) y las construcciones RBG (SP 800-90C).
Analizar en detalle los requisitos clave de NIST SP 800-90B para la validación de fuentes de entropía, incluyendo los diferentes métodos de estimación de entropía  y la función e implementación de las pruebas de salud.
Revisar Tipos y Desafíos de Fuentes de Entropía: Investigar y categorizar, basándose en la literatura académica seleccionada, diversos tipos de fuentes de entropía (ej. físicas basadas en hardware, no físicas basadas en software/sistema/usuario), discutiendo sus principios operativos y los desafíos reportados para cumplir con los criterios de NIST SP 800-90B.
(Opcional) Ilustrar un Concepto Clave: Desarrollar una pequeña demostración práctica o ejemplo ilustrativo para clarificar uno de los conceptos centrales discutidos en el survey.
5. Metodología
Fase 1: Revisión de Estándares NIST: Lectura comprensiva y análisis de los documentos primarios: NIST SP 800-90A, SP 800-90B, SP 800-90C, y documentos contextuales relevantes. Extracción de definiciones clave, requisitos y flujos de proceso.
Fase 2: Búsqueda y Selección de Literatura Académica: Realización de búsquedas sistemáticas en bases de datos académicas para identificar artículos relevantes. Criterios de selección: trabajos que analicen fuentes de entropía, discutan la aplicación de SP 800-90B/90A/90C, evalúen pruebas de aleatoriedad, o critiquen/comparen los estándares.
Fase 3: Síntesis y Estructuración del Survey: Organización lógica de toda la información recopilada (de estándares y papers) siguiendo los objetivos específicos. Creación de un esquema detallado para el artículo de survey final, definiendo las secciones principales (Introducción, Marco NIST RBG, Fuentes de Entropía en Profundidad, Revisión de Fuentes en la Literatura, Rol de DRBGs, Discusión, Conclusiones).
Fase 4 (Condicional): Desarrollo de Ilustración Práctica: Si se determina viable en fases posteriores, se dedicará un tiempo limitado a desarrollar un pequeño código o análisis (claramente identificado como ilustrativo y no una validación completa) para reforzar la explicación de un concepto.

### Nombre: Tomás Bedoya C.
1. Tipo de Artículo: Survey
2. Objetivo General: Estructurar una descripción comprehensiva del proceso de generación aleatoria de bits (RBG), con particular énfasis en las fuentes de entropía que utilizan los algoritmos de generación aleatoria. Por medio de la indiagación sobre las fuentes y técnicas de entropía existentes y frecuentemente utilizadas, se pretende detallar las características fundamentales de una fuente de entropía practica, junto con sus requisitos para cumplir con los estandares de intustria actuales. Posteriormente, se desea analizar las similitudes y diferencias entre diferentes técnicas de entropía para determinar los atributos de una fuente de entropía excepcional, sentando una base conceptual consisa que facilite la propocición de nuevas fuentes de entropía, cada vez más cercanas a la aleatoriedad pura.
3. Objetivos Específicos:
  Comprender los estandares internacionales a los que están sujetos hoy en día los métodos de RBG bajo el criterio de diversas organizaciones como la NSA y la NIST.
  Recopilar los métodos más prominentes de RGB, así como los más utilizados. Esto incluye detallar la diferencia entre los "verdaderos" y los pseudo-generadores de números aleatorios, y las ventajas y desventajas de ambos métodos.
  Indagar sobre las fuentes de entropía fisicas que son utilizadas comumente hoy en día, determinando sus aspectos comunes, sus ventajas y desventajas, y sus usos particulares.
  Comprender el funcionamiento de los algoritmos de RGB relevantes actualmente, y como estos complementan las fuentes de entropía que utilizan, incrementando la dificultad de predictibilidad de los números que producen.
  Documentar los desafios que la literatura académica estipula que existen actualmente en el campo de generación aleatoria de números, o de información en sí, y comparar los problemas con los métodos existentes con el propósito de       encontrar oportunidades de mejoría en los métodos existentes, o la proposición de métodos y fuentes totalmente nuevas.
  Concretar un simiento conceptual básico del cual pueda partirse facilmente para incentivar la proposición de metodos de RGB novedosos que sigan aumentando la aleatoriedad a la hora de generar bits, incrementando así la dificultad de predicción de estos números en entornos en los que esta inpredictibilidad es fundamental para la calidad de seguridad informática.
