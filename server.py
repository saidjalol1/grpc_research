from concurrent import futures
import grpc
from pb import product_pb2_grpc, product_pb2

TEST_DB = {}
NEXT_ID = 1

class ProductService(product_pb2_grpc.ProductServiceServicer):
    def CreateProduct(self, request, context):
        global NEXT_ID
        new_product = product_pb2.Product(
            id=NEXT_ID,
            name=request.name,
            description=request.description,
            price=request.price,
            discount=request.discount
        )
        TEST_DB[NEXT_ID] = new_product
        NEXT_ID += 1
        return new_product
    
    def GetProduct(self, request, context):
        product = TEST_DB.get(request.id)
        if not product:
            context.abort(
                grpc.StatusCode.NOT_FOUND, 
                f"Product {request.id} not found !")
        return product
    
    def DeleteProduct(self, request, context):
        product = TEST_DB.pop(request.id, None)
        if not product:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"Product {request.id} does not exist !")
        return product
    
    def UpdateProduct(self, request, context):
        if request.id not in TEST_DB:
            context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"Product {request.id} does not exist !")
        TEST_DB[request.id] = request
        return TEST_DB[request]
    
    def SearchProducts(self, request, context):
        results = [
            p for p in TEST_DB.values()
            if request.name.lower() in p.name.lower()
            and (request.min_price == 0 or p.price >= request.min_price)
            and (request.max_price == 0 or p.price <= request.max_price)]
        return product_pb2.ProductSearchResponse(products=results)
    

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port("[::]:50051")
    print("ProductService gRPC server running on port 50051...")
    server.start()
    server.wait_for_termination()
    

if __name__ == "__main__":
    server()