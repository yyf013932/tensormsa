import json
from rest_framework.response import Response
from rest_framework.views import APIView
from master.workflow.preprocess.workflow_feed_fr2seq import WorkflowFeedFr2Seq
class WorkFlowPreFeeder(APIView) :
    """

    """
    def post(self, request, src, net, nnid, ver, node):
        """
        - desc : insert data
        """
        try:
            nodeid = ''.join([nnid, '_', ver, '_', node])
            if(src == 'frame' and net == 'seq2seq') :
                return_data = WorkflowFeedFr2Seq().set_view_obj(nodeid , request.data)
            else :
                raise Exception("not supported converting type")
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def get(self, request, src, net, nnid, ver, node):
        """
        - desc : get data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def put(self, request, src, net, nnid, ver, node):
        """
        - desc ; update data
        """
        try:
            nodeid = ''.join([nnid, '_', ver, '_', node])
            if(src == 'frame' and net == 'seq2seq') :
                return_data = WorkflowFeedFr2Seq().set_view_obj(nodeid , request.data)
            else :
                raise Exception("not supported converting type")
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def delete(self, request, src, net, nnid, ver, node):
        """
        - desc : delete  data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))
