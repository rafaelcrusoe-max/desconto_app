from src.app.entities.pedido import Pedido
from src.app.entities.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO

class CriarPedido:
    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(self, input_dto: CriarPedidoInputDTO) -> CriarPedidoOutputDTO:
        tipo_desconto = input_dto.tipo_desconto.lower().strip()
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")
        
        pedido = Pedido(input_dto.cliente, input_dto.valor_original, desconto)
        self.pedido_gateway.salvar(pedido)

        return CriarPedidoOutputDTO(
            cliente=pedido.cliente,
            valor_original=pedido.valor_original,
            valor_desconto=pedido.valor_desconto,
            valor_final=pedido.valor_final,
            tipo_desconto=pedido.tipo_desconto
        )

    def listar_pedido(self) -> list[Pedido]:
        return self.pedido_gateway.listar()
    
    def listar_pedidos(self) -> list[CriarPedidoOutputDTO]:
        pedidos = self.pedido_gateway.listar()

        lista_dto = []

        for registro in pedidos:
            pedido = registro["pedido"]
            dto = CriarPedidoOutputDTO(
                cliente=pedido.cliente,
                valor_original=pedido.valor_original,
                valor_desconto=pedido.valor_desconto(),
                valor_final=pedido.valor_final(),
                tipo_desconto=registro["tipo_desconto"]
            )
            lista_dto.append(dto)

        return lista_dto