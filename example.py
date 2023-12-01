'''Simple example'''
import asyncio
import etathermlib.etatherm as etatherm

async def TestEtatherm():
    service=etatherm.Etatherm('192.168.15.35', 50001)

    # params=await service.getParameters()
    # print('Params', params)

    # temps=await service.getCurrentTemperatures()
    # print('Temps', temps)

    req=await service.get_required_temperatures()
    print('Req  ', req)

    # req=await service.setMode(2,True)
    # print('Req ', req)

    # req=await service.setMode(2,False)
    # print('Req ', req)
    req=await service.set_temporary_temperature(2, 21, 30)
    print('Req  ', req)

    # req=await service.getRequiredTemperatures()
    # print('Req  ', req)
    
asyncio.run(TestEtatherm())
