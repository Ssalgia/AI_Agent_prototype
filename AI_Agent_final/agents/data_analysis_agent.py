import grpc 
from concurrent import futures
import agent_pb2 as agent_pb2
import agent_pb2_grpc as agent_pb2_grpc

class DataAnalysisAgent(agent_pb2_grpc.AgentServiceServicer):
    def ShareData(self, request, context):
        response = f"Processed data: {request.data} from {request.agent_name}"
        return agent_pb2.DataResponse(message=response)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(DataAnalysisAgent(), server)
    server.add_insecure_port('[::]:50051')
    print("Data Analysis Agent running on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
