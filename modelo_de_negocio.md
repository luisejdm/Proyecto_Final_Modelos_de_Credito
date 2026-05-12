# FinPet — Resumen del Modelo de Negocio

---

## 1. Descripción General

FinPet es una plataforma de financiamiento especializado para emergencias veterinarias, dirigida a propietarios de mascotas en Guadalajara, Jalisco. Opera bajo figura jurídica de **SOFOM E.N.R.**, con dos productos complementarios: una **membresía de suscripción anual** y una **línea de crédito pre-aprobada** de uso exclusivo en la red de comercios y clínicas afiliadas. Adicionalmente, la plataforma digital de FinPet opera como canal de promoción para los comercios afiliados, generando una fuente de ingreso adicional por comisión sobre ventas atribuidas a usuarios de la plataforma.

---

## 2. Productos

### 2.1 Membresía FinPet (Producto de Entrada)

El producto de suscripción es el mecanismo de captación y fidelización de clientes. Su función es triple: incorporar al cliente a la plataforma antes de que ocurra una emergencia, generar ingreso recurrente predecible, y actuar como reserva parcial contra pérdidas por impago en el portafolio de crédito.

La membresía tiene un costo anual de **$799 MXN**, con dos modalidades de pago:

| Modalidad | Precio | Forma de cobro |
|---|---|---|
| Pago mensualizado | $799 MXN/año | $66.58 MXN/mes domiciliados a tarjeta |
| Pago anual único | $649 MXN | Una sola exhibición al momento de la afiliación |

El descuento por pago anticipado ($150 MXN) incentiva la liquidez inmediata para FinPet y reduce el riesgo de cancelación por falta de domiciliación.

**Beneficios incluidos en la membresía:**

- Acceso a la línea de crédito pre-aprobada para emergencias veterinarias.
- **3% de cashback** en todas las compras realizadas con comercios afiliados a través de la plataforma FinPet, mediante registro de la transacción con el código de usuario único del suscriptor.
- El cashback acumulado es redimible exclusivamente como abono al siguiente pago mensual o anual de la membresía, o como abono a las cuotas del crédito activo. No se dispersa como efectivo.

> **Nota sobre el cashback:** El costo del cashback para FinPet está cubierto por la comisión del 5.5% que los comercios afiliados pagan sobre las ventas atribuidas a usuarios de la plataforma. El margen neto para FinPet sobre transacciones en el marketplace es del 2.5% (5.5% comisión cobrada − 3% cashback otorgado), sin costo directo de capital de trabajo.

---

### 2.2 Línea de Crédito Pre-Aprobada (Producto Principal)

El cliente se registra en la plataforma web o aplicación móvil de FinPet **antes** de que ocurra una emergencia. El motor crediticio evalúa su perfil y le asigna una línea de crédito pre-aprobada. Al momento de la emergencia, el cliente se identifica en la clínica afiliada y activa su línea disponible.

**Requisito de enganche mínimo:** Para activar el crédito, el cliente debe cubrir un monto mínimo de **$1,500 MXN de su propio bolsillo** directamente en la clínica al momento de la atención. Este mecanismo cumple dos funciones: reduce la exposición máxima de FinPet (EAD efectivo) y genera un compromiso financiero del cliente con la operación, desincentivando el uso irresponsable de la línea.

**Flujo operativo:**

```
Registro web/app → Evaluación crediticia → Línea pre-aprobada asignada
                                                      ↓
                                Emergencia en clínica afiliada
                                                      ↓
                           Cliente se identifica → Clínica valida línea
                                                      ↓
                     Cliente paga $1,500 MXN de enganche a la clínica
                                                      ↓
          FinPet desembolsa a la clínica el saldo neto:
          (Costo emergencia − Enganche cliente − Comisión MDR 5%)
                                                      ↓
                    Cliente paga a FinPet (emergencia − enganche) + intereses a plazos
```

**Ejemplo ilustrativo:**

