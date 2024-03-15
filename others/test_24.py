def Test(arg, exp):
    seekresult = CH_232_温度传感器.Clear()

    seekresult = CH_232_加热棒.Clear()

    print('命令设定温度值为%d' % (arg[0]))

    Protocol_温度传感器.温度值.Value = arg[0]

    bool = Protocol_温度传感器.Write()

    API.Common.Timer.Normal.Sleep(1000)

    Protocol_加热棒.BlockRead()
    # 输出_加热棒
    print(Protocol_加热棒)

    if Protocol_加热棒.包头.Value != 0xFFFA:
        # 包头错误
        print('包头错误')

    if Protocol_加热棒.数据类型1.Value != 0x02:
        # 输出类型1错误
        print('类型1错误')

    if Protocol_加热棒.数据类型2.Value != 0x11:
        # 输出_类型2错误
        print('类型2错误')

    if Protocol_加热棒.数据长度.Value != 0x04:
        # 输出_长度错误
        print('长度错误')

    if Protocol_加热棒.包头.Value != 0xFFFA:
        # 输出_电压错误
        print('电压错误')

    if Protocol_加热棒.检验.Checked != True:
        # 输出校验和错误'
        print('校验和错误')

    if Protocol_加热棒.包尾.Value != 0x0F:
        # 输出包尾错误
        print('包尾错误')


Standard_Test(Test)
