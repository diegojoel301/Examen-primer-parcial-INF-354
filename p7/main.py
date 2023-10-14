from kanren import Relation, facts, run, var

# Definir la relación de parentesco
parentera = Relation()
var1 = var()
facts(parentera, 
      # Padres
      ("Padre: Pedro", "Hijo: Freddy"),
      ("Padre: Pedro", "Hijo: Teddy"),
      ("Padre: Pedro", "Hijo: Willy"),
      ("Padre: Pedro", "Hija: Betty"),

      ("Padre: Pedro2", "Hijo: Luis"),
      ("Padre: Pedro2", "Hija: Ximena"),
      ("Padre: Pedro2", "Hija: Alison"),

      ("Madre: Paola", "Hijo: Freddy"),
      ("Madre: Paola", "Hijo: Teddy"),
      ("Madre: Paola", "Hijo: Willy"),
      ("Madre: Paola", "Hija: Betty"),

      ("Madre: Martha", "Hijo: Luis"),
      ("Madre: Martha", "Hija: Ximena"),
      ("Madre: Martha", "Hija: Alison"),


      ("Padre: Freddy", "Hijo: Diego"),
      ("Padre: Freddy", "Hijo: Sergio"),
      ("Madre: Ximena", "Hijo: Diego"),
      ("Madre: Ximena", "Hijo: Sergio"),

      ("Padre: Lucas", "Hijo: Henry"),
      ("Padre: Lucas", "Hija: Brenda"),
      ("Madre: Betty", "Hijo: Henry"),
      ("Madre: Betty", "Hija: Brenda"),

      ("Madre: Alison", "Hija: Yessica"),

      # Abuelos

      ("Abuelo: Pedro", "Nieto: Diego"),
      ("Abuelo: Pedro", "Nieto: Sergio"),
      ("Abuelo: Pedro", "Nieto: Henry"),
      ("Abuelo: Pedro", "Nieta: Brenda"),

      ("Abuelo: Pedro2", "Nieto: Diego"),
      ("Abuelo: Pedro2", "Nieto: Sergio"),
      ("Abuelo: Pedro2", "Nieta: Yessica"),

    
      ("Abuela: Paola", "Nieto: Diego"),
      ("Abuela: Paola", "Nieto: Sergio"),
      ("Abuela: Paola", "Nieto: Henry"),
      ("Abuela: Paola", "Nieta: Brenda"),

      ("Abuela: Martha", "Nieto: Diego"),
      ("Abuela: Martha", "Nieto: Sergio"),
      ("Abuela: Martha", "Nieta: Yessica"),

      # Nietos

      ("Abuelo: Pedro", "Nieto: Diego"),
      ("Abuelo: Pedro", "Nieto: Sergio"),
      ("Abuelo: Pedro", "Nieto: Henry"),
      ("Abuelo: Pedro", "Nieta: Brenda"),

      ("Abuelo: Pedro2", "Nieto: Diego"),
      ("Abuelo: Pedro2", "Nieto: Sergio"),
      ("Abuelo: Pedro2", "Nieta: Yessica"),

    
      ("Abuela: Paola", "Nieto: Diego"),
      ("Abuela: Paola", "Nieto: Sergio"),
      ("Abuela: Paola", "Nieto: Henry"),
      ("Abuela: Paola", "Nieta: Brenda"),

      ("Abuela: Martha", "Nieto: Diego"),
      ("Abuela: Martha", "Nieto: Sergio"),
      ("Abuela: Martha", "Nieta: Yessica"),



      # Hermanos

      ("Hermana: Paola", "Hermano: Nicolas"),

      ("Hermano: Freddy", "Hermano: Teddy"),
      ("Hermano: Freddy", "Hermano: Willy"),
      ("Hermano: Freddy", "Hermana: Betty"),

      ("Hermano: Teddy", "Hermano: Freddy"),
      ("Hermano: Teddy", "Hermano: Willy"),
      ("Hermano: Teddy", "Hermana: Betty"),

      ("Hermano: Willy", "Hermano: Teddy"),
      ("Hermano: Willy", "Hermano: Freddy"),
      ("Hermano: Willy", "Hermana: Betty"),

      ("Hermana: Betty", "Hermano: Teddy"),
      ("Hermana: Betty", "Hermano: Willy"),
      ("Hermana: Betty", "Hermano: Freddy"),


      ("Hermano: Luis", "Hermana: Ximena"),
      ("Hermano: Luis", "Hermana: Alison"),

      ("Hermana: Ximena", "Hermano: Luis"),
      ("Hermana: Ximena", "Hermana: Alison"),

      ("Hermana: Alison", "Hermano: Luis"),
      ("Hermana: Alison", "Hermana: Ximena"),

      ("Hermano: Henry", "Hermana: Brenda"),
      ("Hermana: Brenda", "Hermano: Henry"),

      ("Hermano: Diego", "Hermano: Sergio"),
      ("Hermano: Sergio", "Hermano: Diego"),

      # Tios

      ("Tio: Nicolas", "Sobrino: Freddy"),
      ("Tio: Nicolas", "Sobrino: Willy"),
      ("Tio: Nicolas", "Sobrino: Teddy"),
      ("Tio: Nicolas", "Sobrina: Betty"),

      ("Tio: Teddy", "Sobrino: Sergio"),
      ("Tio: Teddy", "Sobrina: Brenda"),
      ("Tio: Teddy", "Sobrino: Henry"),

      ("Tio: Teddy", "Sobrino: Diego"),
      ("Tio: Teddy", "Sobrino: Sergio"),
      ("Tio: Teddy", "Sobrina: Brenda"),
      ("Tio: Teddy", "Sobrino: Henry"),
      
      ("Tio: Willy", "Sobrino: Diego"),
      ("Tio: Willy", "Sobrino: Sergio"),
      ("Tio: Willy", "Sobrina: Brenda"),
      ("Tio: Willy", "Sobrino: Henry"),

      ("Tia: Betty", "Sobrino: Diego"),
      ("Tia: Betty", "Sobrino: Sergio"),
      
      ("Tio: Freddy", "Sobrina: Brenda"),
      ("Tio: Freddy", "Sobrino: Henry"),

      ("Tio: Luis", "Sobrino: Diego"),
      ("Tio: Luis", "Sobrino: Sergio"),
      ("Tio: Luis", "Sobrina: Yessica"),

      ("Tia: Alison", "Sobrino: Diego"),
      ("Tia: Alison", "Sobrino: Sergio"),
      ("Tia: Alison", "Sobrina: Yessica"),

      # Sobrinos
      ("Sobrino: Freddy", "Tio: Nicolas"),
      ("Sobrino: Willy", "Tio: Nicolas"),
      ("Sobrino: Teddy", "Tio: Nicolas"),
      ("Sobrina: Betty", "Tio: Nicolas"),

      ("Sobrino: Sergio", "Tio: Teddy"),
      ("Sobrina: Brenda", "Tio: Teddy"),
      ("Sobrino: Henry", "Tio: Teddy"),

      ("Sobrino: Diego", "Tio: Teddy"),
      ("Sobrino: Sergio", "Tio: Teddy"),
      ("Sobrina: Brenda", "Tio: Teddy"),
      ("Sobrino: Henry", "Tio: Teddy"),

      ("Sobrino: Diego", "Tio: Willy"),
      ("Sobrino: Sergio", "Tio: Willy"),
      ("Sobrina: Brenda", "Tio: Willy"),
      ("Sobrino: Henry", "Tio: Willy"),

      ("Sobrino: Diego", "Tia: Betty"),
      ("Sobrino: Sergio", "Tia: Betty"),

      ("Sobrina: Brenda", "Tio: Freddy"),
      ("Sobrino: Henry", "Tio: Freddy"),

      ("Sobrino: Diego", "Tio: Luis"),
      ("Sobrino: Sergio", "Tio: Luis"),
      ("Sobrina: Yessica", "Tio: Luis"),

      ("Sobrino: Diego", "Tia: Alison"),
      ("Sobrino: Sergio", "Tia: Alison"),

      # Primos
      
      ("Primo: Diego", "Primo: Henry"),
      ("Primo: Diego", "Prima: Brenda"),
      ("Primo: Diego", "Prima: Yessica"),
      
      ("Primo: Sergio", "Primo: Henry"),
      ("Primo: Sergio", "Prima: Brenda"),
      ("Primo: Sergio", "Prima: Yessica"),

      ("Prima: Brenda", "Primo: Diego"),
      ("Prima: Brenda", "Primo: Sergio"),

      ("Prima: Yessica", "Primo: Diego"),
      ("Prima: Yessica", "Primo: Sergio"),


      ("Primo: Henry", "Primo: Diego"),
      ("Primo: Henry", "Primo: Sergio"),

)

print(run(5,var1,parentera(var1,"Primo: Sergio")))
print(run(5,var1,parentera(var1,"Prima: Brenda")))
print(run(5,var1,parentera(var1,"Tio: Teddy")))
print(run(5,var1,parentera(var1,"Tio: Luis")))
print(run(5,var1,parentera(var1,"Nieto: Diego")))
print(run(5,var1,parentera(var1,"Nieta: Yessica")))
print(run(5,var1,parentera(var1,"Nieto: Henry")))
