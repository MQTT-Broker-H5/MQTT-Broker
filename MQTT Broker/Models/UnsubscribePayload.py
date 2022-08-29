class c_UnSubscribePayload:
    def __init__(self,topicFilters:list):
        self._TopicFilters = topicFilters

    def _Get_TopicFilters(self):
        return self._TopicFilters

    def _Set_TopicFilter(self,value):
        self._TopicFilters = value

    TopicFilters = property(
        fget= _Get_TopicFilters,
        fset= _Set_TopicFilter)






