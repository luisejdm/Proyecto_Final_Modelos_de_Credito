# FinPet — Resumen del Modelo de Negocio

---

## 1. Descripción General

FinPet es una plataforma de financiamiento especializado para emergencias veterinarias, dirigida a propietarios de mascotas en Guadalajara, Jalisco. Opera bajo figura jurídica de **SOFOM E.N.R.**, con dos productos complementarios: una **membresía de suscripción anual** y una **línea de crédito pre-aprobada** de uso exclusivo en la red de comercios y clínicas afiliadas.

---

## 2. Productos

### 2.1 Membresía FinPet (Producto de Entrada)

El producto de suscripción es el mecanismo de captación y fidelización de clientes, y actúa simultáneamente como reserva parcial contra pérdidas por impago en el portafolio de crédito.

Se proponen dos niveles:

| Característica | Plan Básico | Plan Premium |
|---|---|---|
| Precio anual | A definir | A definir |
| Cashback en red afiliada | Sí | Sí (tasa mayor) |
| Acceso a línea de crédito | Sí | Sí |
| Tasa preferencial en crédito | No | Sí |
| Proceso de activación en emergencia | Estándar | Prioritario |

> **Nota:** Los precios y tasas de cashback son variables a calibrar en el modelo financiero.

**Mecánica del cashback:**
- El cliente paga el total de su compra directamente en el comercio afiliado.
- El comercio registra la transacción en el portal FinPet.
- El cashback se acredita como saldo en la cuenta del cliente, redimible únicamente contra cuotas de su crédito activo o contra la renovación de su membresía.
- No se dispersa como efectivo, lo que elimina la necesidad de capital de trabajo para el cashback y refuerza el incentivo de repago.

---

### 2.2 Línea de Crédito Pre-Aprobada (Producto Principal)

El cliente se registra en la plataforma web de FinPet **antes** de que ocurra una emergencia. El motor crediticio evalúa su perfil y le asigna una línea pre-aprobada. Al momento de la emergencia, el cliente se identifica en la clínica afiliada y activa su línea disponible.

**Flujo operativo:**

```
Registro web → Evaluación crediticia → Línea pre-aprobada asignada
                                                    ↓
                              Emergencia en clínica afiliada
                                                    ↓
                         Cliente se identifica → Clínica valida línea
                                                    ↓
                    FinPet desembolsa a la clínica (neto de comisión)
                                                    ↓
                         Cliente paga a FinPet a plazos (3–6 meses)
```

**Segmentación de línea por PD estimado:**

| Segmento | PD Estimado | Línea Asignada (MXN) |
|---|---|---|
| Bajo riesgo | < 5% | $15,000 – $20,000 |
| Riesgo moderado-bajo | 5% – 10% | $10,000 – $14,999 |
| Riesgo moderado | 10% – 18% | $5,000 – $9,999 |
| Riesgo elevado | 18% – 25% | $2,000 – $4,999 |
| Riesgo inaceptable | > 25% | Rechazo |

Los umbrales son iniciales y se calibrarán conforme se acumule experiencia de repago en el portafolio propio. El modelo crediticio arranca con regresión logística y migra a modelo de boosting cuando el volumen de datos propios sea suficiente (estimado 12–18 meses de operación).

---

## 3. Red de Afiliados

La red de comercios afiliados cumple tres funciones simultáneas:

1. **Canal de distribución** de la membresía hacia clientes potenciales.
2. **Punto de acumulación** de cashback para los suscriptores.
3. **Punto de uso** del crédito al momento de la emergencia (aplica exclusivamente a clínicas veterinarias).

### Tipos de afiliado y su rol:

| Tipo | Rol en cashback | Rol en crédito | Comisión recibida |
|---|---|---|---|
| Clínica veterinaria | Acumulación | Desembolso | Comisión por referido de nuevos suscriptores |
| Tienda de alimentos/accesorios | Acumulación | No aplica | Comisión por referido de nuevos suscriptores |
| Estética veterinaria | Acumulación | No aplica | Comisión por referido de nuevos suscriptores |

---

## 4. Fuentes de Ingreso

El modelo opera con tres fuentes de ingreso diferenciadas:

### 4.1 Ingresos por Membresía
Pago anual por suscripción al plan básico o premium. Ingreso recurrente y predecible que constituye la base de la reserva contra impago.

