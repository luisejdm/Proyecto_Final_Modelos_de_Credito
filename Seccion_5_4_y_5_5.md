## 5.4 Supuestos del análisis financiero y proyecciones

El modelo financiero de FinPet fue construido sobre un horizonte de proyección mensual de 48 meses, divididos en cuatro ejercicios anuales consecutivos. Esta longitud responde a la naturaleza del negocio: dado que el plazo promedio del crédito al consumo otorgado es de nueve meses y que la curva de adquisición de suscriptores tiene una fase de penetración inicial seguida de una etapa de madurez, un horizonte inferior a tres años no permitiría capturar el punto en que el resultado acumulado del proyecto se torna positivo, indicador central para evaluar la viabilidad financiera del proyecto. Las proyecciones se construyeron bajo tres escenarios diferenciados (pesimista, esperado y optimista), cuyos parámetros fueron calibrados de manera independiente con base en evidencia empírica del mercado mexicano de crédito al consumo y en la encuesta primaria aplicada a 361 propietarios de mascotas descrita en la sección 3.2.

### 5.4.1 Supuestos del producto de suscripción

El precio anual de la membresía se fijó en $799 MXN, cifra que es soportada empíricamente por la encuesta, donde el 46% de los encuestados manifestó interés en una membresía con disposición de pago promedio de $700 MXN y mediana de $599 MXN. El cobro se modeló de forma mensualizada en doce parcialidades de $66.58 MXN, con un porcentaje del 80% de clientes mensualizados y 20% en pago de contado, replicando la estructura comercial definida en la sección 4.2.1. El gasto mensual promedio del suscriptor en comercios afiliados se estimó en $1,264.54 MXN, promedio ponderado calculado a partir de la distribución de gasto reportada en la encuesta. Sobre este gasto se aplica un cashback uniforme del 3% para el cliente, financiado íntegramente por la comisión cobrada al comercio (Merchant Discount Rate), por lo que su impacto sobre el flujo neto de FinPet depende únicamente del diferencial entre la comisión cobrada y el cashback otorgado.

### 5.4.2 Supuestos del producto de crédito

Los parámetros del producto de crédito se mantienen constantes en términos estructurales a lo largo de los tres escenarios y reflejan las condiciones operativas definidas en la sección 4.2.4. El monto promedio del crédito otorgado se estableció en $10,000 MXN, supuesto que considera una distribución bimodal de las disposiciones, con aproximadamente la mitad de los créditos concentrados cerca de $5,000 MXN y la otra mitad cerca de $15,000 MXN, conforme a la opinión técnica del experto colaborador del proyecto. El plazo promedio se fijó en nueve meses, valor intermedio del rango contractual de 6 a 12 meses, y el enganche promedio se mantiene en $1,500 MXN, equivalente al 15% del crédito promedio. La comisión por disposición es de $525 MXN durante el primer año y $550 MXN a partir del segundo año, conforme a la Tabla 2 del modelo de negocio. El monto financiado neto por crédito es de $9,025 MXN durante el primer año, resultado de restar el enganche al monto bruto y sumar la comisión por apertura.

### 5.4.3 Supuestos de riesgo crediticio

La probabilidad de default (PD) agregada del portafolio se diferencia por escenario para reflejar la incertidumbre asociada a la calibración inicial del scorecard descrita en la sección 4.3.4. En el escenario esperado se utiliza una PD del 12% en el primer año y 10% a partir del segundo año, valores consistentes con la tasa de mora a 90 días reportada por la CNBV para créditos al consumo de SOFOMes no garantizadas, que históricamente se ubica entre el 8% y el 14%. La pérdida dado incumplimiento (LGD) se asume en 65% en el escenario esperado, valor superior al promedio nacional del 40-50% para créditos garantizados, justificado por la ausencia de colateral en el producto de FinPet. Los parámetros se endurecen en el escenario pesimista (PD del 13% y LGD del 70%) y se relajan en el optimista (PD del 12% y LGD del 60% en años posteriores), reflejando supuestos coherentes con la evolución esperada del motor crediticio al transitar del scorecard inicial al modelo XGBoost a partir del mes 13.

### 5.4.4 Supuestos de fondeo y costos

