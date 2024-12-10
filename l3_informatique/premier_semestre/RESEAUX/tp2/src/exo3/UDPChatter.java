package exo3;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.MulticastSocket;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.net.UnknownHostException;

public class UDPChatter {
    protected String username;
    protected MulticastSocket socket;
    protected int port;
    protected String inetAddr;
    protected String iface;

    public UDPChatter(String username,String inetAddr, String iface, int port) {
        this.username = username;
        this.inetAddr = inetAddr;
        this.port = port;
        this.iface = iface;
        
        try {
            InetAddress mCastAddr = InetAddress.getByName(this.inetAddr);
            InetSocketAddress group = new InetSocketAddress(mCastAddr, 0);
            NetworkInterface netIf = NetworkInterface.getByName(this.iface);
            this.socket = new MulticastSocket(this.port);
            this.socket.joinGroup(group, netIf);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void sendMessage(String msg) throws UnknownHostException {
        String signedMessage = username+": "+msg+"\n";
        DatagramPacket packet = new DatagramPacket(signedMessage.getBytes(), signedMessage.length(), InetAddress.getByName(this.inetAddr) , this.port);
        try {
            socket.send(packet);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void receiveMessage(){
        byte[] buffer = new byte[128];
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
        try {
            while(true) {
                socket.receive(packet);
                String recvMsg = new String(packet.getData(), "UTF-8");
                if (!recvMsg.startsWith(this.username)) {
                	System.out.println(recvMsg);
                }
                
            }
           
            
        } catch (IOException e) {
            if(socket.isClosed()) {
            	System.out.println("Socket Closed");
            }
        }
    }
}
