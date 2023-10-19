import asyncio
import etathermlib.etatherm as etatherm

def TestEtatherm():
    service=etatherm.Etatherm('192.168.15.35', 50001)

    params=asyncio.run(service.getParameters())
    print('Names', params)

    temps=asyncio.run(service.getCurrentTemperatures())
    print('Temps', temps)

    req=asyncio.run(service.getRequiredTemperatures())
    print('Req  ', req)
    
TestEtatherm()