# nsd1903_review2

## OSI参考模型

1. 物理层
2. 数据链路层
3. 网络层
4. 传输层
5. 会话层
6. 表示层
7. 应用层

## TCP/IP参考模型
1. 物理层
2. 数据链路层
3. 网络层
4. 传输层
5. 应用层

问题：如果网络不通了，该怎么排查？
1. ping本网络中的IP地址（网关）。ping底层使用的是ICMP协议，工作在第三层，根据能否ping通，检查问题出现在高层还是低层。
2. 如果ping通，再ping名字，检查DNS解析。
3. 如果名称可以解析为名字，表明DNS服务正常。检查防火墙、服务配置
4. 如果ping不通，再检查低层问题，如地址是否配置正确，网线是否连接好。



物理层主要的是介质
数据链路层主要的技术与原理

- MAC地址：也叫硬件地址，共48位。前24位是厂商标识OUI，后24位厂商自定义。为了人为的方便，表示的时候，将2进制转换成16进制。
- 交换机工作原理：交换机根据它的MAC地址表转发数据帧。MAC地址表开始是空的，当交换机收到一个数据帧时，根据帧的源地址进行学习，生成MAC地址表。根据目标地址决定如何转发，如果目标地址还没有学习到，则向所有端口转发。
- 两个子层：MAC子层（介质访问控制）、LLC子层（逻辑链路控制）
- VLAN：虚拟局域网
- Trunk：中继
- STP：生成树协议
- 以太通道：将交换机上的多个物理端口逻辑上捆绑到一起，提供更大的带宽。



网络层主要的技术与原理

- IPv4地址：32位的2进制数，为了人为上的方便，每8位换算成一个10进制数，再把生成的4段10进制数用小数点分开，称作点分10进制的表示方法
  - ip地址的分类
    - A：前8位作为网络位，第1位必须是0。首字节范围是1－126，因为127被用作本地环回地址了
    - B：前16位作为网络位，前2位必须是10。首字节范围是128－191
    - C：前24位作为网络位，前3位必须是110。首字节范围是192－223
    - D：用作组播，也叫多播
    - E：保留
  - 私有地址
    - A：10.0.0.0/8
    - B：172.16.0.0 - 172.31.0.0/16
    - C：192.168.0.0 - 192.168.255.0/24

- 路由器：用于将不同的网络连接起来，形成逻辑上更大的一张网络。
- 网络的通信流程：A发数据给B
  - A先判断它和B是不是在同一网络，如果是在同一网络，直接发送，试图在局域网中找到目标。如果A发现B和自己不是一个网络的，则发送至网关。
  - A和B如果是不同网络。A把数据发给网关。网关一般是路由设备。
  - 路由器检查它的路由表，决定如何转发数据。如果查到了相应的条目，就从目标端口转发出去。如果路由表中没有对应的条目，则丢弃。

- 三层重要的协议：IP / ARP / ICMP

VRRP：虚拟冗余路由协议

允许客户端透明的使用网关。网络到外界有两个出口，那么设备网关指向任意一个出口都可以工作。但是，设备指向的出口如果出现故障，设备不能自动切换网关。

VRRP，可以创建虚拟路由器。网络中的节点，网关指向虚拟路由器即可。



传输层

- 协议：TCP / UDP
  - TCP：传输控制协议。面向连接的、可靠的协议
  - UDP：用户数据报协议。非面向连接的、不可靠的协议
- 端口号 -> /etc/services
  - ssh: 22
  - ftp: 20 / 21
  - telnet: 23
  - smtp: 25
  - dns: 53
  - tftp: 69
  - http: 80
  - https: 443
  - pop: 110
  - imap: 143
  - rpc: 111
  - nfs: 2049
  - ntp: 123
  - mysql: 3306
  - dhcp: 67 / 68
- 三次握手：A与B建立TCP连接

```sequence
A->B: syn=1
B->A: syn=1/ack=1
A->B: ack=1
```

- ACL：访问控制列表。
- NAT：网络地址转换。本质上，它用于将一个网络地址转换成另一个网络地址。应用时，经常是将私有地址转换成公有地址。
  - 动态转换：多对多
  - 静态转换：一对一

