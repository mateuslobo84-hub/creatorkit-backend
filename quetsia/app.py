import os
from flask import Flask, render_template

app = Flask(__name__)

CHECKOUT_URL = os.environ.get("CHECKOUT_URL", "https://pay.hotmart.com/P107593092M")

MODULOS = [
    ("A nova mentalidade do corretor", "Pare de apresentar imóveis e passe a conduzir decisões."),
    ("Os 4 passos do Método", "Diagnóstico, espelhamento, escada de SIMs e valor."),
    ("O primeiro atendimento", "A venda começa antes da apresentação do imóvel."),
    ("Qualificação", "Como descobrir o cliente por trás do lead."),
    ("Apresentação do imóvel", "Venda valor, não característica."),
    ("Condução da visita", "Como apresentar o imóvel e conduzir a visita."),
    ("Objeções", "Responda sem discutir e sem perder o cliente."),
    ("Negociação e fechamento", "Negocie sem pressionar e conduza ao sim."),
    ("Follow-up que converte", "Retome o contato com estratégia, sem insistência."),
]

APRENDER = [
    "Conduzir o primeiro atendimento",
    "Fazer perguntas estratégicas",
    "Identificar a real necessidade do cliente",
    "Qualificar leads",
    "Apresentar imóveis através de valor",
    "Conduzir visitas",
    "Responder objeções",
    "Negociar sem pressionar",
    "Conduzir para o fechamento",
    "Fazer follow-up com estratégia",
]

BONUS = [
    "Biblioteca de Scripts",
    "Checklist do atendimento",
    "Roteiro de visita",
    "Follow-up que não parece insistência",
]


@app.route("/")
def index():
    return render_template("index.html", checkout=CHECKOUT_URL, modulos=MODULOS,
                           aprender=APRENDER, bonus=BONUS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
