from django.urls import path

from .views import (
    index,
    transacoes_por_usuario,
    contas_por_usuario,
    nova_conta,
    nova_transacao,
    detalhe_conta,
    perfil_usuario
)

app_name = "finances"

urlpatterns = [
    path("", index, name="index"),
    path(
        "transactions/",
        transacoes_por_usuario,
        name="transacoes_por_usuario"
    ),
    path(
        "accounts/",
        contas_por_usuario,
        name="contas_por_usuario"
    ),
    path(
        "accounts/new/",
        nova_conta,
        name="nova_conta"
    ),
    path(
        "transactions/new/",
        nova_transacao,
        name="nova_transacao"
    ),
    path(
        "accounts/<int:conta_id>/",
        detalhe_conta,
        name="detalhe_conta"
    ),
    path(
        "perfil/",
        perfil_usuario,
        name="perfil_usuario"
    )
]