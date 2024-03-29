
from pywps import LiteralInput, LiteralOutput, UOM, Process


class SayHello(Process):
    def __init__(self):
        inputs = [LiteralInput('name', 'Input name', data_type='string')]
        outputs = [LiteralOutput('response',
                                 'Output response', data_type='string')]

        super(SayHello, self).__init__(
            self._handler,
            identifier='say_hello',
            title='Process Say Hello 14h04',
            abstract='Returns a literal string output\
             with Hello plus the inputed ',
            version='1.3.3.7',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True,
            #execution_mode='pbs'
        )

    def _handler(self, request, response):
        response.outputs['response'].data = 'Hello la team HYSOPE II' + \
            request.inputs['name'][0].data
        response.outputs['response'].uom = UOM('unity')
        return response
