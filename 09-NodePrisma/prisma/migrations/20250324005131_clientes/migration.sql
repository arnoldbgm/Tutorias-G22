-- CreateTable
CREATE TABLE "Clientes" (
    "id" SERIAL NOT NULL,
    "tipoDocumento" TEXT NOT NULL,
    "numeroDocumento" TEXT NOT NULL,
    "nombre" TEXT NOT NULL,
    "razonSocial" TEXT NOT NULL,
    "departamento" TEXT NOT NULL,
    "porvincia" TEXT NOT NULL,
    "distrito" TEXT NOT NULL,
    "domicilio" TEXT NOT NULL,
    "telefono" TEXT NOT NULL,
    "correo" TEXT NOT NULL,

    CONSTRAINT "Clientes_pkey" PRIMARY KEY ("id")
);
