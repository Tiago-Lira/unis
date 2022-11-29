import sys
import argparse
import sqlalchemy as sql
import sqlalchemy.orm as orm


Base = orm.declarative_base()


class ResultadoIMC(Base):
    __tablename__ = "resultado_imc"
    id = sql.Column(sql.Integer, primary_key=True)
    nome = sql.Column(sql.String)
    altura = sql.Column(sql.Integer)
    peso = sql.Column(sql.Float)
    imc = sql.Column(sql.Float)


class CalculadoraIMC:
    def calcular(self, args, session: orm.Session):
        altura = args.altura_cm
        peso = args.peso_kg
        nome = args.nome

        if altura <= 0:
            print("A altura tem que ser maior que zero.")
            return

        if peso <= 0:
            print("O peso tem que ser maior que zero.")
            return

        altura = altura / 100
        imc = round(peso / (altura * altura), 2)
        resultado = ResultadoIMC(
            nome=nome,
            altura=altura,
            peso=peso,
            imc=imc,
        )
        session.add_all([resultado])

        print("Resultado:\n-------------")
        self._imprimir(resultado)

    def listar_resultados(self, _, session: orm.Session):
        print("Resultados:\n-------------")
        stmt = sql.select(ResultadoIMC)

        for resultado in session.scalars(stmt):
            self._imprimir(resultado)
            print("-------------\n")

    def _imprimir(self, resultado: ResultadoIMC):
        print(f"Nome: {resultado.nome}")
        print(f"Altura: {resultado.altura}cm")
        print(f"Peso: {resultado.peso}kg")
        print(f"IMC: {resultado.imc}")


if __name__ == "__main__":
    # Iniciar banco e tabelas
    engine = sql.create_engine("sqlite:///ciclo4.db", future=True)
    Base.metadata.create_all(engine)
    imc = CalculadoraIMC()

    # Script
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Calcular
    calcular = subparsers.add_parser("calcular")
    calcular.add_argument("nome", type=str)
    calcular.add_argument("altura_cm", type=int)
    calcular.add_argument("peso_kg", type=int)
    calcular.set_defaults(func=imc.calcular)

    # Listar resultados
    listar_resultados = subparsers.add_parser("listar_resultados")
    listar_resultados.set_defaults(func=imc.listar_resultados)

    # Selecionar comando
    args = parser.parse_args(sys.argv[1:])

    if not hasattr(args, "func"):
        parser.print_help()
    else:
        with orm.Session(engine) as session:
            args.func(args, session)
            session.commit()
