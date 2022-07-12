## eci-hopp

https://metadata.fundacionsadosky.org.ar/

https://metadata.fundacionsadosky.org.ar/competition/26/

https://eci.dc.uba.ar/

 El objetivo es ayudar a una empresa de préstamos al consumo a "predecir el flujo de pagos de sus préstamos" para los próximos seis meses

 "La empresa busca entender la salud de su portafolio, lo que le permitirá tomar decisiones acertadas respecto al flujo de fondos futuro"

 ===========

https://metadata.fundacionsadosky.org.ar/competition/26/

El pago del préstamo ocurre en pagos mensuales o quincenales, con la posibilidad de adelantar cuotas.

Dentro de los tipos de préstamo que ofrece Hopp, uno de sus productos más populares son los préstamos de día de pago (PDL, por su nombre en inglés payday loans). Estos son préstamos de relativamente poco capital (comparado con, por ejemplo, una hipoteca) que se otorgan a una tasa de interés elevada por el riesgo de que el préstamo entre en mora y el monto prestado no sea cobrado. 

Los componentes de un préstamo son:
- Saldo de principal: monto remanente de capital adeudado del préstamo en cuestión.
- Saldo de interés: es el interés acumulado remanente sobre la deuda. La tasa de interés suele ser un porcentaje fijo mensual (o anual) sobre el capital original.
- Saldo de impuestos: una porción de los pagos por parte del prestatario suele estar sujeta a impuestos.


El objetivo de la competencia es, utilizando datos históricos de pagos de Hopp (enero 2019 - junio 2020), predecir los pagos de principal para cada préstamo activo. ( osea tiene mora menor a 180 dias )

??? Los créditos indexados por otros (D-Indexed) podrán ser considerados de manera diferencial respecto a los créditos en control directo de Hopp (Type “Base”). ??? 

===========

no usar fecha como input
podria ordenarlos y marcar cuando fue el siguiente pago tomando como referencia cuando deberia haber sido.

feature tipo de IVA , hacerlo como var categorica ? importa el orden porque quizas a mayor tipo , mayor riesto  

entender de un rate de frecuencia de pago ??

entender de un rate de cuanto % pago 