### 4.2 Ingresos por Intereses del Crédito
Intereses cobrados al cliente sobre el monto del crédito utilizado, pagados en cuotas mensuales durante el plazo acordado (3–6 meses). Es la fuente de ingreso principal del modelo.

### 4.3 Comisión por Desembolso (Merchant Discount Rate)
Al momento de desembolsar el crédito a la clínica, FinPet retiene un porcentaje del monto total como comisión por el servicio de garantía de pago inmediato. La clínica recibe el neto. Este mecanismo es análogo al modelo de factoraje y al merchant discount que cobran los procesadores de pago.

**Ejemplo ilustrativo:**
- Crédito aprobado: $8,000 MXN
- Comisión FinPet (supuesto 5%): $400 MXN
- Monto recibido por la clínica: $7,600 MXN
- El cliente paga $8,000 MXN + intereses a FinPet en cuotas

---

## 5. Estructura de Costos (Resumen)

Conforme al archivo de estructura de costos del equipo, los principales bloques son:

| Bloque | Naturaleza |
|---|---|
| Costo de adquisición por cliente (buró + validación de identidad) | Variable por cliente |
| Publicidad (Meta Ads, Google, material en afiliados) | Fijo mensual |
| Nómina (4 empleados tradicionales + 1 UNE) | Fijo mensual |
| Soporte técnico (hosting web + app) | Fijo mensual |
| Ciberseguridad y suite en nube | Fijo mensual |
| Servicios contable y legal | Fijo mensual |
| Seguros de vehículos | Fijo mensual |
| Gasolina para reclutamiento de afiliados | Fijo mensual |

A estos se añaden dos costos propios del modelo de ingresos:

| Bloque | Naturaleza |
|---|---|
| Cashback otorgado a suscriptores | Variable proporcional al gasto en red afiliada |
| Pérdida esperada por impago (EL = PD × LGD × EAD) | Variable proporcional al portafolio de crédito |

---

## 6. Propuesta de Valor por Actor

### Para el cliente propietario de mascota:
- Línea de crédito lista antes de la emergencia, sin trámites en el momento de mayor estrés.
- Beneficios recurrentes (cashback) por gastos que ya realiza normalmente.
- Acceso a financiamiento formal sin necesidad de historial crediticio robusto.

### Para la clínica veterinaria afiliada:
- Cobro garantizado e inmediato por servicios que de otra forma se perderían por incapacidad de pago del cliente.
- Aumento en conversión de casos de emergencia que actualmente se cancelan o difieren.
- Sin costo de integración tecnológica compleja — solo validación de identidad del cliente en el portal.

### Para FinPet:
- Tres fuentes de ingreso diferenciadas con distinto perfil de riesgo y recurrencia.
- El ingreso por membresía actúa como reserva parcial predecible contra pérdidas por impago.
- La red de afiliados funciona como canal de distribución sin costo de adquisición directa por cliente.

---

## 7. Visión de Evolución del Modelo

El objetivo de expansión de la red afiliada para los primeros dos años de operación es el siguiente:

| Tipo de Afiliado | Objetivo a 2 años |
|---|---|
| Clínicas veterinarias (médico) | 200 |
| Tiendas de alimento y juguetes | 150 |
| Prestadores de servicios especializados (baño, corte de uñas, estética) | 100 |
| **Total red afiliada** | **450** |

La expansión se estructura en tres etapas:

| Etapa | Horizonte | Hito |
|---|---|---|
| Piloto | Meses 1–6 | 10 clínicas veterinarias afiliadas, primeros 100 suscriptores, primeros 10 créditos mensuales. Validación del motor crediticio y del flujo operativo de desembolso. |
| Crecimiento | Meses 7–18 | Incorporación progresiva de tiendas de alimento y prestadores de servicios especializados. Calibración del modelo de PD con datos propios. Expansión hacia las 450 unidades afiliadas objetivo. |
| Madurez | Año 2 en adelante | Red afiliada consolidada en 450 puntos. Migración del modelo crediticio a boosting. Evaluación de expansión geográfica fuera de la ZMG y de productos complementarios de cuidado preventivo financiado. |

---

*Documento de trabajo interno — sujeto a revisión y validación del equipo.*