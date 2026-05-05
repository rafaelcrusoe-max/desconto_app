from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import memoryPedidoRepository

def main() -> None:
    database = MemoryDatabase()
    pedido_gateway = memoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    controller = PedidoController(criar_pedido_use_case)

    pedido1 = controller.criar_pedido("Cliente A", 100, "normal")
    pedido2 = controller.criar_pedido("Cliente B", 100, "vip")
    pedido3 = controller.criar_pedido("Cliente C", 100, "premium")

    print("Pedidos criados:")
    print(pedido1.cliente, pedido1.valor_original, pedido1.valor_final())
    print(pedido2.cliente, pedido2.valor_original, pedido2.valor_final())
    print(pedido3.cliente, pedido3.valor_original, pedido3.valor_final())

    if __name__== "__main__":
        main()















# from src.controllers.pedido_controller import PedidoController
# from src.repositories.pedido_repository import PedidoRepository
# from src.services.pedido_service import PedidoService
# from src.database.connection import DatabaseConnection
# from src.models.pedido import Pedido
# from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium

# if __name__ == "__main__":
#     database = DatabaseConnection()
#     repo = PedidoRepository(database)
#     service = PedidoService(repo)
#     controller = PedidoController(service)

#     pedido1 = Pedido("Cliente 1", DescontoNormal())
#     pedido1.valor_original = 100.0
#     pedido2 = Pedido("Cliente 2", DescontoVIP())
#     pedido2.valor_original = 100.0
#     pedido3 = Pedido("Cliente 3", DescontoPremium())
#     pedido3.valor_original = 100.0

#     controller.adicionar_pedido(pedido1)
#     controller.adicionar_pedido(pedido2)
#     controller.adicionar_pedido(pedido3)

#     controller.processar_pedidos()