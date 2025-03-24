/*
  Warnings:

  - You are about to drop the column `porvincia` on the `Clientes` table. All the data in the column will be lost.
  - Added the required column `provincia` to the `Clientes` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Clientes" DROP COLUMN "porvincia",
ADD COLUMN     "provincia" TEXT NOT NULL;