| Concepto | Monto |
|---|---|
| Costo de la emergencia | $16,000 MXN |
| Enganche pagado por el cliente en la clínica | $1,500 MXN |
| Comisión MDR de FinPet (5% sobre $16,000) | $800 MXN |
| Desembolso de FinPet a la clínica | $13,700 MXN |
| Total recibido por la clínica ($1,500 + $13,700) | $15,200 MXN |
| Costo neto para la clínica (comisión MDR) | $800 MXN (5% del total) |
| Deuda del cliente con FinPet ($16,000 − $1,500) | $14,500 MXN + intereses |

La clínica recibe $15,200 MXN de forma garantizada e inmediata, cediendo únicamente el 5% del valor de la emergencia como comisión a FinPet por el servicio de financiamiento.

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

## 3. Red de Afiliados y Marketplace

### 3.1 Funciones de la red afiliada

La red de comercios afiliados cumple cuatro funciones simultáneas:

1. **Canal de distribución** de la membresía hacia clientes potenciales.
2. **Punto de acumulación** de cashback para los suscriptores, mediante el registro de compras con el código de usuario único de cada cliente.
3. **Punto de uso** del crédito al momento de la emergencia (aplica exclusivamente a clínicas veterinarias).
4. **Canal promocional** dentro del marketplace de la plataforma FinPet, donde los comercios pueden publicar ofertas y promociones dirigidas a la base de suscriptores.

### 3.2 Tipos de afiliado, roles y comisiones

| Tipo | Rol en cashback | Rol en crédito | Comisión pagada a FinPet |
|---|---|---|---|
| Clínica veterinaria | Acumulación | Desembolso de crédito | 5% MDR sobre monto financiado + 5.5% sobre ventas en marketplace |
| Tienda de alimentos/accesorios | Acumulación | No aplica | 5.5% sobre ventas atribuidas a usuarios FinPet |
| Estética y prestadores de servicio | Acumulación | No aplica | 5.5% sobre ventas atribuidas a usuarios FinPet |

### 3.3 Mecánica de atribución de ventas en el marketplace

Cada suscriptor de FinPet cuenta con un **código de usuario único** que presenta al comercio afiliado al momento de realizar una compra. El comercio registra la transacción en el portal FinPet mediante ese código, lo que permite:

- Acreditar el 3% de cashback en la cuenta del cliente de forma automática.
- Generar la obligación de pago del 5.5% de comisión por parte del comercio hacia FinPet.
- Construir un historial de comportamiento de gasto del cliente, enriqueciendo el perfil crediticio para futuras revisiones del límite de crédito.

---

## 4. Fuentes de Ingreso

El modelo opera con cuatro fuentes de ingreso diferenciadas:

### 4.1 Ingresos por Membresía
Pago anual ($649 en una exhibición o $799 en mensualidades de $66.58) por suscripción a la plataforma. Ingreso recurrente y predecible, cobrado de forma anticipada en la modalidad anual o mensualmente con domiciliación en la modalidad mensualizada.

### 4.2 Ingresos por Intereses del Crédito
Intereses cobrados al cliente sobre el monto financiado (costo de la emergencia menos el enganche de $1,500), pagados en cuotas mensuales durante el plazo acordado de 3 a 6 meses. Es la fuente de ingreso de mayor magnitud en el modelo.

### 4.3 Comisión por Desembolso (Merchant Discount Rate — MDR)
Al momento de activar el crédito, FinPet retiene el 5% del valor total de la emergencia como comisión. Este ingreso se realiza de forma inmediata al netear el desembolso a la clínica, sin estar sujeto al riesgo de impago del cliente. La clínica recibe el neto del desembolso de FinPet más el enganche del cliente, sumando el valor total de la emergencia menos la comisión MDR.

### 4.4 Comisión sobre Ventas en Marketplace (5.5%)
Los comercios afiliados pagan una comisión del 5.5% sobre el valor de las ventas realizadas a usuarios de FinPet y registradas mediante el código de usuario único. De este 5.5%, el 3% se transfiere al cliente como cashback y el 2.5% restante constituye ingreso neto para FinPet. Esta fuente de ingreso crece proporcionalmente con la base de suscriptores activos y el volumen de transacciones en la red afiliada.

