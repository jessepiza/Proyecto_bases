-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.2
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: inmobiliaria | type: DATABASE --
-- -- DROP DATABASE IF EXISTS inmobiliaria;
-- CREATE DATABASE inmobiliaria
-- 	ENCODING = 'UTF8'
-- 	LC_COLLATE = 'Spanish_Colombia.1252'
-- 	LC_CTYPE = 'Spanish_Colombia.1252'
-- 	TABLESPACE = pg_default
-- 	OWNER = postgres;
-- -- ddl-end --
-- 

-- object: public."Cliente" | type: TABLE --
-- DROP TABLE IF EXISTS public."Cliente" CASCADE;
CREATE TABLE public."Cliente" (
	"Cedula_ciudadania" integer NOT NULL,
	"Nombre" character varying(50) NOT NULL,
	"Apellido" character varying(50) NOT NULL,
	"Direccion" character varying(50) NOT NULL,
	"Ciudad" character varying(50) NOT NULL,
	"Numero_telefono" integer NOT NULL,
	CONSTRAINT "Cliente_pk" PRIMARY KEY ("Cedula_ciudadania")

);
-- ddl-end --
-- ALTER TABLE public."Cliente" OWNER TO postgres;
-- ddl-end --

-- object: public."Inmueble" | type: TABLE --
-- DROP TABLE IF EXISTS public."Inmueble" CASCADE;
CREATE TABLE public."Inmueble" (
	"Id_inmueble" smallint NOT NULL,
	"Direccion_inmueble" character varying(50) NOT NULL,
	"Sector" character varying(50) NOT NULL,
	"Area (metros)" numeric(8,3) NOT NULL,
	"Numero_habitaciones" smallint,
	"Numero_baños" smallint,
	"Estrato" smallint NOT NULL,
	"Precio" integer NOT NULL,
	"Antiguedad" integer NOT NULL,
	"Id_categoria" smallint,
	CONSTRAINT "Inmueble_pk" PRIMARY KEY ("Id_inmueble"),
	CONSTRAINT "Inmueble_uq" UNIQUE ("Id_categoria")

);
-- ddl-end --
-- ALTER TABLE public."Inmueble" OWNER TO postgres;
-- ddl-end --

-- object: public."Categoria" | type: TABLE --
-- DROP TABLE IF EXISTS public."Categoria" CASCADE;
CREATE TABLE public."Categoria" (
	"Id_categoria" smallint NOT NULL,
	"Tipo_inmueble" character varying(50) NOT NULL,
	CONSTRAINT "Categoria_pk" PRIMARY KEY ("Id_categoria")

);
-- ddl-end --
-- ALTER TABLE public."Categoria" OWNER TO postgres;
-- ddl-end --

-- object: public."Carrito_compra_Id_carrito_seq" | type: SEQUENCE --
-- DROP SEQUENCE IF EXISTS public."Carrito_compra_Id_carrito_seq" CASCADE;
CREATE SEQUENCE public."Carrito_compra_Id_carrito_seq"
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;
-- ddl-end --
-- ALTER SEQUENCE public."Carrito_compra_Id_carrito_seq" OWNER TO postgres;
-- ddl-end --

-- object: public."Carrito_compra" | type: TABLE --
-- DROP TABLE IF EXISTS public."Carrito_compra" CASCADE;
CREATE TABLE public."Carrito_compra" (
	"Id_carrito" smallint NOT NULL DEFAULT nextval('public."Carrito_compra_Id_carrito_seq"'::regclass),
	"Num_item" smallint NOT NULL,
	"Fecha_caducidad" date NOT NULL,
	"Cedula_ciudadania" integer,
	CONSTRAINT "Carrito_compra_pk" PRIMARY KEY ("Id_carrito"),
	CONSTRAINT "Carrito_compra_uq" UNIQUE ("Cedula_ciudadania")

);
-- ddl-end --
-- ALTER TABLE public."Carrito_compra" OWNER TO postgres;
-- ddl-end --

-- object: public."Ventas_Num_venta_seq" | type: SEQUENCE --
-- DROP SEQUENCE IF EXISTS public."Ventas_Num_venta_seq" CASCADE;
CREATE SEQUENCE public."Ventas_Num_venta_seq"
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;
-- ddl-end --
-- ALTER SEQUENCE public."Ventas_Num_venta_seq" OWNER TO postgres;
-- ddl-end --

-- object: public."Ventas" | type: TABLE --
-- DROP TABLE IF EXISTS public."Ventas" CASCADE;
CREATE TABLE public."Ventas" (
	"Num_venta" smallint NOT NULL DEFAULT nextval('public."Ventas_Num_venta_seq"'::regclass),
	"Pago_inicial" integer NOT NULL,
	"Pago_final" integer NOT NULL,
	"Fecha" date NOT NULL,
	"Id_carrito" smallint,
	"Id_empleado" smallint,
	CONSTRAINT "Ventas_pk" PRIMARY KEY ("Num_venta"),
	CONSTRAINT "Ventas_uq" UNIQUE ("Id_carrito")

);
-- ddl-end --
-- ALTER TABLE public."Ventas" OWNER TO postgres;
-- ddl-end --

-- object: public."Empleados_Id_empleado_seq" | type: SEQUENCE --
-- DROP SEQUENCE IF EXISTS public."Empleados_Id_empleado_seq" CASCADE;
CREATE SEQUENCE public."Empleados_Id_empleado_seq"
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;
-- ddl-end --
-- ALTER SEQUENCE public."Empleados_Id_empleado_seq" OWNER TO postgres;
-- ddl-end --

