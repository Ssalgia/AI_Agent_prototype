import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from proto import agent_pb2
from proto import agent_pb2_grpc
import grpc
from concurrent import futures

class WorkflowService(agent_pb2_grpc.WorkflowServiceServicer):
    def AutomateTask(self, request, context):
        print(f"Received task: {request.task_name} with parameters: {request.parameters}")
        result = f"Task '{request.task_name}' automated successfully."
        return agent_pb2.WorkflowResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_pb2_grpc.add_WorkflowServiceServicer_to_server(WorkflowService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Workflow Automation Agent running on port 50052")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()


