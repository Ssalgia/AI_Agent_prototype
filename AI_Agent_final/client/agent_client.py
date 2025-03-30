import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grpc
import agent_pb2
import agent_pb2_grpc



def send_data(agent_name, data):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = agent_pb2_grpc.AgentServiceStub(channel)
        response = stub.ShareData(agent_pb2.DataRequest(agent_name=agent_name, data=data))
        print(f"Response from server: {response.message}")

send_data("DataAnalysisAgent", "Sample data for analysis")
