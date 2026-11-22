import grpc
from pb import product_pb2_grpc, product_pb2


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)

        created = stub.CreateProduct(
            product_pb2.ProductCreateRequest(
                name="Computer",
                description="Ergonomic Bluetooth mouse",
                price=45.0,
                discount=5.0,
            )
        )
        print("Created:", created)

        fetched = stub.GetProduct(product_pb2.ProductGetRequest(id=created.id))
        print("Fetched:", fetched.name, f"${fetched.price}")

       
        search_res = stub.SearchProducts(
            product_pb2.ProductSearchRequest(name="mouse", max_price=100.0)
        )
        print("Found products:", len(search_res.products))

if __name__ == "__main__":
    run()