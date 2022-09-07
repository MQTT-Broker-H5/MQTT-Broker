class c_SubscribePayload:
    def __init__(self,topicFilters:list,requestQoS:int):
        self._TopicFilters = topicFilters,
        self._RequestQoS = requestQoS