-- object: public."Empleados" | type: TABLE --
-- DROP TABLE IF EXISTS public."Empleados" CASCADE;
CREATE TABLE public."Empleados" (
	"Id_empleado" smallint NOT NULL DEFAULT nextval('public."Empleados_Id_empleado_seq"'::regclass),
	"Nombre" character varying(50) NOT NULL,
	"Apellido" character varying(50) NOT NULL,
	"Nom_cargo" character varying(50) NOT NULL,
	"Cedula_empleado" integer NOT NULL,
	"Nom_cargo1" character varying(50),
	CONSTRAINT "Empleados_pk" PRIMARY KEY ("Id_empleado"),
	CONSTRAINT "Empleados_uq" UNIQUE ("Nom_cargo")

);
-- ddl-end --
-- ALTER TABLE public."Empleados" OWNER TO postgres;
-- ddl-end --

-- object: public."Cargo_empleado" | type: TABLE --
-- DROP TABLE IF EXISTS public."Cargo_empleado" CASCADE;
CREATE TABLE public."Cargo_empleado" (
	"Nom_cargo" character varying(50) NOT NULL,
	"Salario" integer NOT NULL,
	"Horas_semanales" smallint NOT NULL,
	CONSTRAINT "Cargo_empleado_pk" PRIMARY KEY ("Nom_cargo")

);
-- ddl-end --
-- ALTER TABLE public."Cargo_empleado" OWNER TO postgres;
-- ddl-end --

-- object: public."many_Inmueble_has_many_Carrito_compra" | type: TABLE --
-- DROP TABLE IF EXISTS public."many_Inmueble_has_many_Carrito_compra" CASCADE;
CREATE TABLE public."many_Inmueble_has_many_Carrito_compra" (
	"Id_inmueble_Inmueble" smallint NOT NULL,
	"Id_carrito_Carrito_compra" smallint NOT NULL,
	CONSTRAINT "many_Inmueble_has_many_Carrito_compra_pk" PRIMARY KEY ("Id_inmueble_Inmueble","Id_carrito_Carrito_compra")

);
-- ddl-end --
-- ALTER TABLE public."many_Inmueble_has_many_Carrito_compra" OWNER TO postgres;
-- ddl-end --

-- object: public."Extras" | type: TABLE --
-- DROP TABLE IF EXISTS public."Extras" CASCADE;
CREATE TABLE public."Extras" (
	"Id_extra" smallint NOT NULL,
	"Nombre_extra" smallint NOT NULL,
	"Cantidad" smallint,
	"Id_inmueble" smallint NOT NULL,
	CONSTRAINT "Extras_pk" PRIMARY KEY ("Id_extra")

);
-- ddl-end --
-- ALTER TABLE public."Extras" OWNER TO postgres;
-- ddl-end --

-- object: "Inmueble_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Extras" DROP CONSTRAINT IF EXISTS "Inmueble_fk" CASCADE;
ALTER TABLE public."Extras" ADD CONSTRAINT "Inmueble_fk" FOREIGN KEY ("Id_inmueble")
REFERENCES public."Inmueble" ("Id_inmueble") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "Categoria_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Inmueble" DROP CONSTRAINT IF EXISTS "Categoria_fk" CASCADE;
ALTER TABLE public."Inmueble" ADD CONSTRAINT "Categoria_fk" FOREIGN KEY ("Id_categoria")
REFERENCES public."Categoria" ("Id_categoria") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Cliente_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Carrito_compra" DROP CONSTRAINT IF EXISTS "Cliente_fk" CASCADE;
ALTER TABLE public."Carrito_compra" ADD CONSTRAINT "Cliente_fk" FOREIGN KEY ("Cedula_ciudadania")
REFERENCES public."Cliente" ("Cedula_ciudadania") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Carrito_compra_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Ventas" DROP CONSTRAINT IF EXISTS "Carrito_compra_fk" CASCADE;
ALTER TABLE public."Ventas" ADD CONSTRAINT "Carrito_compra_fk" FOREIGN KEY ("Id_carrito")
REFERENCES public."Carrito_compra" ("Id_carrito") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Empleados_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Ventas" DROP CONSTRAINT IF EXISTS "Empleados_fk" CASCADE;
ALTER TABLE public."Ventas" ADD CONSTRAINT "Empleados_fk" FOREIGN KEY ("Id_empleado")
REFERENCES public."Empleados" ("Id_empleado") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Cargo_empleado_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Empleados" DROP CONSTRAINT IF EXISTS "Cargo_empleado_fk" CASCADE;
ALTER TABLE public."Empleados" ADD CONSTRAINT "Cargo_empleado_fk" FOREIGN KEY ("Nom_cargo")
REFERENCES public."Cargo_empleado" ("Nom_cargo") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Inmueble_fk" | type: CONSTRAINT --
-- ALTER TABLE public."many_Inmueble_has_many_Carrito_compra" DROP CONSTRAINT IF EXISTS "Inmueble_fk" CASCADE;
ALTER TABLE public."many_Inmueble_has_many_Carrito_compra" ADD CONSTRAINT "Inmueble_fk" FOREIGN KEY ("Id_inmueble_Inmueble")
REFERENCES public."Inmueble" ("Id_inmueble") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "Carrito_compra_fk" | type: CONSTRAINT --
-- ALTER TABLE public."many_Inmueble_has_many_Carrito_compra" DROP CONSTRAINT IF EXISTS "Carrito_compra_fk" CASCADE;
ALTER TABLE public."many_Inmueble_has_many_Carrito_compra" ADD CONSTRAINT "Carrito_compra_fk" FOREIGN KEY ("Id_carrito_Carrito_compra")
REFERENCES public."Carrito_compra" ("Id_carrito") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --


