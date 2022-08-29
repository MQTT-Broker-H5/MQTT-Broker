class c_SubscribePayload:
    def __init__(self,topicFilters:list,requestQoS:int):
        self._TopicFilters = topicFilters,
        self._RequestQoS = requestQoS

    def _Get_TopicFilters(self):
        return self._TopicFilters
    def _Get_RequestQoS(self):
        return self._RequestQoS

    def _Set_TopicFilters(self,value):
        self._TopicFilters = value
    def _Set_RequestQoS(self,value):
        self._RequestQoS = value

    TopicFilters = property(
        fget= _Get_TopicFilters,
        fset= _Set_RequestQoS)
    RequestQoS = property(
        fget= _Get_RequestQoS,
        fset= _Set_RequestQoS)




