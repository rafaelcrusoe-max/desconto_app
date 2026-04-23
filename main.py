from src.models.desconto import DescontoVIP
from src.models.pedido import Pedido

if __name__ == "__main__":
    pedido = Pedido("Leonardo", DescontoVIP())

    valor_final = pedido.valor_final(100)
    print(f"Cliente: {pedido.cliente}")
    print(f"Valor final: {valor_final}")



# from src.services.pedido_service import PedidoService
# from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
# from src.models.pedido import Pedido

# if __name__ == "__main__":
#     service = PedidoService()

#     """Criando pedidos e aplicando descontos"""

#     pedido1 = Pedido("Cliente A", DescontoNormal())
#     pedido1.valor_original = 100.0  # Definindo o valor original do pedido

#     pedido2 = Pedido("Cliente B", DescontoVIP())
#     pedido2.valor_original = 200.0  # Definindo o valor original do pedido

#     pedido3 = Pedido("Cliente C", DescontoPremium())
#     pedido3.valor_original = 300.0  # Definindo o valor original do pedido

#     # Aqui você pode criar pedidos, aplicar descontos e processar os pedidos
#     service.adicionar_pedido(pedido1)
#     service.adicionar_pedido(pedido2)
#     service.adicionar_pedido(pedido3)

#     service.processar_pedidos()