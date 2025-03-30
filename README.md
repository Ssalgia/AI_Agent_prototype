# AI_Agent_prototype
This project demonstrates an AI Agent Operating System prototype that facilitates collaboration between vertical AI agents in an enterprise environment. The system architecture supports multiple AI agents with distinct roles and a communication framework for inter-agent collaboration. The project features the following components:

Data Analysis Agent

Workflow Automation Agent

Client for communication

Dashboard for performance monitoring

## Setup Instructions

1. Clone the Repository
   git clone <repository_url>
   cd AI_Agent

2. Create a Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Generate gRPC Code (if not already generated)
   python -m grpc_tools.protoc -I proto --python_out=proto -- 
   grpc_python_out=proto proto/agent.proto

## Running the AI Agents

Step 1: Start the Data Analysis Agent
        python agents/data_analysis_agent.py
        
Step 2: Start the Workflow Automation Agent 
        python agents/workflow_agent.py

 Step 3: Run the Client to Test Communication
         python client/agent_client.py

 Step 4: Launch the Dashboard
         streamlit run dashboard/dashboard.py

**Usage**

The client communicates with both the Data Analysis and Workflow Automation agents to share data and automate tasks. The dashboard provides real-time monitoring of agent performance.

**Troubleshooting**

If you encounter import issues with generated gRPC files, make sure to regenerate them using the command provided above.

Ensure that both agents are running before launching the client.


## Concepts Used

** 1. gRPC (Google Remote Procedure Call):
**
Used to facilitate communication between the AI agents.

The protocol buffer file (agent.proto) defines the structure for data exchange.

Enables real-time data sharing between agents through RPC methods.

** 2. Data Analysis and Workflow Automation:
**
* Two primary agents are developed:

a.Data Analysis Agent: Performs data processing tasks.

b.Workflow Automation Agent: Automates task management.

Both agents can share data and insights in real-time.

** 3. Machine Learning Integration:
**
One of the agents is integrated with a predictive model to analyze data.

The model can be dynamically updated with new data.

** 4.Performance Monitoring:
**
A dashboard (built using Streamlit) monitors agent performance metrics.

Includes task completion time, accuracy, and resource utilization.

** 5. Client-Server Communication:
**
A client script communicates with the AI agents.

Sends data requests and receives responses, facilitating collaborative actions.

** 6. Python Virtual Environment:
**
Uses a virtual environment to manage dependencies.

Requirements are specified in a requirements.txt file.

**6. Streamlit for Visualization:
**
The dashboard leverages Streamlit for real-time visualization and monitoring.

** Protobuf (Protocol Buffers):
**
Used for defining structured data that the gRPC framework uses for serialization and communication.

** Error Handling and Troubleshooting:
**
Instructions for regenerating the gRPC code if import issues arise.

Guidelines to ensure all agents are running before launching the client.