El costo de fondeo anual de FinPet se calibró en 17% para el escenario pesimista, 16% para el esperado y 15% para el optimista. Estos valores reflejan una prima sobre la TIIE (aproximadamente 6.7% anual para grandes jugadores) y se ubican por encima del costo promedio de fondeo de las SOFOMes en México (cercano al 10%), prima que se justifica por el riesgo de un originador en etapa de lanzamiento y resulta atractiva para inversionistas institucionales o fondos de deuda privada. Los costos fijos mensuales son comunes a los tres escenarios e incorporan nómina, soporte técnico, ciberseguridad, servicios contable y legal, seguros y publicidad: $121,189.53 MXN para el primer año y $115,714.53 MXN a partir del segundo año, monto este último que refleja la reducción del esfuerzo publicitario de introducción de mercado tras la fase piloto. El costo variable de adquisición por cliente (consulta a buró más validación de identidad) es de $105 MXN durante el primer año y $55 MXN a partir del segundo, reducción explicada por la mejora en la eficiencia de los procesos de KYC y el aumento del volumen de consultas.

### 5.4.5 Supuestos de inversión inicial

La inversión inicial requerida para la apertura constituye uno de los parámetros más sensibles del modelo y varía por escenario en función del capital aportado para la originación de créditos. En el escenario pesimista, la inversión inicial total se ubica en $3,440,160 MXN, de los cuales $3,000,000 MXN corresponden al capital disponible para originación crediticia. El escenario esperado contempla una inversión inicial de $4,128,192 MXN con $3,600,000 MXN destinados al capital de préstamos. El escenario optimista incrementa la inversión a $4,816,224 MXN con $4,200,000 MXN para préstamos. La diferencia entre la inversión total y el capital de préstamos en cada escenario corresponde a los rubros de constitución legal de la SOFOM E.N.R., desarrollo tecnológico, adquisición de vehículos para reclutamiento de afiliados, equipos de cómputo y campaña de introducción al mercado, descritos en la sección 5.3.

### 5.4.6 Supuestos de comportamiento de la cartera

El churn rate mensual de suscriptores se asume en 2% para los escenarios esperado y optimista, y en 3% para el pesimista. La carga fiscal estimada se modela como un porcentaje aplicado sobre los ingresos brutos, con valores de 22% en el escenario pesimista, 24% en el esperado y 25% en el optimista, diferenciación que captura la mayor base gravable en escenarios de mayor rentabilidad. La ganancia promedio por cliente por comisiones del marketplace se calculó en $15.49 MXN mensuales, valor derivado del promedio ponderado del cashback neto en las cinco categorías de comercio definidas en la sección 4.2.2. El ingreso promedio por crédito otorgado, que captura el margen neto después de pérdidas esperadas y costo de fondeo, es de $243.45 MXN durante el primer año y $434.83 MXN a partir del segundo año en el escenario esperado, diferencial explicado por el incremento de la comisión por apertura, la reducción del MDR pagado a la pasarela de pagos y la mejora del costo de fondeo conforme se consolida la trayectoria operativa.

### 5.4.7 Diferenciación entre escenarios

La Tabla 15 consolida los parámetros que difieren entre escenarios y constituyen las palancas de sensibilidad del modelo.

| Parámetro | Pesimista | Esperado | Optimista |
|---|---|---|---|
| Meta de suscriptores al mes 36 | 4,000 | 4,500 | 5,000 |
| Tasa de interés anual del crédito | 40% | 44% | 48% |
| MDR cobrado al comercio | 4.5% | 4.0% | 3.0% |
| Probabilidad de default (PD) | 13% | 12% | 12% |
| Pérdida dado incumplimiento (LGD) | 70% | 65% | 60% |
| Costo de fondeo anual | 17% | 16% | 15% |
| Inversión inicial total | $3,440,160 | $4,128,192 | $4,816,224 |
| Capital disponible para préstamos | $3,000,000 | $3,600,000 | $4,200,000 |
| Churn rate mensual | 3% | 2% | 2% |
| Carga fiscal sobre ingresos | 22% | 24% | 25% |

Tabla 15. Parámetros diferenciales por escenario del análisis financiero. Elaboración propia.

