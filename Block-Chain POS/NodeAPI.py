from flask_classful import FlaskView , route
from flask import Flask

node = None
class NodeAPI(FlaskView):
    def __init__(self):
        self.app = Flask(__name__)

    def start(self,apiPort):
        NodeAPI.register(self.app, route_base='/')
        self.app.run(host="localhost", port= apiPort)
    def injectNode(self, injectedNode):
        global node
        node = injectedNode

    @route('/info', methods=['GET'],)
    def info(self):
        return 'This is a communication interface to a nodes blockchain', 200

    @route('/blockchain', methods=['GET'],)
    def blockchain(self):
        return node.blockchain.toJson(), 200
