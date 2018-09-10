import grpc

import calculator_pb2
import calculator_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.AdditionStub(channel)
        #Accept two numbers from user
        input1 = input("Enter number one for addition:\t")
        input2 = input("Enter number two for addition:\t")
        #Sends the 2 numbers as request parameters 
        response = stub.Addition(calculator_pb2.AddRequest(num1=int(input1), num2=int(input2)))
        #Response should be str
        print("Addition of two number is:\t"+str(response.result))

if __name__ == '__main__':
    run()
