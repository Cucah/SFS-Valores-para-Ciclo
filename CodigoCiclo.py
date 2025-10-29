from math import pi

print("\n" * 100)
ValorRaio = float(input("Planet Radius (ex: 4000.0)"))

ValorAtmo = float(input("StartHeight (ex: -2500.0)"))

ValorHerobrine = ValorRaio * 2 * pi # (funcina na calculadora como: 8650 * 2pi)
ValorHeroi = ValorRaio - ValorAtmo # (atmosfera - altura)

ValorJagunco = ValorRaio / ValorHeroi # (vai dividir a porra toda)
ResultadoG = ValorJagunco * ValorHerobrine

print(f"result\nwidth: {ResultadoG:.1f}")
