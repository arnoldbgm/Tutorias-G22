## Configuración del proyecto de express

Partidos todo empezando por ejecutar el siguiente comando

```bash
npm init
```

Ahora instalamos  ***express***

```bash
npm install express
```

Ahora instalamos ***nodemon***

```bash
npm install --save-dev nodemon
```

Para este punto nuestro ***package.json*** debe lucir asi:

```json
{
  "name": "tutoria_express",
  "version": "1.0.0",
  "description": "Este sera el backend de mi proyecto final",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.19.2"   //ESTO ES EXPRESS
  },
  "devDependencies": {
    "nodemon": "^3.1.4"   //ESTO ES NODEMON
  }
}
```

Ahora para poder usar nodemon debemos de hacer un cambio en el package.json, debemos colocar  `“dev” : “nodemon app.js”`  Esto hara que cada vez que queramos levantar nuestro backend solo debamos de colocar en terminal `npm run dev` , tambien debemos de colocar el   `"type": "module",`

```json
{
  "name": "tutoria_express",
  "version": "1.0.0",
  "description": "Este sera el backend de mi proyecto final",
  "type": "module",     // Esto hemos agregado
  "main": "index.js", 
  "scripts": {
    "dev": "nodemon app.js",  // Esto es para trabajar con nodemon
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.19.2"
  },
  "devDependencies": {
    "nodemon": "^3.1.4"
  }
}
```

Una vez hecho todo esto pasamos a crear el archivo`app.js`, si lo vez esta en la raiz a la misma altura que mi `package.json`

![image](https://github.com/user-attachments/assets/76177d42-bf88-4024-8be1-c3219ddedad0)

Ahora dentro del archivo **`app.js`**, copiamos  y pegamos el siguiente codigo

```jsx
import express from "express";

// Aqui inicializo mi aplicacion en express
const app = express();
// Este sera el puerto que va a usar mi backend
const port = 3000;

// Aqui se ejecutara mi backend
// Esta parte solo se crea una vez y una vez ya configurada no se vuelve a tocar
try {
  app.listen(port, () => {
    console.log(`Mi Backend esta funcionando 🔥🎉🦾 `);
    console.log(`http://localhost:${port}/`);
  });
} catch (error) {
  console.log(error);
}
```

Con que te vayas a la terminal y ejecutes `npm run dev`, habras logrado levantar tu backend usando express

![image](https://github.com/user-attachments/assets/0671df69-1d80-48e7-9fa8-fc74666c67f3)

## Creación de nuestra Base de datos

Para comenzar con la creación de nuestra Bd, es importante que tengamos instalado prisma dentro de nuestro proyecto, por lo que ejecutaremos el siguiente comando

```bash
npm install prisma --save-dev
```

Ahora ejecutaremos lo siguiente, para poder instalar Prisma ORM 

```bash
npx prisma init 
```

Veremos que se nos crearon una carpeta llamada `prisma` y `.env` , no tengas miedo

![image](https://github.com/user-attachments/assets/57c7c0cc-e6f7-4f5b-8b33-f1e3ba10f8c5)

<aside>
💡 Es fundamental que comprendas que dentro de la carpeta de `prisma` es donde crearemos nuestra base de datos. El archivo `.env` nos permite especificar la ubicación de nuestra base de datos.

</aside>

🔥 ***IMPORTANTE (usaremos MYSQL) :  Ahora nos iremos a mysqlworkbech y crearemos desde ahi una bd, con el comando*** 

```sql
CREATE DATABASE IF NOT exists mi_base_de_datos;
```

<aside>
💡 Lo que hize aqui es crear una base de datos con el `nombe mi_base_de_datos`

</aside>

Ahora me ire al archivo `.env` para configurarlo, pero antes de configurarlo, este es el protocolo de como se configura 

![image](https://github.com/user-attachments/assets/a618a3b1-5832-4609-be9d-a4a2f528d5db)


```jsx
//Esto significa que solo debo de cambiar =>  mysql://USER:PASSWORD@HOST:PORT/DATABASE

// Asi es como nos viene por defecto
DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/mydb?schema=public"
 