Es importante destacar que el escenario optimista contempla un capital de préstamos superior y, en consecuencia, una inversión inicial mayor, dado que un mayor volumen de originación requiere proporcionalmente más capital de trabajo. Esta dinámica implica que la rapidez de recuperación de la inversión no necesariamente es monotónica con respecto al optimismo de los supuestos operativos: un escenario con mayor crecimiento de cartera exige también un hoyo financiero inicial más profundo que debe ser amortizado posteriormente con los flujos operativos.

## 5.5 Resultados de las proyecciones

### 5.5.1 Escenario pesimista

El escenario pesimista representa el caso de mayor adversidad operativa simultánea para FinPet y constituye el piso de viabilidad financiera del proyecto. Bajo este escenario, la suscripción no alcanza la meta declarada de 4,500 usuarios al mes 36 y cierra con 3,249 suscriptores acumulados, equivalente al 81% del objetivo interno definido para este escenario (4,000). A pesar de esta penetración inferior, el proyecto logra revertir la senda de pérdidas mensuales y alcanza su primer resultado mensual positivo en el mes 13, coincidiendo con el inicio del segundo año, cuando la combinación de menores costos fijos, la entrada en vigor de la comisión de apertura de $550 MXN y la consolidación de la base de suscriptores recurrentes permite cubrir la estructura operativa.

El indicador más relevante de este escenario es el mes en que el resultado acumulado se vuelve positivo, momento en el cual el proyecto ha recuperado íntegramente la inversión inicial. Esto ocurre en el mes 48, último mes del horizonte de proyección, con un resultado acumulado de $52,964.93 MXN. Este resultado evidencia que, aun bajo el conjunto completo de supuestos adversos, el modelo logra ser autosuficiente con sus propios flujos antes de la conclusión del cuarto año, sin requerir capital adicional, aunque con un margen estrecho que deja escasa holgura ante desviaciones marginales adicionales. Al mes 48, el ingreso total mensual alcanza $425,014.99 MXN y el resultado mensual asciende a $210,022.16 MXN, mientras que el portafolio acumula 527 créditos otorgados a lo largo de los cuatro años, con una cartera viva al cierre de aproximadamente $2.88 millones MXN.

### 5.5.2 Pruebas de estrés

Las pruebas de estrés se ejecutaron bajo el principio ceteris paribus, modificando un único parámetro a la vez desde la base del escenario pesimista y observando hasta qué nivel el modelo conserva la capacidad de recuperar la inversión inicial dentro del horizonte de 48 meses. Este ejercicio permite identificar los puntos críticos del proyecto y dimensionar el margen de seguridad disponible frente a desviaciones específicas de cada variable. La Tabla 16 resume los límites de tolerancia identificados.

| Variable estresada | Valor base (pesimista) | Límite máximo tolerado | Margen disponible |
|---|---|---|---|
| Meta de suscriptores al mes 36 | 4,000 | 3,250 | -19% |
| Precio anualidad (MXN) | 799 | 769 | -3.8% |
| MDR cobrado al comercio | 4.5% | 5.3% | +0.8 pp |
| Tasa de interés anual | 40% | 34% | -6 pp |
| Comisión apertura año 1 (MXN) | 525 | 105 | -80% |
| Comisión apertura año 2 (MXN) | 550 | 220 | -60% |
| Enganche del crédito | 15% | 16% | +1 pp |
| PD primer año | 13% | 14% | +1 pp |
| PD segundo año | 10% | inelástico | sensibilidad crítica |
| Costo ingreso por cliente año 1 (MXN) | 105 | 141 | +34% |
| Costo ingreso por cliente año 2 (MXN) | 55 | 67 | +22% |
| Ingreso promedio por crédito año 1 (MXN) | 243.45 | 160 | -34% |
| Ingreso promedio por crédito año 2 (MXN) | 434.83 | 425 | -2.3% |
| Churn rate mensual | 3% | 3% | sin margen |
| Carga fiscal sobre ingresos | 22% | 22% | sin margen |

Tabla 16. Resultados del análisis de sensibilidad bajo el principio ceteris paribus. Elaboración propia.

