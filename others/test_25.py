def Test(arg, exp):
    seekresult = CH_232温度传感器.Clear()

    seekresult = CH_232加热棒.Clear()

    seekresult = CH_232散热风扇.Clear()

    print('命令设定温度值为%d' % (arg[0]))

    Protocol温度传感器.温度值.Value = arg[0]

    bool = Protocol_温度传感器.Write()

    API.Common.Timer.Normal.Sleep(400)

    Protocol温度传感器.温度值.Value = arg[1]

    bool = Protocol温度传感器.Write()

    API.Common.Timer.Normal.Sleep(500)

    Protocol温度传感器.温度值.Value = arg[2]

    bool = Protocol温度传感器.Write()

    API.Common.Timer.Normal.Sleep(500)

    Protocol散热风扇.BlockRead()

    print(Protocol散热风扇)

    if Protocol散热风扇.包头.Value != 0xFFFA:
        print('包头错误')

    if Protocol散热风扇.数据类型1.Value != 0x02:
        print('数据类型1错误')

    if Protocol散热风扇.数据类型2.Value != 0x22:
        print('数据类型2错误')

    if Protocol散热风扇.数据长度.Value != 0x01:
        print('长度错误')

    if Protocol_散热风扇.操作指令.Value != 0:
        print('指令错误')

    if Protocol散热风扇.检验.Checked != True:
        print('校验和错误')

    if Protocol散热风扇.包尾.Value != 0x0F:
        print('包尾错误')

    Protocol散热风扇.BlockRead()

    print(Protocol散热风扇)

    if Protocol散热风扇.包头.Value != 0xFFFA:
        print('包头错误')

    if Protocol散热风扇.数据类型1.Value != 0x02:
        print('1错误')

    if Protocol散热风扇.数据类型2.Value != 0x22:
        print('2错误')

    if Protocol散热风扇.数据长度.Value != 0x01:
        print('长度错误')

    if Protocol_散热风扇.操作指令.Value != 0:
        print('指令错误')

    if Protocol散热风扇.检验.Checked != True:
        print('校验和错误')

    if Protocol散热风扇.包尾.Value != 0x0F:
        print('包尾错误')

    Protocol散热风扇.BlockRead()

    print(Protocol散热风扇)

    if Protocol散热风扇.包头.Value != 0xFFFA:
        print('包头错误')

    if Protocol散热风扇.数据类型1.Value != 0x02:
        print('1错误')

    if Protocol散热风扇.数据类型2.Value != 0x22:
        print('2错误')

    if Protocol散热风扇.数据长度.Value != 0x01:
        print('长度错误')

    if Protocol_散热风扇.操作指令.Value != 1:
        print('指令错误')

    if Protocol散热风扇.检验.Checked != True:
        print('校验和错误')

    if Protocol散热风扇.包尾.Value != 0x0F:
        print('包尾错误')


Standard_Test(Text)
