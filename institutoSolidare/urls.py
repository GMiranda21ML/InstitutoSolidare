from django.urls import path
from institutoSolidare.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", home, name="home"),
    path("index", index, name="index"),
    path("adm-login/", admLogin, name="admLogin"),
    path("adm-main/", admMain, name="admMain"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("gerenciar-apadrinhados/", gerenciarApadrinhados,
         name="gerenciarApadrinhados"),
    path("cadastro-apadrinhados/", cadastrarApadrinhados,
         name="cadastroApadrinhados"),
    path("informacoes/<str:nome>/", informacoesApadrinhados,
         name="informacoesApadrinhados"),
    path("cadastro-status/", cadastroStatus, name="cadastroStatus"),
    path("cadastro-padrinhos/", cadastroPadrinhos, name="cadastroPadrinhos"),
    path("informacoes-padrinho/", informacoesPadrinho, name="informacoesPadrinho"),
    path("informacoes-extras-apadrinhado/", informacoesExtrasApadrinhado,
         name="informacoesExtrasApadrinhado"),
    path("login/", loginPadrinho, name="login"),
    path("meus-apadrinhados", meusApadrinhados, name="meusApadrinhados"),
    path("novo-apadrinhado", novoApadrinhado, name="novoApadrinhado"),
    path("informacao-meu-apadrinhado/<int:id>/",
         infoMeuApadrinhado, name="infoMeuApadrinhado"),
    path("escolher-apadrinhado", escolherApadrinhado, name="escolherApadrinhado"),
    path("meus-dados-padrinho", meusDadosPadrinho, name="meusDadosPadrinho"),
]