Los resultados de las pruebas de estrés identifican como variables críticas para la viabilidad del proyecto la probabilidad de default del segundo año, el ingreso promedio por crédito del segundo año, el churn rate y la carga fiscal, donde el modelo prácticamente no admite desviaciones sin comprometer la recuperación de la inversión dentro del horizonte. En el extremo opuesto, variables como el MDR (con margen de 0.8 puntos porcentuales adicionales sobre el supuesto pesimista) y el costo de adquisición de cliente (con margen del 22%-34%) muestran holgura suficiente para absorber desviaciones operativas razonables. El supuesto del MDR pesimista del 4.5% resulta particularmente conservador si se considera que el promedio del mercado mexicano se ubica cerca del 1.4%, lo que indica que el modelo tiene un colchón sustancial en este rubro. Asimismo, el supuesto del costo de fondeo del 17% se ubica aproximadamente 7 puntos porcentuales por encima del promedio de las SOFOMes mexicanas, lo que sugiere que el modelo absorbería sin dificultad una tasa de mercado promedio.

### 5.5.3 Escenario esperado

El escenario esperado constituye la proyección central del proyecto y refleja las condiciones operativas más probables conforme a la calibración de mercado descrita en la sección 5.4. Bajo este escenario, FinPet alcanza 3,316 suscriptores al mes 24 y 4,423 al mes 36, ubicándose dentro del 98% de la meta declarada de 4,500. El primer resultado mensual positivo se registra en el mes 10, todavía dentro del primer año operativo, lo que constituye un punto de inflexión temprano respecto al escenario pesimista. La recuperación de la inversión inicial ocurre en el mes 37, once meses antes que en el escenario pesimista. Al cierre del horizonte de proyección, el resultado acumulado asciende a $4,008,134.74 MXN, lo que equivale a una ganancia neta acumulada cercana al 97% sobre la inversión inicial de $4,128,192 MXN.

La trayectoria operativa muestra que el modelo transita por tres fases claramente diferenciadas. La primera fase, comprendida entre los meses 1 y 9, corresponde al periodo de absorción de la inversión inicial y se caracteriza por resultados mensuales negativos que se moderan progresivamente conforme se consolida la base de suscriptores. La segunda fase, entre los meses 10 y 36, exhibe resultados mensuales positivos pero un resultado acumulado todavía deficitario, durante la cual el proyecto opera con autosuficiencia operativa pero aún no ha amortizado el capital invertido. La tercera fase, a partir del mes 37, corresponde al régimen de rentabilidad neta, donde tanto el flujo mensual como el resultado acumulado son positivos. Al mes 48 el ingreso total mensual alcanza $714,284.12 MXN y el resultado mensual del periodo se sitúa en $417,791.40 MXN, equivalente a un margen operativo del 58%.

El portafolio de crédito acumula un total de 714 créditos otorgados a lo largo de los cuatro años, con una cartera viva al mes 48 cercana a $4.5 millones MXN. El porcentaje de suscriptores con crédito abierto se estabiliza alrededor del 6%-8% de la base, comportamiento consistente con la tasa de incidencia de emergencias del 25% anual estimada en la sección 3.4 y con la lógica de que no todos los suscriptores con derecho a línea de crédito ejercerán esa opción en un mes dado.

### 5.5.4 Escenario optimista

El escenario optimista contempla la combinación más favorable de parámetros operativos: tasa de interés del 48% anual, MDR del 3%, PD del 11%, LGD del 65% y churn del 2%. Bajo estas condiciones, FinPet alcanza 3,546 suscriptores al mes 24 y 4,660 al mes 36, superando la meta declarada antes de tiempo. El primer resultado mensual positivo se adelanta al mes 7, anticipándose materialmente respecto a los otros dos escenarios, gracias a la combinación de mayor tasa de interés, menor probabilidad de default y mayor margen unitario por crédito desde las primeras disposiciones. La recuperación de la inversión inicial se materializa en el mes 34, seis meses antes que en el escenario esperado y catorce meses antes que en el pesimista, a pesar de que la inversión inicial de este escenario es la más elevada de los tres ($4,816,224 MXN).

