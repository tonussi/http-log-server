from service.log_text_reader import LogTextReader

class TextLineService(object):
    """
    Receiver Controller 
    """

    def perform(self, line):
        """
        only public method that will perform the desired operation
        and maybe return some response for coordination of the rest
        """
        return self._text_by_line_number(line)

    # private

    def _text_by_line_number(self, line_number) -> dict:
        """
        check managers statuses return a dict to the endpoint
        """
        return LogTextReader().perform(line_number)