---

## 5. Estructura de Costos (Resumen)

Conforme al archivo de estructura de costos del equipo, los principales bloques son:

| Bloque | Naturaleza |
|---|---|
| Costo de adquisición por cliente (buró + validación de identidad) | Variable por cliente nuevo |
| Publicidad (Meta Ads, Google, material en afiliados) | Fijo mensual |
| Nómina (4 empleados tradicionales + 1 UNE) | Fijo mensual |
| Soporte técnico (hosting web + app) | Fijo mensual |
| Ciberseguridad y suite en nube | Fijo mensual |
| Servicios contable y legal | Fijo mensual |
| Seguros de vehículos | Fijo mensual |
| Gasolina para reclutamiento de afiliados | Fijo mensual |

El costo del cashback otorgado a suscriptores está cubierto por la comisión del marketplace y no representa un egreso neto para FinPet, siempre que el volumen de transacciones registradas sea suficiente para compensarlo. El único costo de riesgo variable propio del portafolio de crédito es la pérdida esperada por impago:

| Bloque | Naturaleza |
|---|---|
| Pérdida esperada por impago (EL = PD × LGD × EAD efectivo) | Variable proporcional al portafolio de crédito |

Donde el **EAD efectivo = monto de la emergencia − $1,500 de enganche**, reduciendo la exposición máxima por operación respecto al valor bruto de la emergencia.

---

## 6. Propuesta de Valor por Actor

### Para el cliente propietario de mascota:
- Línea de crédito lista antes de la emergencia, sin trámites en el momento de mayor estrés emocional y financiero.
- Cashback del 3% en compras cotidianas con comercios afiliados, redimible contra la membresía o el crédito activo.
- Acceso a financiamiento formal sin necesidad de historial crediticio robusto, con solo $1,500 MXN de enganche al momento de la emergencia.

### Para la clínica veterinaria afiliada:
- Cobro garantizado e inmediato por emergencias que de otra forma se perderían o diferirían por incapacidad de pago del cliente.
- Costo de afiliación nulo: la comisión MDR del 5% se deduce únicamente cuando se activa un crédito, no hay cuota fija de membresía para el afiliado.
- Canal de promoción gratuito en el marketplace de FinPet hacia una base de suscriptores con perfil de gasto en mascotas verificado.

### Para comercios de alimentos, accesorios y servicios afiliados:
- Acceso a una base de clientes segmentada y con gasto verificado en el ecosistema de mascotas.
- Canal de promoción en el marketplace sin costo fijo: la comisión del 5.5% aplica solo sobre ventas efectivamente realizadas y registradas.
- Herramienta de fidelización: el cashback incentiva a los clientes FinPet a preferir comercios afiliados sobre la competencia.

### Para FinPet:
- Cuatro fuentes de ingreso diferenciadas con distintos perfiles de riesgo y recurrencia.
- El MDR se realiza de forma inmediata al desembolso, sin exposición al riesgo de impago.
- El cashback está financiado por la comisión del marketplace, eliminándolo como costo neto.
- El enganche de $1,500 reduce el EAD efectivo y la pérdida esperada por operación.

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
| Piloto | Meses 1–6 | 10 clínicas veterinarias afiliadas, primeros 100 suscriptores, primeros 10 créditos mensuales. Validación del motor crediticio, del flujo de enganche y del mecanismo de atribución de ventas por código de usuario. |
| Crecimiento | Meses 7–18 | Incorporación progresiva de tiendas de alimento y prestadores de servicios especializados. Lanzamiento del marketplace con comisión sobre ventas. Calibración del modelo de PD con datos propios. Expansión hacia las 450 unidades afiliadas objetivo. |
| Madurez | Año 2 en adelante | Red afiliada consolidada en 450 puntos. Migración del modelo crediticio a boosting. Evaluación de expansión geográfica fuera de la ZMG y de productos complementarios de cuidado preventivo financiado. |

---

*Documento de trabajo interno — sujeto a revisión y validación del equipo.*