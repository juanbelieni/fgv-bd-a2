-- Databse: brazil
drop database if exists brazil;

create database brazil;

use brazil;

-- Table: states
-- Primary key: code
create table states (
  code char(2) not null,
  name varchar(50) not null,
  primary key (code)
);

-- Table: cities
-- Primary key: id
-- Relation: cities.state_code -> states.code
create table cities (
  id integer primary key,
  name varchar(50) not null,
  state_code char(2) not null,
  geom geometry not null,
  foreign key (state_code) references states(code)
);

-- Inserting states
insert into
  states (code, name)
values
  ('AC', 'Acre'),
  ('AL', 'Alagoas'),
  ('AM', 'Amazonas'),
  ('AP', 'Amapá'),
  ('BA', 'Bahia'),
  ('CE', 'Ceará'),
  ('DF', 'Distrito Federal'),
  ('ES', 'Espírito Santo'),
  ('GO', 'Goiás'),
  ('MA', 'Maranhão'),
  ('MG', 'Minas Gerais'),
  ('MS', 'Mato Grosso do Sul'),
  ('MT', 'Mato Grosso'),
  ('PA', 'Pará'),
  ('PB', 'Paraíba'),
  ('PE', 'Pernambuco'),
  ('PI', 'Piauí'),
  ('PR', 'Paraná'),
  ('RJ', 'Rio de Janeiro'),
  ('RN', 'Rio Grande do Norte'),
  ('RO', 'Rondônia'),
  ('RR', 'Roraima'),
  ('RS', 'Rio Grande do Sul'),
  ('SC', 'Santa Catarina'),
  ('SE', 'Sergipe'),
  ('SP', 'São Paulo'),
  ('TO', 'Tocantins');