// Pero debemos de cambiarlo por nuestro BD, USER, PASSWORD, HOST , PORT , DATABASE
// Asi seria en mi caso

DATABASE_URL="mysql://root:root@localhost:3306/mi_base_de_datos"   👍
```

Genial, ahora vamos, a la carpeta prisma donde cambiaremos el provider

```jsx
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "mysql"  // esto viene por defecto postgresql, solo lo cambiamos
  url      = env("DATABASE_URL")
}

model Categoria {
  id        Int      @id @default(autoincrement())
  nombre    String
  productos Producto[]
}

// Definición del modelo de Producto
model Producto {
  id          Int       @id @default(autoincrement())
  nombre      String
  descripcion String?
  precio      Float
  categoriaId Int
  categoria   Categoria @relation(fields: [categoriaId], references: [id])
}
```

Lo que hicimos fue modelar la siguiente base de datos.

![image](https://github.com/user-attachments/assets/02fed100-159b-4e0c-86b3-757d53460155)


Si tu vas y a tu mysql workbech veras que no tienes ninguna tabla y que tu base de datos esta vacia, y esto se debe porque aun no ejecutaste la migracion correspondiente, esta la debes de ejecutar en tu terminal, con esto ya podras observar tu bd.

```bash
npx prisma migrate dev 
```
## Seed SQL 🌱

### Creacion de tablas
```sql
-- Crear la tabla de marcas
CREATE TABLE tb_marca (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE
);

-- Crear la tabla de productos
CREATE TABLE tb_producto (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE
);

-- Crear la tabla de productos por marca
CREATE TABLE tb_producto_marca (
    id SERIAL PRIMARY KEY,
    id_producto INT NOT NULL REFERENCES tb_producto(id),
    id_marca INT NOT NULL REFERENCES tb_marca(id)
);

-- Crear la tabla de modelos
CREATE TABLE tb_modelos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    stock INT NOT NULL,
    descripcion TEXT,
    id_producto_marca INT NOT NULL REFERENCES tb_producto_marca(id)
);

```
### Inserceccion de datos
```sql
-- Insertar marcas
INSERT INTO tb_marca (nombre) VALUES
('Dell'),
('HP'),
('Apple'),
('Samsung');

-- Insertar productos
INSERT INTO tb_producto (nombre) VALUES
('Laptop'),
('Monitor');

-- Insertar relación producto-marca
INSERT INTO tb_producto_marca (id_producto, id_marca) VALUES
(1, 1),  -- Laptop - Dell
(2, 1),  -- Monitor - Dell
(1, 2),  -- Laptop - HP
(1, 3),  -- Laptop - Apple
(2, 4);  -- Monitor - Samsung

-- Insertar modelos
INSERT INTO tb_modelos (nombre, precio, stock, descripcion, id_producto) VALUES
-- Dell Laptops
('8GB RAM, 1TB HDD', 950.00, 12, 'Laptop básica', 1),
('16GB RAM, 512GB SSD', 1350.00, 5, 'Laptop para programadores', 1),
-- HP Laptops
('8GB RAM, 256GB SSD', 800.00, 20, 'Laptop económica', 3),
('16GB RAM, 1TB SSD', 1200.00, 10, 'Laptop de alto rendimiento', 3),
-- Apple Laptop
('M1 8GB, 256GB SSD', 1200.00, 8, 'MacBook Air M1', 4),
-- Dell Monitors
('24" Full HD', 200.00, 15, 'Monitor básico Dell', 2),
('27" 4K Ultra HD', 400.00, 10, 'Monitor profesional Dell', 2),
-- Samsung Monitor
('24" Full HD Curvo', 250.00, 18, 'Monitor curvo Samsung', 5);

```
![image](https://github.com/user-attachments/assets/f1e68331-f2ef-461e-b9d8-39d351ff5ab5)

https://dbdiagram.io/d/678300676b7fa355c398a965

## POST
Para hacer un metodo post en ``express`` nosotros debemos antes de coloclar el siguiente midlware:

```js
// Este me permite leer la data json. que es enviada por el cliente
app.use(bodyParser.json()) 
```
