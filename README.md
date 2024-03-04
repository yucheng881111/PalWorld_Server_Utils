# Frp Usage

## 下載
https://github.com/fatedier/frp/releases

## Reference
https://blog.csdn.net/qq_35427539/article/details/104001378

https://forum.gamer.com.tw/Co.php?bsn=25095&sn=14255

## 內網穿透、反向代理步驟

1. 準備一個具有公網ip的proxy server。推薦AWS EC2服務 (https://aws.amazon.com/tw/) 記得調整防火牆設定(allow all TCP, UDP)。

2. ssh進入proxy server。
3. 下載frp並解壓縮。
```
wget https://github.com/fatedier/frp/releases/download/v0.54.0/frp_0.54.0_linux_amd64.tar.gz
tar zxvf frp_0.54.0_linux_amd64.tar.gz
```
4. 執行frps。
```
cd frp_0.54.0_linux_amd64/
./frps
```
5. 回到真正的遊戲server端，同樣下載frp並修改設定檔frpc.toml。以帕魯為例，帕魯使用的是UDP with port 8211。
```
serverAddr = "your proxy server ip"
serverPort = 7000

[[proxies]]
name = "test-udp"
type = "udp"
localIP = "127.0.0.1"
localPort = 8211
remotePort = 8211
```
6. 執行frpc。
```
.\frpc -c .\frpc.toml
```
7. 終端顯示```start proxy success```和```incoming a new work connection for udp proxy, ip:7000```，即代理成功，代表成功將local端的port 8211 broadcast到公網ip的port 8211，在任何裝置上輸入ip:8211即可連線遊玩。
