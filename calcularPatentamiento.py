import random as ra

costosFijosTextos = [
  "la inscripción del 0km",
  "título automotor",
  "cédula          ",
  "chapa patente   ",
  "alta de rentas  "
  ]

costosFijos = [
	1.5,
	400,
	780,
	180,
	220
	]

autos = [
	('Toyota','Etios','Aibo (utilitario)','2498000'),
	('Toyota','Etios','X MT (hatchback)','2579000'),
	('Fiat','Mobi','Like','2609400'),
	('Toyota','Etios','X MT (sedán)','2660000'),
	('Fiat','Cronos','Attractive','2873400'),
	('Renault','Duster Zen 1.6','Nafta , 1.6 L , 115cv , L4','4240300'),
	('Renault','Duster Intens 1.6 CVT','Nafta , 1.6 L , 115cv , L4','4240300'),
	('Chevrolet','Joy','Base 1.4','2987900'),
	('Toyota','Etios','XLS MT (hatchback)','3028000'),
	('Fiat','Strada','Endurance cabina plus','3032400'),
	('Renault','Logan','Life','3075000'),
	('Renault','Sandero','Life','3086000'),
	('Nissan','Versa','Sense MT','3149000'),
	('Toyota','Etios','XLS AT (hatchback)','3168000'),
	('Renault','Duster Outsaider 1.3T 4x2 CVT','Nafta , 1.3 L , 155cv , L4','4240300'),
	('Fiat','Cronos','Drive','3202000'),
	('Renault','Duster Iconic 1.3T 4x4','Nafta , 1.3 L , 155cv , L4','4240300'),	('Chevrolet','Joy Plus','Base 1.4','3089900'),
	('Toyota','Etios','XLS MT (sedán)','3111000'),
	('Volkswagen','Gol*','Trendline MT','3205500'),
	('Chevrolet','Joy Plus','Black Edition','3211900'),
	('Toyota','Yaris','XS MT (hatchback)','3233000'),
	('Fiat','Argo','Drive','3233200'),
	('Toyota','Etios','XLS AT (sedán)','3251000')
	]

print("Calcular patentamiento de Auto 0km"+
	"\n----------------------------------")
print("Al valor del vehículo hay que sumarle los costos adicionales \npor patentamiento, alta y habilitación; punto por punto, \nqué se abona al comprar un auto nuevo.\n")
autoElegido= autos[ra.randint(0,len(autos))]
valorInicial = autoElegido[3]
print(f"Auto: {autoElegido[0]}  {autoElegido[1]} {autoElegido[2]}")
print(f"Costo del Vehiculo: ${float(valorInicial)} ")
inscrip0km = costosFijos[0] * float(valorInicial) / 100
print(f"  {costosFijosTextos[0]}\t ${inscrip0km}")
sumaCostosFijos =0
print("Costos Fijos")
for i in range(1,len(costosFijos)):
	print("\t",costosFijosTextos[i], f" :\t ${costosFijos[i]:.2f}")
	sumaCostosFijos+= costosFijos[i]
print(f"Total Costos Fijos: \t ${sumaCostosFijos:.2f}")
print(f"\n TOTAL PATENTAMIENTO :  ${sumaCostosFijos + inscrip0km}" )
print(f"\n    Porcentaje {(100*(sumaCostosFijos + inscrip0km)/float(valorInicial)):.2f}%")