Al cierre del horizonte de proyección el resultado acumulado del escenario optimista asciende a $6,349,675.22 MXN, lo que equivale a una ganancia neta acumulada del 132% sobre la inversión inicial. La superioridad financiera frente al escenario esperado es consistente en todos los indicadores: $2.34 millones MXN adicionales de resultado acumulado al mes 48, $194,696 MXN adicionales de ingreso mensual al mes 48 y $125,775 MXN adicionales de resultado mensual al mes 48. Esta dinámica confirma que en el escenario optimista la mayor inversión inicial es ampliamente compensada por la mayor velocidad de generación de margen por crédito y por la mayor escala del portafolio.

El volumen de originación crediticia en este escenario es sustancialmente mayor: el portafolio acumula 1,011 créditos otorgados durante los cuatro años, con una cartera viva al mes 48 cercana a $6.0 millones MXN. El ingreso total mensual al mes 48 alcanza $908,980.48 MXN y el resultado mensual del periodo se sitúa en $543,566.02 MXN, equivalente a un margen operativo del 60%, marginalmente superior al del escenario esperado, reflejo de las economías de escala que se obtienen al diluir los costos fijos sobre una base de operación más amplia.

### 5.5.5 Síntesis comparativa de los tres escenarios

La Tabla 17 consolida los indicadores de resultado más relevantes para los tres escenarios proyectados, permitiendo una lectura comparativa directa de la viabilidad financiera del proyecto.

| Indicador | Pesimista | Esperado | Optimista |
|---|---|---|---|
| Suscriptores al mes 24 | 2,593 | 3,317 | 3,546 |
| Suscriptores al mes 36 | 3,249 | 4,423 | 4,660 |
| Suscriptores al mes 48 | 3,584 | 5,418 | 5,733 |
| Mes con primer resultado mensual positivo | 13 | 10 | 7 |
| Mes de recuperación de la inversión inicial | 48 | 37 | 34 |
| Resultado acumulado al mes 24 (MXN) | -3,726,576 | -3,349,877 | -3,050,809 |
| Resultado acumulado al mes 36 (MXN) | -2,167,816 | -315,106 | 886,042 |
| Resultado acumulado al mes 48 (MXN) | 52,965 | 4,008,135 | 6,349,675 |
| Ingreso total mes 48 (MXN) | 425,015 | 714,284 | 908,980 |
| Resultado mensual al mes 48 (MXN) | 210,022 | 417,791 | 543,566 |
| Créditos totales originados (48 meses) | 527 | 714 | 1,011 |

Tabla 17. Síntesis comparativa de los resultados de proyección por escenario. Elaboración propia.

La lectura conjunta de los tres escenarios permite extraer cuatro conclusiones operativas. Primero, el modelo es robusto frente a la adversidad: incluso en el escenario pesimista, donde se combinan simultáneamente todas las desviaciones desfavorables de los parámetros, el proyecto logra recuperar la inversión inicial dentro del horizonte de proyección, sin necesidad de capital adicional. Segundo, los indicadores de tiempo a la rentabilidad operativa y a la recuperación de la inversión muestran una monotonicidad clara con respecto al optimismo de los supuestos: el primer mes con resultado mensual positivo se ubica en el mes 7, 10 y 13 para los escenarios optimista, esperado y pesimista respectivamente, y la recuperación de la inversión inicial ocurre en los meses 34, 37 y 48. Este ordenamiento confirma que las palancas operativas más sensibles a la rentabilidad terminal son la tasa de interés efectiva del crédito y la calidad crediticia del portafolio, capturadas conjuntamente en el ingreso promedio por crédito. Tercero, la diferencia en resultado acumulado terminal entre los escenarios esperado y pesimista es de aproximadamente $3.96 millones MXN, mientras que entre el optimista y el esperado es de $2.34 millones MXN, lo que indica una respuesta no lineal del proyecto a las desviaciones operativas y una asimetría favorable: el upside frente al caso central es proporcionalmente menor que el downside, lo cual constituye un perfil de retorno-riesgo atractivo desde la perspectiva del inversionista. Cuarto, el margen operativo mensual al mes 48 se ubica en niveles del 49%, 58% y 60% para los escenarios pesimista, esperado y optimista respectivamente, evidenciando que una vez superada la curva de aprendizaje y absorbida la inversión inicial, el modelo de negocio exhibe una rentabilidad operativa estructuralmente alta, consistente con la naturaleza de un modelo basado en ingresos recurrentes de suscripción y márgenes financieros sobre originación crediticia.